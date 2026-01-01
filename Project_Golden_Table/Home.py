import streamlit as st
import pandas as pd

st.title("Uploading Page")

dummy_data = pd.DataFrame([
    ["Ivysaur", "Grass", "Poison", 405, 60, 62, 63, 80, 80, 60, 1],
    ["Venusaur", "Grass", "Poison", 525, 80, 82, 83, 100, 100, 80, 1],
    ["Venusaur Mega", "Grass", "Poison", 625, 80, 100, 123, 122, 120, 80, 1],
    ["Charmander", "Fire", None, 309, 39, 52, 43, 60, 50, 65, 1],
    ["Charmeleon", "Fire", None, 405, 58, 64, 58, 80, 65, 80, 1],
    ["Charizard", "Fire", "Flying", 534, 78, 84, 78, 109, 85, 100, 1],
    ["Charizard Mega X", "Fire", "Dragon", 634, 78, 130, 111, 130, 85, 100, 1],
    ["Charizard Mega Y", "Fire", "Flying", 634, 78, 104, 78, 159, 115, 100, 1],
    ["Squirtle", "Water", None, 314, 44, 48, 65, 50, 64, 43, 1],
    ["Blastoise Mega", "Water", None, 630, 79, 103, 120, 135, 115, 78, 1]],
columns = [
    "Name", "Type 1", "Type 2", "Total", "HP", "Attack",
    "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation"]
)

if "df" not in st.session_state:
    st.session_state.df = dummy_data

if "uploaded_file" not in st.session_state :
    st.session_state.uploaded_file = None

uploaded_file = st.file_uploader("Upload File : ", type = ["csv", "xlsx"])

if uploaded_file is not None:
    # st.balloons()
    if uploaded_file.name.endswith(".csv"):
        st.session_state.df = pd.read_csv(uploaded_file)
    else:
        st.session_state.df = pd.read_excel(uploaded_file)


st.subheader("Dummy Data ")
st.dataframe(st.session_state.df, width = "stretch")
