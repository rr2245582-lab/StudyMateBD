import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import threading
from supabase import create_client, Client

# Credentials
SUPABASE_URL = "https://nvwryjgonrznkeptilkx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52d3J5amdvbnR6bmtlcHRpbGt4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI4NTUwODgsImV4cCI6MjEwODQzMTA4OH0.JpgkJlW-nE0HbzwTOQzKGQMOS4_OkATwD3Bh9B-juzo"
GROQ_API_KEY = "YOUR_GROQ_API_KEY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class StudyMateBDGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("StudyMate BD - AI Learning Platform")
        self.root.geometry("450x650")
        self.root.configure(bg="#1E1E2E")

        # User Data
        self.username = "রাফি"
        self.xp = 150
        self.gems = 30
        self.streak = 3

        self.setup_ui()

    def setup_ui(self):
        # Header / Profile Section
        header_frame = tk.Frame(self.root, bg="#2D2D44", pady=10)
        header_frame.pack(fill="x")

        title_lbl = tk.Label(header_frame, text="📚 StudyMate BD", font=("Arial", 18, "bold"), fg="#89B4FA", bg="#2D2D44")
        title_lbl.pack()

        user_lbl = tk.Label(header_frame, text=f"👤 শিক্ষার্থী: {self.username}", font=("Arial", 11), fg="#CDD6F4", bg="#2D2D44")
        user_lbl.pack(pady=2)

        # Gamification Wallet Cards Frame
        card_frame = tk.Frame(self.root, bg="#1E1E2E", pady=10)
        card_frame.pack(fill="x", px=10)

        self.lbl_streak = tk.Label(card_frame, text=f"🔥 {self.streak} Days", font=("Arial", 11, "bold"), fg="#FAB387", bg="#313244", width=11, py=6)
        self.lbl_streak.grid(row=0, column=0, padx=4)

        self.lbl_gems = tk.Label(card_frame, text=f"💎 {self.gems} Gems", font=("Arial", 11, "bold"), fg="#F9E2AF", bg="#313244", width=11, py=6)
        self.lbl_gems.grid(row=0, column=1, padx=4)

        self.lbl_xp = tk.Label(card_frame, text=f"⚡ {self.xp} XP", font=("Arial", 11, "bold"), fg="#A6E3A1", bg="#313244", width=11, py=6)
        self.lbl_xp.grid(row=0, column=2, padx=4)

        # Topic Input Section
        input_frame = tk.LabelFrame(self.root, text=" 🤖 AI Teacher Query ", font=("Arial", 10, "bold"), fg="#CBA6F7", bg="#1E1E2E", bd=1, relief="solid")
        input_frame.pack(fill="x", padx=15, pady=8)

        tk.Label(input_frame, text="বিষয়:", fg="#CDD6F4", bg="#1E1E2E").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_subject = tk.Entry(input_frame, bg="#313244", fg="#FFFFFF", insertbackground="white")
        self.ent_subject.insert(0, "পদার্থবিজ্ঞান")
        self.ent_subject.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(input_frame, text="টপিক:", fg="#CDD6F4", bg="#1E1E2E").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ent_topic = tk.Entry(input_frame, bg="#313244", fg="#FFFFFF", insertbackground="white")
        self.ent_topic.insert(0, "গতির সমীকরণ")
        self.ent_topic.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        input_frame.columnconfigure(1, weight=1)

        # Action Buttons
        btn_ask = tk.Button(input_frame, text="✨ পড়া শুরু করুন (Groq AI)", command=self.ask_ai_thread, font=("Arial", 10, "bold"), bg="#89B4FA", fg="#11111B", activebackground="#B4BEFE")
        btn_ask.grid(row=2, column=0, columnspan=2, pady=8, padx=5, sticky="ew")

        # Response Output Box
        output_frame = tk.Frame(self.root, bg="#1E1E2E")
        output_frame.pack(fill="both", expand=True, padx=15, pady=5)

        tk.Label(output_frame, text="📖 AI শিক্ষকের ক্লাস নোট:", font=("Arial", 10, "bold"), fg="#89B4FA", bg="#1E1E2E").pack(anchor="w")

        self.txt_output = scrolledtext.ScrolledText(output_frame, wrap="word", bg="#181825", fg="#CDD6F4", font=("Arial", 10), insertbackground="white")
        self.txt_output.pack(fill="both", expand=True, pady=5)

        # Bottom Bar Buttons
        bottom_frame = tk.Frame(self.root, bg="#1E1E2E", pady=5)
        bottom_frame.pack(fill="x", padx=15)

        btn_sync = tk.Button(bottom_frame, text="☁️ Cloud Sync", command=self.sync_cloud, bg="#A6E3A1", fg="#11111B", font=("Arial", 9, "bold"))
        btn_sync.pack(side="left", fill="x", expand=True, padx=2)

        btn_leaderboard = tk.Button(bottom_frame, text="🏆 Leaderboard", command=self.show_leaderboard, bg="#F9E2AF", fg="#11111B", font=("Arial", 9, "bold"))
        btn_leaderboard.pack(side="right", fill="x", expand=True, padx=2)

    def update_wallet_ui(self):
        self.lbl_streak.config(text=f"🔥 {self.streak} Days")
        self.lbl_gems.config(text=f"💎 {self.gems} Gems")
        self.lbl_xp.config(text=f"⚡ {self.xp} XP")

    def ask_ai_thread(self):
        threading.Thread(target=self.ask_ai, daemon=True).start()

    def ask_ai(self):
        subject = self.ent_subject.get().strip()
        topic = self.ent_topic.get().strip()

        if not subject or not topic:
            messagebox.showwarning("সতর্কতা", "দয়া করে বিষয় এবং টপিক উভয়ই পূরণ করুন।")
            return

        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert(tk.END, f"🤖 Groq AI [{subject}] এর [{topic}] নিয়ে পাঠ তৈরি করছেন... অনুগ্রহ করে অপেক্ষা করুন।\n\n")

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        prompt = f"বাংলাদেশের NCTB কারিকুলাম অনুযায়ী {subject} বিষয়ের '{topic}' টপিকটি সহজ বাংলায় একজন শিক্ষকের মতো বুঝিয়ে দিন এবং শেষে একটি প্রশ্ন দিন।"

        data = {
            "model": "qwen/qwen3.8-27b",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }

        try:
            res = requests.post(url, headers=headers, json=data)
            if res.status_code == 200:
                answer = res.json()['choices'][0]['message']['content']
                self.txt_output.delete("1.0", tk.END)
                self.txt_output.insert(tk.END, answer)

                # Reward Points
                self.xp += 50
                self.gems += 10
                self.update_wallet_ui()
                messagebox.showinfo("🎉 অভিনন্দন!", "পাঠ সফলভাবে সম্পন্ন হয়েছে!\n+50 XP এবং +10 Gems আপনার ওয়ালেটে যোগ করা হয়েছে।")
            else:
                self.txt_output.insert(tk.END, f"\n❌ এআই এরর ({res.status_code}): {res.text}")
        except Exception as e:
            self.txt_output.insert(tk.END, f"\n❌ কানেকশন এরর: {str(e)}")

    def sync_cloud(self):
        try:
            data = {"username": self.username, "xp": self.xp, "gems": self.gems, "streak": self.streak}
            supabase.table("global_leaderboard").upsert(data, on_conflict="username").execute()
            messagebox.showinfo("☁️ Cloud Sync", "আপনার স্কোর ক্লাউড ডেটাবেসে সফলভাবে সেভ হয়েছে!")
        except Exception as e:
            messagebox.showerror("❌ এরর", f"সিঙ্ক ব্যর্থ হয়েছে: {e}")

    def show_leaderboard(self):
        try:
            res = supabase.table("global_leaderboard").select("*").order("xp", desc=True).limit(5).execute()
            data = res.data
            msg = "🏆 --- Live Leaderboard ---\n\n"
            if not data:
                msg += "কোনো ডেটা পাওয়া যায়নি।"
            else:
                for idx, row in enumerate(data, 1):
                    msg += f"{idx}. {row.get('username')} — {row.get('xp')} XP\n"
            messagebox.showinfo("Global Leaderboard", msg)
        except Exception as e:
            messagebox.showerror("❌ এরর", f"লিডারবোর্ড লোড করা যায়নি: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyMateBDGUI(root)
    root.mainloop()
