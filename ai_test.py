import requests

GROQ_API_KEY = "YOUR_GROQ_API_KEY"

def ask_study_ai(question):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # বর্তমান সক্রিয় Groq মডেল ব্যবহার করা হচ্ছে
    payload = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {
                "role": "system",
                "content": "তুমি StudyMate BD-এর AI শিক্ষক। বাংলাদেশের NCTB কারিকুলাম অনুযায়ী ১ম-১০ম শ্রেণির শিক্ষার্থীদের সহজ ও সাবলীল বাংলায় ধাপে ধাপে উত্তর দেবে।"
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Connection Error: {str(e)}"

if __name__ == "__main__":
    prompt = "সালোকসংশ্লেষণ বলতে কী বোঝো? সহজ ভাষায় ৩ লাইনে বুঝিয়ে দাও।"
    print("\n🤖 Study Helper AI সংযোগ করা হচ্ছে...\n")
    answer = ask_study_ai(prompt)
    print("--- 📚 AI শিক্ষকের উত্তর ---")
    print(answer)
    print("\n----------------------------\n")
