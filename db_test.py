from supabase import create_client, Client

SUPABASE_URL = "https://nvwryjgonrznkeptilkx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52d3J5amdvbnJ6bmtlcHRpbGt4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI4NTUwODgsImV4cCI6MjEwODQzMTA4OH0.JpgkJlW-nE0HbzwTOQzKGQMOS4_OkATwD3Bh9B-juzo"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def test_connection():
    try:
        response = supabase.table("global_leaderboard").select("*").execute()
        print("\n✅ Supabase Connection Successful!")
        print(f"Total Leaderboard Entries: {len(response.data)}\n")
    except Exception as e:
        print(f"\n❌ Connection Failed: {str(e)}\n")

if __name__ == "__main__":
    test_connection()
