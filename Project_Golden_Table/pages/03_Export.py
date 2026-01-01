import streamlit as st
from io import BytesIO

st.markdown("<h1 style = 'color:#ab56e8;' >Download Data : </h1>",
            unsafe_allow_html=True)

if "df" not in st.session_state:
    st.error("No Data available. ")
    st.stop()
df = st.session_state.df

c1, c2 = st.columns(2)
with c1:
    f_type = st.selectbox("Export Format :",["csv","xlsx"])

with c2:
    f_name = st.text_input("File name :",value= f"Output.{f_type}")

if f_type == "csv":
    dt = df.to_csv(index = False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data= dt,
        file_name= f_name,
        mime="text/csv",
        type = "primary"
    ) 

elif f_type == "xlsx" :
    buffer = BytesIO()
    df.to_excel(buffer,index = False, engine = "openpyxl") 
    buffer.seek(0)

    st.download_button(
        label="Download Excel ",
        data= buffer,
        file_name= f_name
    )      
