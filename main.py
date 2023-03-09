import openai 
import streamlit as st 
import os

st.write(
    "Has environment variables been set:",
    os.environ["secrets"] == st.secrets["secrets"],
)
