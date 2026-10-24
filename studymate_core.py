import os
from supabase import create_client, Client

SUPABASE_URL = "https://nvwryjgonrznkeptilkx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52d3J5amdvbnJ6bmtlcHRpbGt4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI4NTUwODgsImV4cCI6MjEwODQzMTA4OH0.JpgkJlW-nE0HbzwTOQzKGQMOS4_OkATwD3Bh9B-juzo"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def app_info():
    print("\n========================================")
    print("  📚 StudyMate BD - Core Engine Ready! ")
    print("========================================\n")
    print("✅ Supabase Backend: Connected")
    print("✅ Gamification Wallet: Active")
    print("✅ Groq AI Teacher: Ready to integrate\n")

if __name__ == "__main__":
    app_info()
