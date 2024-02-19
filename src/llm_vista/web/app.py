import streamlit as st
from llm_vista.services import DefaultVectoStore

dvs = DefaultVectoStore()
st.title(dvs.url)



