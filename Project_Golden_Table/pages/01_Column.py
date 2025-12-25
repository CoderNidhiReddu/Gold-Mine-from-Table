import streamlit as st
import io

st.title("Data Analysis")

st.set_page_config(page_title = "Handling missing values : ")

if "df" not in st.session_state:
    st.error("No Data available. ")
    st.stop()
df = st.session_state.df

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()

st.summary(s)

st.write("How you want to handle missing values ? ")
c1,c2 = st.columns(2)

with c1:
    f1 = st.radio("Type :" , ["Fill with mean ","Fill with median ","Drop Rows", "Fill with"])

fill_with = None
if f1 == "Fill with":
    num = st.number_input("",value=0)


st.button("Apply Changes ",type="primary")


# handling missing values
# show graphs between x and y
# download file format