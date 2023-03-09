# Libraries
import openai, streamlit as st, random, warnings
# Necessary
st.write(
    "Has environment variables been set:",
    os.environ["secrets"] == st.secrets["secrets"],
)
