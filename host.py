import streamlit as st
import pandas as pd
import folium
import requests
from streamlit_folium import folium_static
from streamlit_lottie import st_lottie

st.title("Become a host")

def save_contact_info(name, phone, additional_info):
    # Save the contact information to a file or database
    with open("contacts.txt", "a") as f:
        f.write("{}\t{}\t{}\t{}\n".format(name, phone, additional_info))

def display_contact_info(name, phone, additional_info):
    # Display the contact information on the page
    st.write("Name:", name)
    st.write("Phone:", phone)
    st.write("Additional Information:", additional_info)

def main():
    st.subheader("Information")
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    additional_info = st.text_area("Additional Information")
    if st.button("Submit"):
        st.write("---")
        save_contact_info(name, phone, additional_info)
        display_contact_info(name, phone, additional_info)

def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

# Loading the necessary assets.
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_wog0txcc.json")

with st.container():
  left_column, right_column = st.columns(2)
  with left_column:
    if __name__ == "__main__":
        main()
  with right_column:
    st.write("##")
    st_lottie(lottie_coding, height=300, key="coding")



# Create a sample dataframe with latitude and longitude columns
df = pd.DataFrame({
    'lat': [41.3370, 41.3494, 41.2235, 41.2942, 41.2875, 41.3189, 41.3783, 41.2720],
    'lon': [69.2924, 69.2086, 69.2354, 69.2924, 69.1884, 69.3470, 69.2784, 69.1672]
})

# Create a Folium map centered on the US
m = folium.Map(location=[41.3231, 69.2354], zoom_start=10)

# Add markers to the map for each city in the dataframe
for index, row in df.iterrows():
    folium.Marker(location=[row['lat'], row['lon']]).add_to(m)

# Display the map using folium_static()
st.write("---")
st.subheader("News")
st.write("""
    There are over thousounds of active hosts nearby, and you're one of them! By encouraging travelers to stay
    with locals, Roamstay hopes to reduce the need for additional accommodation and resources, 
    while also promoting responsible and respectful travel behavior. 
    """)
folium_static(m)