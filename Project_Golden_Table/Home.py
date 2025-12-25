import streamlit as st
import pandas as pd
st.title("Import Bronze Table ")

file = st.file_uploader("Upload File : ", type=["csv"])

if file is None :
    st.error("Upload file first !!")

else:
    if "df" not in st.session_state:
        st.session_state.df = pd.read_csv(file)

    df = st.session_state.df
    df_col = df.columns.tolist()

    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)
    with c1:
        old_col = st.selectbox("Select Column :",df_col)
    with c2:
        new_name = st.text_input("Enter Column new name : ")
        if st.button("Rename Column"):
            if new_name:
                st.session_state.df = df.rename(columns = {old_col : new_name})
                st.success("Column Name successfully Updated")

    with c3:
        col2 = st.selectbox("Select Column :",df_col, key = "col2")
    with c4:
        st.write("")
        st.write("")
        if st.button("Drop Column") :
            st.session_state.df = df.drop(columns=[col2])
        

    st.write("Data Preview ")
    st.dataframe(st.session_state.df)

