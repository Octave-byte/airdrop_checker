import requests
import pandas as pd
import streamlit as st

def fetch_airdrop_data(wallet_address):
    url = f"https://airdropcheck-octavionotpunk.pythonanywhere.com/get_alloc?wallet_address={wallet_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title("Airdrop Eligibility Checker")
    wallet_address = st.text_input("Enter Wallet Address:")
    
    if st.button("Verify"):
        data = fetch_airdrop_data(wallet_address)
        
        if data and data.get("status") == "success":
            allocations = data.get("allocation", [])
            if allocations:
                df = pd.DataFrame(allocations)
                df.rename(columns={"claimableTokens": "Amount", "project": "Project"}, inplace=True)
                st.write(df)
            else:
                st.warning("No airdrops available for this address.")
        else:
            st.error("Failed to fetch data or invalid address.")

if __name__ == "__main__":
    main()

