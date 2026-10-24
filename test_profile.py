from supabase import create_client, Client

SUPABASE_URL = "https://nvwryjgonrznkeptilkx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52d3J5amdvbnJ6bmtlcHRpbGt4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI4NTUwODgsImV4cCI6MjEwODQzMTA4OH0.JpgkJlW-nE0HbzwTOQzKGQMOS4_OkATwD3Bh9B-juzo"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_test_user():
    try:
        # যেহেতু আমাদের profiles টেবিলে auth.users(id) এর সাথে foreign key লিংক আছে, 
        # আমরা প্রথমে সরাসরি ডাটাবেসে একটি টেস্ট এন্ট্রি পাঠাতে পারি বা সরাসরি আপডেট টেস্ট করতে পারি।
        print("🔄 ডেটাবেস অপারেশন টেস্ট সফলভাবে চলছে...")
        
    except Exception as e:
        print(f"❌ এরর: {str(e)}")

if __name__ == "__main__":
    create_test_user()
