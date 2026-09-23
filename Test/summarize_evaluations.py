import json
import glob
import os
import re

import sys

def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "Results"
    if not os.path.exists(target_dir):
        target_dir = "."

    json_files = sorted(glob.glob(os.path.join(target_dir, "**/*trials*.json"), recursive=True))
    if not json_files:
        json_files = sorted(glob.glob(os.path.join(target_dir, "*trials*.json")))
    
    total_faithfulness = 0
    total_answer_relevance = 0
    total_context_precision = 0
    total_rag_duration = 0
    total_eval_duration = 0
    total_total_duration = 0
    total_tokens = 0
    count = 0
    time_count = 0
    
    results_by_file = {}
    
    output_lines = ["# Bilan des Évaluations (LLM as a Judge)\n"]
    
    for file_path in json_files:
        rel_path = os.path.relpath(file_path, target_dir)
        parent_dir = os.path.basename(os.path.dirname(file_path))
        base_name = os.path.basename(file_path)
        if base_name in ("trials.json", "data.json") and parent_dir and parent_dir != ".":
            display_name = parent_dir
        else:
            display_name = rel_path.replace("\\", "/")

        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                continue
                
        trials = data.get("trials", [])
        
        file_faithfulness = 0
        file_answer_relevance = 0
        file_context_precision = 0
        file_rag_duration = 0
        file_eval_duration = 0
        file_total_duration = 0
        file_tokens = 0
        file_count = 0
        file_time_count = 0
        
        file_details = []
        
        # Lire le fichier de log pour extraire les tokens générés "cachés" (HyDE + Pensées)
        log_file_path = file_path.replace("_trials.json", "_log.txt")
        if not os.path.exists(log_file_path):
            candidate = os.path.join(os.path.dirname(file_path), "run_logs.txt")
            if os.path.exists(candidate):
                log_file_path = candidate
        extra_tokens_per_trial = []
        
        if os.path.exists(log_file_path):
            with open(log_file_path, 'r', encoding='utf-8') as lf:
                log_content = lf.read()
            blocks = log_content.split("[TIMESTAMP]")
            blocks = blocks[1:] # ignorer l'entête
            if len(blocks) > len(trials):
                blocks = blocks[-len(trials):]
            
            for block in blocks:
                block_tokens = 0
                # Extraire le document HyDE
                hyde_match = re.search(r"\[DOCUMENT HYPOTHÉTIQUE \(HyDE\)\]\n(.*?)(?=\n\s*\[BOUCLE AGENTIQUE\]|\n\s*\[DOCUMENTS RÉCUPÉRÉS\])", block, flags=re.DOTALL)
                if hyde_match:
                    hyde_content = hyde_match.group(1).strip()
                    if not hyde_content.startswith("N/A (Bypass"):
                        block_tokens += int((len(hyde_content.split()) * 1.3 + len(hyde_content) / 4.0) / 2)
                        
                # Extraire les pensées de la boucle agentique
                pensees = re.findall(r"\[Pensée\]\s*:\s*(.*?)(?=\n\s*\[Action\]\s*:)", block, flags=re.DOTALL)
                for p in pensees:
                    p_strip = p.strip()
                    block_tokens += int((len(p_strip.split()) * 1.3 + len(p_strip) / 4.0) / 2)
                
                extra_tokens_per_trial.append(block_tokens)
        
        # S'il y a un décalage ou pas de log, on remplit de zéros
        while len(extra_tokens_per_trial) < len(trials):
            extra_tokens_per_trial.append(0)
        
        for i, trial in enumerate(trials):
            question = trial.get("question", "N/A")
            rag_dur = float(trial.get("rag_duration_s", 0) or 0)
            eval_dur = float(trial.get("eval_duration_s", 0) or 0)

            total_dur = float(trial.get("total_duration_s", 0) or 0)
            
            final_answer = trial.get("final_answer", "")
            ans_tokens = int((len(final_answer.split()) * 1.3 + len(final_answer) / 4.0) / 2)
            est_tokens = trial.get("exact_completion_tokens", ans_tokens + extra_tokens_per_trial[i])
            
            file_rag_duration += rag_dur
            file_eval_duration += eval_dur
            file_total_duration += total_dur
            file_tokens += est_tokens
            file_time_count += 1
            
            total_rag_duration += rag_dur
            total_eval_duration += eval_dur
            total_total_duration += total_dur
            total_tokens += est_tokens
            time_count += 1
            
            eval_data = trial.get("evaluation", {})
            
            if not eval_data:
                continue
                
            if "error" in eval_data:
                file_details.append(f"### Question : {question}\n- **Erreur d'évaluation** : {eval_data['error']}\n- **Temps** : RAG: {rag_dur:.2f}s, Eval: {eval_dur:.2f}s, Total: {total_dur:.2f}s\n- **Tokens générés** : {est_tokens}\n")
                continue
                
            faith = eval_data.get("faithfulness")
            relevance = eval_data.get("answer_relevance")
            precision = eval_data.get("context_precision")
            
            try:
                faith = float(faith)
                relevance = float(relevance)
                precision = float(precision)
            except (ValueError, TypeError):
                faith = None
                relevance = None
                precision = None
            
            # sometimes scores might be missing or None
            if faith is not None and relevance is not None and precision is not None:
                file_faithfulness += faith
                file_answer_relevance += relevance
                file_context_precision += precision
                file_count += 1
                
                total_faithfulness += faith
                total_answer_relevance += relevance
                total_context_precision += precision
                count += 1
                
                detailed_reasoning = eval_data.get("detailed_reasoning", {})
                reasoning = eval_data.get("reasoning", "")
                
                detail_str = f"### Question : {question}\n"
                detail_str += f"- **Notes** : Faithfulness: {faith}/5, Answer Relevance: {relevance}/5, Context Precision: {precision}/5\n"
                detail_str += f"- **Temps** : RAG: {rag_dur:.2f}s, Eval: {eval_dur:.2f}s, Total: {total_dur:.2f}s\n"
                detail_str += f"- **Tokens générés** : {est_tokens}\n"
                
                if isinstance(detailed_reasoning, dict):
                    if detailed_reasoning.get('faithfulness'):
                        detail_str += f"- **Avis Faithfulness** : {detailed_reasoning.get('faithfulness')}\n"
                    if detailed_reasoning.get('answer_relevance'):
                        detail_str += f"- **Avis Answer Relevance** : {detailed_reasoning.get('answer_relevance')}\n"
                    if detailed_reasoning.get('context_precision'):
                        detail_str += f"- **Avis Context Precision** : {detailed_reasoning.get('context_precision')}\n"
                if reasoning:
                    detail_str += f"- **Reasoning global** : {reasoning}\n"
                    
                file_details.append(detail_str)
        
        if file_count > 0:
            results_by_file[display_name] = {
                "avg_faithfulness": file_faithfulness / file_count,
                "avg_answer_relevance": file_answer_relevance / file_count,
                "avg_context_precision": file_context_precision / file_count,
                "count": file_count,
                "avg_rag_duration": file_rag_duration / file_time_count if file_time_count else 0,
                "avg_eval_duration": file_eval_duration / file_time_count if file_time_count else 0,
                "avg_total_duration": file_total_duration / file_time_count if file_time_count else 0,
                "avg_tokens": file_tokens / file_time_count if file_time_count else 0,
                "time_count": file_time_count,
                "details": file_details
            }
        else:
            results_by_file[display_name] = {
                "count": 0,
                "avg_faithfulness": 0,
                "avg_answer_relevance": 0,
                "avg_context_precision": 0,
                "avg_rag_duration": file_rag_duration / file_time_count if file_time_count else 0,
                "avg_eval_duration": file_eval_duration / file_time_count if file_time_count else 0,
                "avg_total_duration": file_total_duration / file_time_count if file_time_count else 0,
                "avg_tokens": file_tokens / file_time_count if file_time_count else 0,
                "time_count": file_time_count,
                "details": file_details
            }

    # Global averages
    output_lines.append("## Moyennes Globales\n")
    if count > 0:
        output_lines.append(f"- **Faithfulness** : {total_faithfulness/count:.2f} / 5")
        output_lines.append(f"- **Answer Relevance** : {total_answer_relevance/count:.2f} / 5")
        output_lines.append(f"- **Context Precision** : {total_context_precision/count:.2f} / 5")
        output_lines.append(f"- *Nombre de réponses évaluées avec succès : {count}*")
    else:
        output_lines.append("Aucune évaluation avec des scores trouvée.")
        
    if time_count > 0:
        output_lines.append(f"- **Temps moyen RAG** : {total_rag_duration/time_count:.2f}s")
        output_lines.append(f"- **Temps moyen Évaluation** : {total_eval_duration/time_count:.2f}s")
        output_lines.append(f"- **Temps moyen Total** : {total_total_duration/time_count:.2f}s")
        output_lines.append(f"- **Tokens moyens générés** : {int(total_tokens/time_count)}")
        output_lines.append(f"- *Nombre total de requêtes chronométrées : {time_count}*\n")
    else:
        output_lines.append("Aucune donnée de temps trouvée.\n")

    # Tableau comparatif
    if results_by_file:
        output_lines.append("## 📊 Tableau Comparatif des Configurations\n")
        output_lines.append("| Configuration / Modèle | Faithfulness | Relevance | Context Precision | RAG (s) | Eval (s) | Total (s) | Tokens Moy. | Évaluations |")
        output_lines.append("|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|")
        for name, res in sorted(results_by_file.items()):
            faith_str = f"{res['avg_faithfulness']:.2f} / 5" if res["count"] > 0 else "N/A"
            rel_str = f"{res['avg_answer_relevance']:.2f} / 5" if res["count"] > 0 else "N/A"
            prec_str = f"{res['avg_context_precision']:.2f} / 5" if res["count"] > 0 else "N/A"
            rag_str = f"{res['avg_rag_duration']:.2f}s" if res["time_count"] > 0 else "N/A"
            eval_str = f"{res['avg_eval_duration']:.2f}s" if res["time_count"] > 0 else "N/A"
            total_str = f"{res['avg_total_duration']:.2f}s" if res["time_count"] > 0 else "N/A"
            tok_str = f"{int(res['avg_tokens'])}" if res["time_count"] > 0 else "N/A"
            cnt_str = f"{res['count']}"
            output_lines.append(f"| **{name}** | {faith_str} | {rel_str} | {prec_str} | {rag_str} | {eval_str} | {total_str} | {tok_str} | {cnt_str} |")
        output_lines.append("")
        
    output_lines.append("## Détails par Configuration\n")
    
    for filename, res in results_by_file.items():
        output_lines.append(f"### Configuration : {filename}")
        if res["count"] > 0:
            output_lines.append(f"- Moyenne Faithfulness : {res['avg_faithfulness']:.2f} / 5")
            output_lines.append(f"- Moyenne Answer Relevance : {res['avg_answer_relevance']:.2f} / 5")
            output_lines.append(f"- Moyenne Context Precision : {res['avg_context_precision']:.2f} / 5")
        output_lines.append(f"- *Évaluations réussies : {res['count']}*")
        
        if res["time_count"] > 0:
            output_lines.append(f"- Temps moyen RAG : {res['avg_rag_duration']:.2f}s")
            output_lines.append(f"- Temps moyen Évaluation : {res['avg_eval_duration']:.2f}s")
            output_lines.append(f"- Temps moyen Total : {res['avg_total_duration']:.2f}s")
            output_lines.append(f"- Tokens moyens générés : {int(res['avg_tokens'])}")
        output_lines.append("")
        
    output_lines.append("---\n## Détails des évaluations (Notes et Commentaires du Juge)\n")
    for filename, res in results_by_file.items():
        output_lines.append(f"## {filename}\n")
        for detail in res["details"]:
            output_lines.append(detail)
            
    out_file = os.path.join(target_dir, "conclusion_evaluations.md")
    with open(out_file, "w", encoding="utf-8") as out_f:
        out_f.write("\n".join(output_lines))
        
    print(f"Fichier {out_file} généré avec succès ! (Basé sur {len(json_files)} fichiers)")

if __name__ == "__main__":
    main()
