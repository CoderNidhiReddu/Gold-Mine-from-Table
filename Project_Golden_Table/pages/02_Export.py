import streamlit as st
from io import BytesIO

st.title("Download Data : ")

if "df" not in st.session_state:
    st.error("No Data available. ")
    st.stop()
df = st.session_state.df

c1, c2 = st.columns(2)
with c1:
    f_name = st.text_input("File name :")

with c2:
    f_type = st.selectbox("Export Format :",["CSV","EXCEL","TEXT"])

if f_type == "CSV":
    dt = df.to_csv(index = False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data= dt,
        file_name= f_name,
        mime="text/csv"
    ) 

elif f_type == "EXCEL" :
    buffer = BytesIO()
    df.to_excel(buffer,index = False, engine = "openpyxl") 
    buffer.seek(0)

    st.download_button(
        label="Download Excel ",
        data= buffer,
        file_name= f_name
    )      

