import streamlit as st
import subprocess
import sys
import os

API_KEY = "qggkwn4svoocy13z"
API_SECRET = "hd97qxe2h5lp07f4gpjnp54iyh2ncyid"

st.title("Zerodha Access Token Generator")

st.markdown("### Web-native version (no console `input()`)")

st.write("1. Click the button to get the login URL here itself.")
if st.button("Get login URL"):
    from kiteconnect import KiteConnect  # recommended
    kite = KiteConnect(api_key=API_KEY)
    login_url = kite.login_url()
    st.success("Login URL generated:")
    st.write(login_url)
    st.write("After logging in, copy the `request_token` parameter from the redirected URL.")

request_token = st.text_input("Paste request_token here:")

if st.button("Generate access token"):
    if not request_token:
        st.warning("Please enter a request_token first.")
    else:
        from kiteconnect import KiteConnect
        kite = KiteConnect(api_key=API_KEY)
        try:
            data = kite.generate_session(request_token, api_secret=API_SECRET)
            access_token = data["access_token"]
            with open("access_token.txt", "w") as f:
                f.write(access_token)
            st.success("Access Token generated and saved to access_token.txt")
            st.write(f"Token: {access_token}")
        except Exception as e:
            st.error(f"Error generating session: {e}")
