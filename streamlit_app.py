import json 

import requests 
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Title
st.title("A Data Journey to Your :blue[Dream Apartment]")
st.markdown("---")

# Hello and Intro
hello_lottiefile =load_lottiefile("Hello.json")
st_lottie(hello_lottiefile, key="hello")
st.write("intro")
st.markdown("---")

# The beginning of the story
grad_lottiefile =load_lottiefile("Graduation.json")
st_lottie(grad_lottiefile, key="grad")
st.write("begin of the story")
st.markdown("---")

# Interview
grad_lottiefile =load_lottiefile("Interview.json")
st_lottie(grad_lottiefile, key="interview")
st.write("Interview part")
st.markdown("---")