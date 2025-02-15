import requests
import pandas as pd
import streamlit as st

def fetch_airdrop_data(wallet_address):
    url = f"https://api.octavionotpunk.com/airdrop?address={wallet_address}"
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
        
        if data:
            formatted_data = []
            for key, value in data.items():
                formatted_data.append({
                    "Project": key,
                    "Amount": value["amount"],
                    "Link": f'[Claim Here]({value["link"]})'
                })
            
            df = pd.DataFrame(formatted_data)
            st.write(df.to_html(escape=False), unsafe_allow_html=True)
        else:
            st.error("Failed to fetch data or invalid address.")

if __name__ == "__main__":
    main()
