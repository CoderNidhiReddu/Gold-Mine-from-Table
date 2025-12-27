import streamlit as st
import io

st.title("Data Analysis")

st.set_page_config(page_title = "Handling missing values : ")

if "df" not in st.session_state:
    st.error("No Data available. ")
    st.stop()
df = st.session_state.df

# st.write("Show Columns with NaN values : ")
# col_nan = df.columns[df.isna().any()].tolist()
# t1,t2,t3,t4 = st.tabs(["Column Statistics","Duplicates","Missing Values"])



st.write("How you want to handle missing values ? ")
c1,c2 = st.columns(2)

with c1:
    f1 = st.radio("Type :" , ["Fill with mean ","Fill with median ","Drop Rows", "Fill with"])

fill_num = None
if f1 == "Fill with":
    fill_num = st.number_input("",value=0)


if st.button("Apply Changes ",type="primary"):
    if f1 == "Fill with mean" :
        numeric_mean = df.select_dtypes(include = ["number"]).mean()
        df = df.fillna(numeric_mean)
    elif f1 == "Fill with median" :
        num_median = df.select_dtypes(include = ["number"]).median()
        df.fillna(num_median, inplace = True)
    elif f1 == "Drop Rows" :
        df = df.dropna()
    else:
        df = df.fillna(fill_num)


st.write("Data Preview ")
st.dataframe(df)


# show graphs between x and y
# download file format
        
