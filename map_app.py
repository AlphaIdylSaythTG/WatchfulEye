import streamlit as st
import folium
import sqlite3
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static

# Create a SQLite database connection
conn = sqlite3.connect("markers.db")
c = conn.cursor()

# Create a markers table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS markers
             (latitude REAL, longitude REAL, popup TEXT, color TEXT)''')

# Create a map centered at latitude 40.7128 and longitude -74.0060 (New York City)
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# Retrieve markers data from the database
c.execute("SELECT * FROM markers")
marker_locations = c.fetchall()

for marker in marker_locations:
    latitude, longitude, popup, color = marker
    folium.Marker(location=[latitude, longitude], popup=popup, icon=folium.Icon(color=color)).add_to(m)

# Display the map using folium_static with custom width and height
folium_static(m, width=800, height=600)

# Page for users to submit suspicious activity
st.subheader("Report Suspicious Activity")

with st.form("suspicious_activity_form"):
    col1, col2 = st.columns(2)
    with col1:
        latitude = st.number_input("Latitude")
    with col2:
        longitude = st.number_input("Longitude")

    description = st.text_area("Description")

    submitted = st.form_submit_button("Submit")

if submitted:
    # Insert the submitted suspicious activity into the database
    c.execute("INSERT INTO markers VALUES (?, ?, ?, ?)", (latitude, longitude, description, "yellow"))
    conn.commit()

    # Add a marker for the submitted suspicious activity
    folium.Marker(location=[latitude, longitude], popup=description, icon=folium.Icon(color="yellow")).add_to(m)

    # Display the updated map with the new marker
    folium_static(m, width=800, height=600)

# Page for users to search location and get latitude and longitude
st.subheader("Search Location")

location_input = st.text_input("Enter a location or ZIP code")
location_button = st.button("Get Latitude and Longitude")

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
