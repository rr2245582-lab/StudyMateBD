import requests
from supabase import create_client, Client

SUPABASE_URL = "https://nvwryjgonrznkeptilkx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52d3J5amdvbnR6bmtlcHRpbGt4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI4NTUwODgsImV4cCI6MjEwODQzMTA4OH0.JpgkJlW-nE0HbzwTOQzKGQMOS4_OkATwD3Bh9B-juzo"
GROQ_API_KEY = "YOUR_GROQ_API_KEY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class StudyMateCloudApp:
    def __init__(self, username="রফিক"):
        self.username = username
        self.xp = 150
        self.gems = 30
        self.streak = 3

    def show_dashboard(self):
        print("\n" + "="*45)
        print(f"   📱 StudyMate BD [Cloud Synced] ")
        print("="*45)
        print(f"👤 শিক্ষার্থী: {self.username}")
        print(f"🔥 Daily Streak: {self.streak} দিন")
        print(f"💎 Gems Counter: {self.gems} Gems")
        print(f"⚡ Total XP: {self.xp} XP")
        print("="*45)
        print(" [1] 🤖 Groq AI শিক্ষকের সাথে পাঠ গ্রহণ ও রিওয়ার্ড")
        print(" [2] 🏆 Supabase লাইভ লিডারবোর্ড দেখুন")
        print(" [3] ☁️ ক্লাউডে প্রোফাইল সিঙ্ক করুন")
        print(" [0] ❌ প্রস্থান")
        print("="*45)

    def fetch_leaderboard(self):
        print("\n🔄 Supabase থেকে লাইভ লিডারবোর্ড লোড হচ্ছে...")
        try:
            response = supabase.table("global_leaderboard").select("*").order("xp", desc=True).limit(5).execute()
            data = response.data
            print("\n🏆 --- Global Leaderboard (Live) ---")
            if not data:
                print(" (এই মুহূর্তে লিডারবোর্ডে কোনো ডেটা নেই। অপশন ৩ চেপে আপনার ডেটা সিঙ্ক করুন!)")
            else:
                for idx, row in enumerate(data, 1):
                    print(f" {idx}. {row.get('username', 'Unknown')} — {row.get('xp', 0)} XP")
            print("-" * 35)
        except Exception as e:
            print(f"❌ লিডারবোর্ড ফেচ করতে সমস্যা: {e}")

    def sync_to_cloud(self):
        print(f"\n☁️ {self.username}-এর প্রোফাইল ক্লাউডে সেভ করা হচ্ছে...")
        try:
            # লিডারবোর্ড টেবিলে আপসর্ট (ইনসার্ট বা আপডেট) করা
            data = {
                "username": self.username,
                "xp": self.xp,
                "gems": self.gems,
                "streak": self.streak
            }
            supabase.table("global_leaderboard").upsert(data, on_conflict="username").execute()
            print("✅ ক্লাউড সিঙ্ক সফল! আপনার স্কোর এখন অনলাইনে সংরক্ষিত।\n")
        except Exception as e:
            print(f"❌ সিঙ্ক এরর: {e}")

    def run_ai_teacher(self):
        print("\n--- 🤖 AI Teacher Module ---")
        subject = input("বিষয় লিখুন (যেমন: পদার্থবিজ্ঞান, গণিত): ")
        topic = input("টপিক লিখুন (যেমন: নিউটনের সূত্র, বীজগণিত): ")
        
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        prompt = f"বাংলাদেশের NCTB কারিকুলাম অনুযায়ী {subject} বিষয়ের '{topic}' টপিকটি সহজ বাংলায় একজন শিক্ষকের মতো বুঝিয়ে দিন।"
        
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
                # অটো ক্লাউড সিঙ্ক
                self.sync_to_cloud()
            else:
                print(f"❌ এআই রেসপন্স এরর: {res.status_code}")
        except Exception as e:
            print(f"❌ কানেকশন এরর: {e}")

if __name__ == "__main__":
    app = StudyMateCloudApp(username="রাফি_স্টুডেন্ট")
    while True:
        app.show_dashboard()
        choice = input("আপনার পছন্দ (0-3): ")
        if choice == "1":
            app.run_ai_teacher()
        elif choice == "2":
            app.fetch_leaderboard()
        elif choice == "3":
            app.sync_to_cloud()
        elif choice == "0":
            print("\n👋 StudyMate BD বন্ধ করা হলো। ভালো থাকবেন!\n")
            break
        else:
            print("\n❌ ভুল ইনপুট! সঠিক অপশন দিন।\n")
