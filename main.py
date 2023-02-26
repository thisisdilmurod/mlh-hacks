import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
  page_title="Roamstay",
  page_icon=":earth-asia:",
  layout="wide"
)

# Add an image to the sidebar
st.sidebar.image("image.png", use_column_width=True)

def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

# Loading the necessary assets.
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_8Pv1mqEp3b.json")

# Header section.
with st.container():
  st.title("Roamstay")
  st.header("Stay with locals, roam free 🌏")
  st.write(
    """
    A platform that allows travelers to connect with welcoming hosts who are willing to share their homes and experiences.
    We want to create a world where everyone can travel without breaking the bank and enjoy authentic local experiences.
    With Roamstay, you can choose from a variety of lodging options, ranging from a cozy couch to a luxurious villa.
    """
    )
  st.write("[Learn More >](https://google.com/)")

# Mission section.
with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("Our mission 🛫")
    st.write(
      """
      We aim to connect travelers with locals around the world,
      providing a unique and authentic travel experience while promoting cultural exchange and understanding. 
      By offering a platform for couch surfing and more, Roamstay breaks down barriers and create 
      a more open and welcoming global community.\n
      Through our service, we hope to foster meaningful connections between people from different 
      cultures and backgrounds, allowing travelers to gain a deeper appreciation and understanding of the places they visit.
      """
    )
  with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# Contact section.
with st.container():
  st.write("---")
  st.header("Contact us ✉️")
  st.write("##")

  left_column, right_column = st.columns(2)
  with left_column:
    st.text_input("Name")
    st.text_area("Message")
    st.button("Send")
  with right_column:
    st.empty()
