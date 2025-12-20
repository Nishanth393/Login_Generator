# token_generator.py
from kiteconnect import KiteConnect

API_KEY = "nxxjc8a0ddtaisg0"
API_SECRET = "lftkesvi6loaix4qvryew29sbnk0dfyd"

def get_daily_access_token():
    kite = KiteConnect(api_key=API_KEY)

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
        data = kite.generate_session(request_token, api_secret=API_SECRET)
        access_token = data["access_token"]
        # with open("access_token.txt", "w") as f:
        #  f.write(access_token)
        print("✅ SUCCESS! Access Token saved to 'access_token.txt'")
        print(f"Token: {access_token}... (hidden)")
    except Exception as e:
        print("❌ Error generating session:", e)

if __name__ == "__main__":
    get_daily_access_token()
