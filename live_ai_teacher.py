import requests

GROQ_API_KEY = "YOUR_GROQ_API_KEY"

def ask_groq_ai(subject, topic):
    print(f"\n🤖 Groq AI শিক্ষক [{subject}] বিষয়ের [{topic}] নিয়ে NCTB কারিকুলাম অনুযায়ী পড়া তৈরি করছেন...")
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "StudyMateBD-App/1.0"
    }
    
    prompt = f"বাংলাদেশের NCTB কারিকুলাম অনুযায়ী {subject} বিষয়ের '{topic}' টপিকটি সহজ বাংলায় একজন শিক্ষকের মতো বুঝিয়ে দিন এবং সাথে একটি ছোট্ট প্রশ্ন দিন। উত্তর সুন্দরভাবে ফরম্যাট করুন।"
    
    data = {
        "model": "qwen/qwen3.8-27b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            res_body = response.json()
            ai_reply = res_body['choices'][0]['message']['content']
            print("\n----------------------------------------")
            print(ai_reply)
            print("\n----------------------------------------")
            print("✨ সফল! শিক্ষার্থী এই পাঠ শেষ করলে পাবে: +50 XP এবং +10 Gems\n")
        else:
            print(f"❌ এআই রেসপন্স এরর ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"❌ এআই কানেকশন এরর: {str(e)}")

if __name__ == "__main__":
    ask_groq_ai("পদার্থবিজ্ঞান", "গতির সমীকরণ (Equations of Motion)")
