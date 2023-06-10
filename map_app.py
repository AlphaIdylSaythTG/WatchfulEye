import streamlit as st
import folium
import sqlite3
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static
from PIL import Image
from streamlit_option_menu import option_menu
from annotated_text import annotated_text
import pandas as pd
import pydeck as pdk
from streamlit_chat import message




# Set page title and favicon

logo_image = Image.open("Logo.png")
st.image(logo_image, use_column_width=True)

selected = option_menu(
    menu_title=None,
    options=["Crime Mapper", "Safety Corner"],
    # possibly even add a crime prediction option
    icons=["map", "search"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Crime Mapper":
    # Create a SQLite database connection
    conn = sqlite3.connect("markers.db")
    c = conn.cursor()

    # Create a markers table if it doesn't exist
    c.execute(
        '''CREATE TABLE IF NOT EXISTS markers
                (latitude REAL, longitude REAL, popup TEXT, color TEXT)'''
    )

    # Create a map centered at latitude 40.7128 and longitude -74.0060 (New York City)
    m = folium.Map(location=[40.7128, -94.0060], zoom_start=4)

    # Retrieve markers data from the database
    c.execute("SELECT * FROM markers")
    marker_locations = c.fetchall()

    for marker in marker_locations:
        latitude, longitude, popup, color = marker
        folium.Marker(
            location=[latitude, longitude],
            popup=popup,
            icon=folium.Icon(color=color),
        ).add_to(m)

    # Display the map using folium_static with custom width and height
    folium_static(m, width=700, height=600)

    # Center the titles using CSS
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            margin-top: 20px;
            color: white; /* Foreground color */
            background-color: red; /* Background color */
            text-decoration: none;
            border-radius: 10px;
        }
        .form-container {
            border: 1px solid black;
            border-radius: 5px;
            margin-bottom: 20px;
            padding: 20px;
        }
        .search-button {
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Page for users to submit suspicious activity
    st.markdown('<p class="title">Report Suspicious Activity</p>', unsafe_allow_html=True)
    st.markdown("---")  # Add a horizontal line for separation

    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            latitude = st.number_input("Latitude", value=0.0, step=0.0001)
    with col2:
        with st.container():
            longitude = st.number_input("Longitude", value=0.0, step=0.0001)

    with st.container():
        with st.container():
            description = st.text_area("Description")

    submitted = st.button("Submit")

    if submitted:
        # Insert the submitted suspicious activity into the database
        c.execute(
            "INSERT INTO markers VALUES (?, ?, ?, ?)",
            (latitude, longitude, description, "yellow"),
        )
        conn.commit()

        # Add a marker for the submitted suspicious activity
        folium.Marker(
            location=[latitude, longitude],
            popup=description,
            icon=folium.Icon(color="yellow"),
        ).add_to(m)

        # Display the updated map with the new marker
        folium_static(m, width=800, height=600)

    # Page for users to search location and get latitude and longitude
    st.markdown('<p class="title">Search Location</p>', unsafe_allow_html=True)
    st.markdown("---")  # Add a horizontal line for separation

    location_input = st.text_input("Enter a location or ZIP code")
    location_button = st.button("Get Latitude and Longitude", key="location_button")

    if location_button:
        geolocator = Nominatim(user_agent="my-app")
        location = geolocator.geocode(location_input)
        if location:
            st.write("Latitude:", location.latitude)
            st.write("Longitude:", location.longitude)
        else:
            st.write("Location not found")

    # Close the database connection
    conn.close()

if selected == "Safety Corner":
     # Page title and description
    st.title("Safety Corner")
    st.write("Welcome to the Safety Corner! Here, you can get safety tips, resources, and educational materials to help you stay safe.")

    # Chatbot section
    st.header("Chat with our Safety Bot")
    
    # Example chatbot messages
    message("Hello! How can I assist you today?")
    message("I'm here to provide safety tips and answer any questions you have.")

    # User input
    user_input = st.text_input("Enter your message")
    if user_input:
        # Process user input and generate bot's response
        bot_response = generate_bot_response(user_input)  # Replace with your own logic

        # Display bot's response
        message(bot_response, is_user=False)

    # Add more safety tips and resources below

    # End of Safety Corner page

    
    

    

    