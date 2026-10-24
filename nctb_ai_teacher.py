import os
from supabase import create_client, Client

SUPABASE_URL = "https://nvwryjgonrznkeptilkx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52d3J5amdvbnJ6bmtlcHRpbGt4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI4NTUwODgsImV4cCI6MjEwODQzMTA4OH0.JpgkJlW-nE0HbzwTOQzKGQMOS4_OkATwD3Bh9B-juzo"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def ask_ai_teacher(subject, topic):
    print(f"\n🤖 Groq AI শিক্ষক [{subject}] বিষয়ের [{topic}] টপিক তৈরি করছেন...")
    # এখানে আমরা Groq AI API কানেক্ট করব
    print("📖 NCTB কারিকুলাম অনুযায়ী কনটেন্ট প্রস্তুত করা হচ্ছে...")
    print("✨ সফল! শিক্ষার্থী এই পাঠ শেষ করলে পাবেন: +50 XP এবং +10 Gems\n")

if __name__ == "__main__":
    ask_ai_teacher("পদার্থবিজ্ঞান", "গতির সমীকরণ (Equations of Motion)")
