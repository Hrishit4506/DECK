import requests
import json

API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImUwZDQ5MTA0LWNjYjItNDc2Mi04NjYxLThkMDA5OThkZjI1YyIsImlhdCI6MTc2OTU5NTE0MCwic3ViIjoiZGV2ZWxvcGVyLzgzNmQ2ZTRhLWVlNjktMmI2NS02OGJlLTQ3MzdiNjU3ZjhhMSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0OS4zNi44MS4xNDkiXSwidHlwZSI6ImNsaWVudCJ9XX0.7KMB-CtdpMTcPKJzXWQ6tAhZQJz4F1h3NFwqwUWDltb5sptDclAQhZY0XlewNNOeVZFPGmZujur2BPL3UBBPiQ"

url = "https://api.clashroyale.com/v1/arena/54000011"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)

    with open("leaderboard.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("cards.json saved successfully ✅")
else:
    print("Error:", response.status_code)