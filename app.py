import streamlit as st
from kiteconnect import KiteConnect

st.title("Zerodha Access Token Generator")

# --------- DYNAMIC CREDS ----------
api_key = st.text_input("API Key", value="", type="default")
api_secret = st.text_input("API Secret", value="", type="password")

st.markdown("### Web-native version (no console `input()`)")
st.write("1. Click the button to get the login URL here itself.")

# --------- LOGIN URL BUTTON ----------
if st.button("Get login URL"):
    if not api_key:
        st.warning("Please enter API Key first.")
    else:
        try:
            kite = KiteConnect(api_key=api_key)
            login_url = kite.login_url()
            st.success("Login URL generated:")
            st.write(login_url)
            st.write("After logging in, copy the `request_token` parameter from the redirected URL.")
        except Exception as e:
            st.error(f"Error generating login URL: {e}")

# --------- REQUEST TOKEN INPUT ----------
request_token = st.text_input("Paste request_token here:")

# --------- GENERATE ACCESS TOKEN BUTTON ----------
if st.button("Generate access token"):
    if not api_key or not api_secret:
        st.warning("Please enter both API Key and API Secret.")
    elif not request_token:
        st.warning("Please enter a request_token first.")
    else:
        try:
            kite = KiteConnect(api_key=api_key)
            data = kite.generate_session(request_token, api_secret=api_secret)
            access_token = data["access_token"]

            # save to file (same behavior as before, just dynamic creds)
            with open("access_token.txt", "w") as f:
                f.write(access_token)

            st.success("Access Token generated and saved to access_token.txt")
            st.write(f"Token: {access_token}")
        except Exception as e:
            st.error(f"Error generating session: {e}")
