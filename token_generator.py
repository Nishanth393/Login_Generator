# token_generator.py
from kiteconnect import KiteConnect

def get_daily_access_token(api_key: str, api_secret: str):
    kite = KiteConnect(api_key=api_key)

    print("--------------------------------------------------")
    print("🚀 GENERATING ZERODHA ACCESS TOKEN")
    print("--------------------------------------------------")

    login_url = kite.login_url()
    print("1. Click this link to login:")
    print(login_url)
    print("\n(After logging in, you will be redirected to a URL that looks like:")
    print("http://127.0.0.1/?request_token=xyz...)")
    print("--------------------------------------------------")

    request_token = input("2. Paste the 'request_token' from the URL bar here: ")

    try:
        data = kite.generate_session(request_token, api_secret=api_secret)
        access_token = data["access_token"]
        print("✅ SUCCESS! Access Token generated")
        print(f"Token: {access_token}")
    except Exception as e:
        print("❌ Error generating session:", e)

if __name__ == "__main__":
    # optional: manual test values here, or keep empty
    API_KEY = "REPLACE_ME"
    API_SECRET = "REPLACE_ME"
    get_daily_access_token(API_KEY, API_SECRET)
