import streamlit as st
import pandas as pd
import requests
st.title("AutoEit  Monitoring System")
uploaded_file=st.file_uploader("Upload csv file",type=["csv"])
if uploaded_file:
    
    if st.button("Score via API"):
        
        files = {
            "file": uploaded_file.getvalue()
        }

        response = requests.post(
            "http://127.0.0.1:8000/score",
            files=files
        )

        data = response.json()
        df = pd.DataFrame(data)

        st.dataframe(df)
