import streamlit as st
from pathlib import Path
from PIL import Image
# PAth settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = current_dir/"assets"/"profile-pic.png"
project1 = current_dir/"assets"/"exemple-2.png"
project2 = current_dir/"assets"/"exemple-3.png"
project3 = current_dir/"assets"/"exemple4.png"
project4 = current_dir/"assets"/"project4.png"


# generale settings#
PAGE_TITLE = "Portfolio | Tarik KHALFI"
NAME = "Tarik KHALFI"
DESCRIPTION = f"Hello i'm {NAME} a Future Web Developer From Agadir. I'am a creative developper based in Morocco, and i'm very passionate and dedicated to my work. "
DESCRIPTION2 = "my skillset includes programming with JavaScript, ReactJS, and Python there are some project that i've worked before "
EMAIL = "khtarek07@gmail.com"


profile_pic = Image.open(profile_pic)
project1 = Image.open(project1)
project2 = Image.open(project2)
project3 = Image.open(project3)
project4 = Image.open(project4)
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(EMAIL)
st.subheader("My skills 🤹‍♂️:")
st.write(DESCRIPTION2)
st.subheader("MY PROJECTS 🚀:")
st.image(project1)
st.markdown("<h3 style='text-align: center;'>Covid-19 Tracker</h3>",
            unsafe_allow_html=True)
st.image(project2)
st.markdown("<h3 style='text-align: center;'>Tesla Website Clone</h3>",
            unsafe_allow_html=True)
st.image(project3)
st.markdown("<h3 style='text-align: center;'>Expense Tracker</h3>",
            unsafe_allow_html=True)
st.image(project4)
st.markdown("<h3 style='text-align: center;'>Youtube Website Clone</h3>",
            unsafe_allow_html=True)
