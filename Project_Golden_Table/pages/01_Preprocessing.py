import streamlit as st
import io

st.markdown("<h1 style = 'color:#2196F0;'> Data Preprocessing</h1>",
            unsafe_allow_html= True)

st.set_page_config(page_title = "Handling missing values : ")

if "df" not in st.session_state:
    st.error("No Data available. ")
    st.stop()

df = st.session_state.df
df_col = st.session_state.df.columns.tolist()

@st.fragment
def column_op():

    c1,c2,c3 = st.columns(3)    
    c4,c5 = st.columns(2)
    with c1:
        old_col = st.selectbox("Select Column", df_col, key="c1")
    with c2:
        new_name = st.text_input("Enter the New Name : ")
    with c3 : 
        st.write("")
        st.write("")
        if st.button("Rename ", type='primary', width= "stretch"):
            if new_name:
                st.session_state.df.rename(columns={old_col : new_name}, inplace = True)
                st.rerun()

    with c4:
        col = st.selectbox("Select Column", df_col, key="c2")
    with c5:
        st.write("")
        st.write("")
        if st.button("Drop Column", type="primary", width="stretch"):
            st.session_state.df.drop(columns=[col], inplace= True)
            st.rerun()

column_op()
# st.dataframe(st.session_state.df, width = "stretch")

st.markdown(
    "<h2 style='color:#2196F3;'>How you want to handle missing values ?</h2>",
    unsafe_allow_html=True
)

c1,c2 = st.columns(2)

with c1:
    f1 = st.radio("Type :" , ["Fill with mean ","Fill with median ","Drop Rows", "Fill with"])

fill_num = None
if f1 == "Fill with":
    fill_num = st.number_input("",value=0)


if st.button("Apply Changes ",type="primary"):
    if f1 == "Fill with mean" :
        # error
        numeric_mean = df.select_dtypes(include = ["number"]).mean()
        df = df.fillna(numeric_mean)
    elif f1 == "Fill with median" :
        # error
        num_median = df.select_dtypes(include = ["number"]).median()
        df.fillna(num_median, inplace = True)
    elif f1 == "Drop Rows" :
        df = df.dropna()
    else:
        df = df.fillna(fill_num)


st.markdown("<h2 style = 'color:#2196F3;'> Data Preview </h2>",
            unsafe_allow_html= True)
st.dataframe(df)


# show graphs between x and y
# column wise mean, mode, median, sum, avg, ...

