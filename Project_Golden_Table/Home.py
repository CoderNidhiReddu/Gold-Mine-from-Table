import streamlit as st
import pandas as pd

st.title("Uploading Page")

if "uploaded_file" not in st.session_state :
    st.session_state.uploaded_file = None

uploaded_file = st.file_uploader("Upload File : ", type = ["csv", "xlsx"])

if uploaded_file is None:
    st.error("Upload a file first !!")
    st.stop()

else:
    # st.balloons()
    if "df" not in st.session_state:
        if uploaded_file.name.endswith(".csv"):
            st.session_state.df = pd.read_csv(uploaded_file)
        else:
            st.session_state.df = pd.read_excel(uploaded_file)

    

    st.dataframe(st.session_state.df, width = "stretch")
