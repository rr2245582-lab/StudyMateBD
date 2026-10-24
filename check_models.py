import requests

GROQ_API_KEY = "YOUR_GROQ_API_KEY"

url = "https://api.groq.com/openai/v1/models"
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        models = response.json().get('data', [])
        print("\n✅ আপনার API Key দিয়ে যে মডেলগুলো বর্তমানে সচল রয়েছে:\n")
        for m in models:
            print(f" • {m['id']}")
        print("\n")
    else:
        print(f"❌ এরর ({response.status_code}): {response.text}")
except Exception as e:
        print(f"❌ এরর: {str(e)}")
