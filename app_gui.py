import requests
from supabase import create_client, Client

SUPABASE_URL = "https://nvwryjgonrznkeptilkx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52d3J5amdvbnR6bmtlcHRpbGt4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI4NTUwODgsImV4cCI6MjEwODQzMTA4OH0.JpgkJlW-nE0HbzwTOQzKGQMOS4_OkATwD3Bh9B-juzo"
GROQ_API_KEY = "YOUR_GROQ_API_KEY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class StudyMateBDApp:
    def __init__(self, username="শিক্ষার্থী"):
        self.username = username
        self.xp = 150
        self.gems = 30
        self.streak = 3

    def show_dashboard(self):
        print("\n" + "="*45)
        print(f"   📱 StudyMate BD - Dashboard")
        print("="*45)
        print(f"👤 শিক্ষার্থী: {self.username}")
        print(f"🔥 Daily Streak: {self.streak} দিন")
        print(f"💎 Gems Counter: {self.gems} Gems")
        print(f"⚡ Total XP: {self.xp} XP")
        print("="*45)
        print(" [1] 🤖 Groq AI শিক্ষকের সাথে পাঠ গ্রহণ")
        print(" [2] 🏆 Global Leaderboard প্রদর্শন")
        print(" [3] 🎒 Wallet & Rewards Check")
        print(" [0] ❌ Exit App")
        print("="*45)

    def run_ai_teacher(self):
        print("\n--- 🤖 AI Teacher Module ---")
        subject = input("বিষয় লিখুন (যেমন: পদার্থবিজ্ঞান, গণিত, রসায়ন): ")
        topic = input("টপিক লিখুন (যেমন: বল, জারণ-বিজারণ, সেট): ")
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        prompt = f"বাংলাদেশের NCTB কারিকুলাম অনুযায়ী {subject} বিষয়ের '{topic}' টপিকটি সহজ বাংলায় একজন শিক্ষকের মতো বুঝিয়ে দিন এবং সাথে একটি ছোট্ট প্রশ্ন দিন।"
        
        data = {
            "model": "qwen/qwen3.8-27b",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        
        try:
            res = requests.post(url, headers=headers, json=data)
            if res.status_code == 200:
                answer = res.json()['choices'][0]['message']['content']
                print("\n" + "-"*40)
                print(answer)
                print("-"*40)
                self.xp += 50
                self.gems += 10
                print(f"🎉 রিওয়ার্ড অর্জিত! +50 XP | +10 Gems")
                print(f"বর্তমান ব্যালেন্স: {self.xp} XP, {self.gems} Gems")
            else:
                print(f"❌ এরর: {res.status_code}")
        except Exception as e:
            print(f"❌ এরর: {e}")

if __name__ == "__main__":
    app = StudyMateBDApp(username="রাফি")
    while True:
        app.show_dashboard()
        choice = input("আপনার পছন্দ নির্বাচন করুন (0-3): ")
        if choice == "1":
            app.run_ai_teacher()
        elif choice == "2":
            print("\n🏆 Leaderboard Top 3: 1. রাফি (150 XP), 2. সাকিব (120 XP), 3. তামিম (100 XP)\n")
        elif choice == "3":
            print(f"\n🎒 Wallet Status: {app.gems} Gems, {app.xp} XP\n")
        elif choice == "0":
            print("\n👋 StudyMate BD ব্যবহার করার জন্য ধন্যবাদ!\n")
            break
        else:
            print("\n❌ ভুল ইনপুট! আবার চেষ্টা করুন।\n")
