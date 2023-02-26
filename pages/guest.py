import streamlit as st
import pandas as pd

# Define the function to retrieve data by city
def search_by_city(city):
    data_list = []
    with open("contacts.txt", "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if data[2].lower() == city.lower():
                data_list.append(data)
    df = pd.DataFrame(data_list, columns=["Name", "Phone", "City", "Info"])
    return df

# Define the Streamlit app
def main():
    st.title("Guest 🙎‍♂️")
    st.write(
        """
        Roamstay hosts come from a variety of backgrounds and may offer anything from a 
        spare room to a couch or air mattress in a common area. This allows guests to choose 
        the type of accommodation that best suits their needs, whether they're looking for a private 
        space or a more communal experience.
        """)
    st.write("---")

    # Create a search box for the city
    st.subheader("Search 🔎")
    city = st.text_input("Enter your location:")

    # When the user clicks the "Search" button, display the results in a table
    if st.button("Search"):
        results = search_by_city(city)
        if len(results) == 0:
            st.write("No results found.")
        else:
            st.write("---")
            st.subheader("Available hosts nearby 📍")
            st.table(results)

if __name__ == "__main__":
    main()
