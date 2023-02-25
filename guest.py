import streamlit as st
import pandas as pd

st.title("House taker")

st.write("A person who wants to share house, click here.")


# Define the data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'City': ['National hotel', 'Korean hotel', 'London', 'San Francisco'],
    'Country': ['Yunusobod', 'Chilonzor', 'Sergeli', ''],
    'Interests': ['Cooking', 'Hiking', 'Reading', 'Music']
})

# Define the sidebar options
cities = sorted(data['City'].unique())
selected_city = st.sidebar.selectbox('Select a city', cities)

countries = sorted(data['Country'].unique())
selected_country = st.sidebar.selectbox('Select a country', countries)

# Filter the data based on the selected city and country
filtered_data = data[(data['City'] == selected_city) & (data['Country'] == selected_country)]

# Show the filtered data
st.write('Couch surfers in {} ({})'.format(selected_city, selected_country))
st.write(filtered_data)


         
