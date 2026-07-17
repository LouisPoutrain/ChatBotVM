(function () {
    // 1. Configuration
    // Automatically determine the API base URL from where this script is hosted
    const currentScript = document.currentScript;
    const apiBaseUrl = currentScript ? new URL(currentScript.src).origin : "http://127.0.0.1:8600";
    const API_URL = `${apiBaseUrl}/api/chat`;
    const PRIMARY_COLOR = "#ea580c"; // Orange vibrant (inspiré de l'image)
    const BOT_NAME = "VICTORIA";
    
    // Generate a unique session ID for the user
    const SESSION_ID = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);

    // 2. Inject CSS
    const style = document.createElement("style");
    style.innerHTML = `
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

        #univ-chatbot-root {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 999999;
            font-family: 'Inter', sans-serif;
            pointer-events: none; /* Let clicks pass through empty areas */
        }
        
        #univ-chatbot-root * {
            box-sizing: border-box;
            pointer-events: auto; /* Re-enable clicks for actual elements */
        }

        /* Floating Action Button */
        #univ-fab {
            width: 75px;
            height: 75px;
            border-radius: 50%;
            background: ${PRIMARY_COLOR};
            box-shadow: 0 4px 20px rgba(234, 88, 12, 0.4);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
            position: absolute;
            bottom: 0;
            right: 0;
        }

        #univ-fab:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 25px rgba(234, 88, 12, 0.6);
        }

        #univ-fab svg {
            width: 36px;
            height: 36px;
            fill: white;
            transition: transform 0.3s ease;
        }

        /* Tooltip */
        #univ-chat-tooltip {
            position: absolute;
            bottom: 90px;
            right: 0;
            background: white;
            color: #334155;
            padding: 12px 16px;
            border-radius: 12px;
            border-bottom-right-radius: 4px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            font-size: 14px;
            font-weight: 500;
            white-space: nowrap;
            opacity: 0;
            transform: translateY(10px);
            animation: univFadeInUp 0.5s ease forwards 1s;
            transition: opacity 0.3s ease, transform 0.3s ease;
            pointer-events: none;
        }
        
        #univ-chat-tooltip::after {
            content: '';
            position: absolute;
            bottom: -6px;
            right: 24px;
            width: 12px;
            height: 12px;
            background: white;
            transform: rotate(45deg);
        }

        #univ-chat-tooltip.hidden {
            opacity: 0 !important;
            transform: translateY(10px) !important;
        }

        /* Backdrop */
        #univ-chatbot-backdrop {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.4);
            backdrop-filter: blur(4px);
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.4s ease;
            z-index: -1;
        }

        #univ-chatbot-backdrop.active {
            opacity: 1;
            pointer-events: auto;
        }

        /* Chat Window (Floating Modal) */
        #univ-chat-window {
            position: fixed;
            top: 50%;
            left: 50%;
            width: 850px;
            height: 80vh;
            max-width: 95vw;
            max-height: 900px;
            background: #ffffff;
            border-radius: 16px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            opacity: 0;
            transform: translate(-50%, -45%) scale(0.95);
            pointer-events: none;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        #univ-chat-window.active {
            opacity: 1;
            transform: translate(-50%, -50%) scale(1);
            pointer-events: auto;
        }

        /* Header */
        #univ-chat-header {
            background: ${PRIMARY_COLOR};
            padding: 20px;
            color: white;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .univ-header-info {
            display: flex;
            flex-direction: column;
        }

        .univ-header-title {
            font-weight: 600;
            font-size: 16px;
            margin: 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .univ-status-dot {
            width: 8px;
            height: 8px;
            background: #4ade80;
            border-radius: 50%;
            box-shadow: 0 0 8px rgba(74, 222, 128, 0.6);
        }

        .univ-header-subtitle {
            font-size: 12px;
            opacity: 0.8;
            margin-top: 4px;
        }

        /* Messages Area */
        #univ-chat-messages {
            flex: 1;
            padding: 30px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            background: #f8fafc;
            scroll-behavior: smooth;
        }

        .univ-message-wrapper {
            display: flex;
            gap: 16px;
            align-items: flex-start;
            margin-bottom: 24px;
            animation: univFadeInUp 0.3s ease forwards;
            opacity: 0;
            transform: translateY(10px);
        }

        .univ-msg-wrapper-user {
            flex-direction: row-reverse;
        }

        .univ-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 16px;
            flex-shrink: 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .univ-avatar-user {
            background: #334155;
            color: white;
        }

        .univ-avatar-bot {
            background: ${PRIMARY_COLOR};
            color: white;
        }

        .univ-message {
            max-width: 80%;
            padding: 16px 20px;
            border-radius: 12px;
            font-size: 15px;
            line-height: 1.6;
            word-wrap: break-word;
        }

        .univ-message p {
            margin: 0 0 12px 0;
        }
        .univ-message p:last-child {
            margin: 0;
        }
        .univ-message a {
            color: ${PRIMARY_COLOR};
            text-decoration: none;
            font-weight: 500;
        }
        .univ-message a:hover {
            text-decoration: underline;
        }

        .univ-msg-user {
            background: #f1f5f9;
            color: #1e293b;
            border-top-right-radius: 4px;
        }

        .univ-msg-bot {
            background: white;
            color: #334155;
            border: 1px solid #e2e8f0;
            border-top-left-radius: 4px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.02);
        }

        .univ-contact-card {
            margin-top: 12px;
            padding: 12px;
            background: rgba(14, 165, 233, 0.05);
            border-left: 3px solid ${PRIMARY_COLOR};
            border-radius: 4px 8px 8px 4px;
            font-size: 13px;
        }

        /* Input Area */
        #univ-chat-input-area {
            padding: 16px;
            background: white;
            border-top: 1px solid #e2e8f0;
            display: flex;
            gap: 12px;
            align-items: center;
        }

        #univ-chat-input {
            flex: 1;
            border: none;
            background: #f1f5f9;
            padding: 12px 16px;
            border-radius: 20px;
            font-size: 14px;
            outline: none;
            font-family: inherit;
            transition: box-shadow 0.2s;
        }

        #univ-chat-input:focus {
            box-shadow: 0 0 0 2px rgba(14, 165, 233, 0.2);
            background: white;
        }

        #univ-chat-submit {
            background: ${PRIMARY_COLOR};
            color: white;
            border: none;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: background 0.2s, transform 0.2s;
        }

        #univ-chat-submit:hover {
            background: #0284c7;
            transform: scale(1.05);
        }

        #univ-chat-submit svg {
            width: 16px;
            height: 16px;
            fill: white;
        }
        
        #univ-chat-submit:disabled {
            background: #cbd5e1;
            cursor: not-allowed;
            transform: none;
        }

        /* Loader */
        .univ-typing-wrapper {
            display: none;
            gap: 16px;
            align-items: flex-start;
            margin-bottom: 24px;
            animation: univFadeInUp 0.3s ease forwards;
        }

        .univ-typing-indicator {
            display: flex;
            gap: 4px;
            padding: 16px 20px;
            background: white;
            border-radius: 12px;
            border-top-left-radius: 4px;
            border: 1px solid #e2e8f0;
            align-items: center;
        }

        .univ-dot {
            width: 6px;
            height: 6px;
            background: #cbd5e1;
            border-radius: 50%;
            animation: univBounce 1.4s infinite ease-in-out both;
        }

        .univ-dot:nth-child(1) { animation-delay: -0.32s; }
        .univ-dot:nth-child(2) { animation-delay: -0.16s; }

        @keyframes univFadeInUp {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes univBounce {
            0%, 80%, 100% { transform: scale(0); }
            40% { transform: scale(1); }
        }
    `;
    document.head.appendChild(style);

    // 3. Inject HTML
    const root = document.createElement("div");
    root.id = "univ-chatbot-root";

    root.innerHTML = `
        <div id="univ-chatbot-backdrop"></div>
        <div id="univ-chat-window">
            <div id="univ-chat-header">
                <div class="univ-header-info">
                    <h3 class="univ-header-title">
                        <div class="univ-status-dot"></div>
                        ${BOT_NAME} - ChatBot de la DRV 
                    </h3>
                    <div class="univ-header-subtitle">Posez toutes vos questions sur l'université</div>
                </div>
            </div>
            <div id="univ-chat-messages">
                <div class="univ-message-wrapper">
                    <div class="univ-avatar univ-avatar-bot">VI</div>
                    <div class="univ-message univ-msg-bot">
                        <p>Bonjour ! Je suis VICTORIA le ChatBot de la DRV. Je peux vous aider à trouver des informations sur les formations, les procédures administratives, et vous orienter vers les bons contacts.</p>
                        <p>Afin de m'aider à vous répondre au mieux, merci d'être le plus précis possible dans vos questions.</p>
                        <p>Comment puis-je vous aider aujourd'hui ?</p>
                    </div>
                </div>
                <div class="univ-typing-wrapper" id="univ-typing">
                    <div class="univ-avatar univ-avatar-bot">VI</div>
                    <div class="univ-typing-indicator">
                        <div class="univ-dot"></div><div class="univ-dot"></div><div class="univ-dot"></div>
                    </div>
                </div>
            </div>
            <div id="univ-chat-input-area">
                <input type="text" id="univ-chat-input" placeholder="Tapez votre message..." autocomplete="off">
                <button id="univ-chat-submit" disabled>
                    <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
                </button>
            </div>
        </div>
        <div id="univ-chat-tooltip">Une question sur la DRV ?</div>
        <div id="univ-fab">
            <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/></svg>
        </div>
    `;

    const container = document.getElementById("univ-chatbot-container") || document.body;
    container.appendChild(root);

    // 4. Logic
    const fab = document.getElementById("univ-fab");
    const chatWindow = document.getElementById("univ-chat-window");
    const input = document.getElementById("univ-chat-input");
    const submitBtn = document.getElementById("univ-chat-submit");
    const messagesArea = document.getElementById("univ-chat-messages");
    const typingIndicator = document.getElementById("univ-typing");

    const backdrop = document.getElementById("univ-chatbot-backdrop");
    const tooltip = document.getElementById("univ-chat-tooltip");

    let isOpen = false;

    // Toggle open/close
    function toggleChat() {
        isOpen = !isOpen;
        if (isOpen) {
            tooltip.classList.add("hidden");
            backdrop.classList.add("active");
            chatWindow.classList.add("active");
            fab.innerHTML = `<svg viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>`;
            setTimeout(() => input.focus(), 300);
        } else {
            backdrop.classList.remove("active");
            chatWindow.classList.remove("active");
            fab.innerHTML = `<svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/></svg>`;
        }
    }

    fab.addEventListener("click", toggleChat);
    backdrop.addEventListener("click", toggleChat); // Close when clicking outside

    // Input handling
    input.addEventListener("input", () => {
        submitBtn.disabled = input.value.trim().length === 0;
    });

    input.addEventListener("keypress", (e) => {
        if (e.key === "Enter" && !submitBtn.disabled) {
            sendMessage();
        }
    });

    submitBtn.addEventListener("click", sendMessage);

    /**
     * Convertit un texte Markdown basique en HTML (Gras, Italique, Liens).
     * @param {string} text Le texte brut reçu de l'API.
     * @returns {string} Le texte formaté en HTML.
     */
    function parseText(text) {
        if (!text) return "";
        let html = text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>')
            .replace(/\n/g, '<br>');
        return html;
    }

    /**
     * Gère l'envoi d'un message utilisateur à l'API et l'affichage de la réponse.
     * Désactive le champ de saisie pendant le chargement et affiche l'indicateur de frappe.
     */
    async function sendMessage() {
        const text = input.value.trim();
        if (!text) return;

        addMessage(text, 'user');
        input.value = '';
        submitBtn.disabled = true;

        typingIndicator.style.display = 'flex';
        messagesArea.appendChild(typingIndicator);
        scrollToBottom();

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ question: text, history: [], session_id: SESSION_ID })
            });

            if (!response.ok) throw new Error("Erreur réseau");

            const data = await response.json();

            typingIndicator.style.display = 'none';

            let botHtml = parseText(data.response);
            if (data.contact_info) {
                botHtml += `<div class="univ-contact-card"><strong>Contact expert :</strong><br>` + parseText(data.contact_info) + `</div>`;
            }

            addMessage(botHtml, 'bot', true);

        } catch (error) {
            console.error("Erreur API:", error);
            typingIndicator.style.display = 'none';
            addMessage("Désolé, une erreur est survenue lors de la communication avec le serveur. Veuillez réessayer plus tard.", 'bot');
        }
    }

    /**
     * Ajoute une bulle de message dans l'interface de discussion.
     * @param {string} content Le contenu du message.
     * @param {string} sender L'expéditeur du message ('user' ou 'bot').
     * @param {boolean} isHtml Détermine si le contenu doit être interprété comme du HTML.
     */
    function addMessage(content, sender, isHtml = false) {
        const wrapper = document.createElement("div");
        wrapper.className = `univ-message-wrapper univ-msg-wrapper-\${sender}`;
        
        const avatar = document.createElement("div");
        avatar.className = `univ-avatar univ-avatar-\${sender}`;
        avatar.textContent = sender === 'user' ? 'U' : 'AI';

        const div = document.createElement("div");
        div.className = `univ-message univ-msg-\${sender}`;

        if (isHtml) {
            div.innerHTML = content;
        } else {
            div.textContent = content;
        }

        wrapper.appendChild(avatar);
        wrapper.appendChild(div);

        messagesArea.insertBefore(wrapper, typingIndicator);
        scrollToBottom();
    }

    /**
     * Fait défiler la zone de discussion vers le bas pour afficher le message le plus récent.
     */
    function scrollToBottom() {
        setTimeout(() => {
            messagesArea.scrollTop = messagesArea.scrollHeight;
        }, 50);
    }

})();
