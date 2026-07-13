import requests
import json

response = requests.post(
    "http://localhost:6333/collections/infocontact/points/scroll",
    json={
        "filter": {
            "must": [
                {
                    "key": "metadata.source_file",
                    "match": {
                        "value": "gestionnaire études doctorales SST.txt"
                    }
                }
            ]
        },
        "limit": 10
    }
)
print(json.dumps(response.json(), indent=2))
