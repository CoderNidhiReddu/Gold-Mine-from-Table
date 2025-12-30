import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.markdown("<h1 style = 'color:#00E676;'> Data Visulization</h1>",
            unsafe_allow_html= True)

if "df" not in st.session_state:
    st.write("No Data is Available!!")
    st.stop()

df = st.session_state.df
df_col = st.session_state.df.columns.tolist()
num_col = df.select_dtypes(include = [np.number]).columns

t1, t2 = st.tabs(["Column Statistics", "Missing Values and Duplicates"])

with t1:
    c1, c2 = st.columns(2)
    with c1 : 
        st.header("Column")

        col = st.selectbox("Select Numeric Column : ", num_col)
        st.subheader("Mean")
        st.text(round(df[col].mean(),2))
        st.subheader("Median")
        st.text(round(df[col].median(),2))
        st.subheader("Minimum Value")
        st.text(df[col].min())
        st.subheader("Maximum Value")
        st.text(df[col].max())
        st.subheader("Total Rows")
        st.text(df[col].count())

    with c2:
        st.header("Data Distribution")

        fig,ax= plt.subplots()

        ax.hist(df[col],bins=15)
        ax.set_xlabel(col)
        ax.set_ylabel("Counts")
        st.pyplot(fig)

with t2:
    st.markdown("<h2 style='color:#6B5BFF;'> Missing Values : </h2>",unsafe_allow_html=True)
    c1 , c2 = st.columns(2)
    with c1 :
        total = df.size
        missing = df.isna().sum().sum()
        present = total - missing
        missing_percent = (missing/total)*100

        fig, ax = plt.subplots()

        ax.pie(
        [missing, present],
        colors=[ "#e7dada","#6ef7c4"],
        startangle=90,
        wedgeprops=dict(width=0.25)  # 1 - hole
        )
        ax.legend(labels=["Missing Values", "Present Values"],
                  loc="upper center", bbox_to_anchor=(0.5, 1.15), frameon=False)
        ax.set(aspect="equal")
        st.pyplot(fig)
    with c2:
        st.subheader("Percentage Missing ")
        st.text(f"{round(missing_percent,2)} %")
        st.subheader("Missing Entries")
        st.text(missing)
        st.subheader("Total Entries")
        st.text(total)
    
    st.markdown("<h2 style='color:#6B5BFF;'>Duplicates </h2>", unsafe_allow_html=True)
    c3,c4,c5 = st.columns(3)
    with c3 :
        st.subheader("Total Rows")
        rows = df.shape[0]
        st.text(rows)
    with c4:
        st.subheader("Duplicate Rows")
        duplicate = df.duplicated().sum()
        st.text(duplicate)
    with c5:
        st.subheader("Unique Rows ")
        unique = df.drop_duplicates().shape[0]
        st.text(unique)


# correlation tab can be added  
# st.write("Show Columns with NaN values : ")
# col_nan = df.columns[df.isna().any()].tolist()
