import requests

url = "https://poisonpie.us-west.host.bsky.network/xrpc/app.bsky.actor.putPreferences"

TOKEN = ""
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer "+TOKEN,
    "content-type": "application/json",
    "origin": "https://bsky.app",
    "referer": "https://bsky.app/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

payload = {
    "preferences": [
        {
            "$type": "app.bsky.actor.defs#interestsPref",
            "tags": ["animals", "comics", "dev"]
        },
        {
            "$type": "app.bsky.actor.defs#savedFeedsPrefV2",
            "items": [
                {
                    "id": "",
                    "pinned": True,
                    "type": "feed",
                    "value": ""
                },
                {
                    "id": "",
                    "pinned": True,
                    "type": "timeline",
                    "value": "following"
                }
            ]
        },
        {
            "$type": "app.bsky.actor.defs#bskyAppStatePref"
        },
        {
            "$type": "app.bsky.actor.defs#personalDetailsPref",
            "birthDate": "0001-01-01T00:00:00.000Z"
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print("Birthdate updated successfully!")
else:
    print(f"Failed to update birthdate. Status code: {response.status_code} {response.json()}")
    print(response.text)
