import json 

import requests 
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_navigation_bar import st_navbar

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    

# Title
st.title("Riyadh, and :blue[The Hunt for a Home!]")
st.markdown("---")

# Grad part 
st.subheader("CONGRATULATIONS!")
st.subheader("For graduating from the top academy for Data Science!!")
grad_lottiefile =load_lottiefile("Graduation.json")
st_lottie(grad_lottiefile, key="grad")


st.markdown("##### **Pretty nice getting all those job offers ha? Better go back and thank the academy, especially your instructors! But wait… all offers are in Riyadh? Interviewers are asking if you live in Riyadh?**")


# The beginning of the story
# grad_lottiefile =load_lottiefile("Graduation.json")
# st_lottie(grad_lottiefile, key="grad")
# st.write("begin of the story")
# st.markdown("---")

# Interview
# grad_lottiefile =load_lottiefile("Interview.json")
# st_lottie(grad_lottiefile, key="interview")
# st.write("Interview part")
# st.markdown("---")

st.markdown("###### Oh, now it’s getting real..")
st.markdown("###### Yeah… Yeah we know… it's time to seriously consider moving, and finding a place to stay in Riyadh is a bit annoying (might be an understatement) and it doesn’t help that whenever you go online to find something you just get bombarded by so many options, or none! ")
st.markdown("###### And you’re probably thinking “Wouldn’t it be nice if someone just picked something for me? Or at least help me decide? I need an expert…” ")
st.markdown("###### Well look no more! We did the search for you!")
st.markdown("###### See Riyadh, just like any city, is split into multiple regions:")
st.markdown('Note: chart for all regions')

st.markdown("###### And although accommodations are found in all regions, prices vary.")
st.markdown("###### What affects the price is how far the place is from the center, and whether or not it's in a 'fancy' new neighborhood.")
st.markdown("###### So, after you see the regions")

option = st.selectbox(
   "**Which region do you want to move to?**",
    ("Center", "West", "East", "North", "South"),
)
st.markdown("Note: prices for each region")