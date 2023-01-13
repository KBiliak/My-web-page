import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/my_photo.jpg", width=400)

with col2:
    st.title("Kateryna Biliak")
    content = """
    Hello, my name is Kateryna and I am a junior Python Developer.
I have an experience as a QA Engineer for one year.
Now I am going to face with new challenges like a development of interesting things. 
I have completed a couple of courses to become a competitive employee 
and ready to do all my best to be a valuable team member. 
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python.
Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")



with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://pythonhow.com)")
