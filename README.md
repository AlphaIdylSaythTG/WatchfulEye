# WatchfulEye

# Community Safety and Crime Prevention

Community Safety and Crime Prevention is a web application that allows community members to report safety concerns, suspicious activities, or incidents to local law enforcement agencies. The application provides an interactive map where users can view reported suspicious activities and submit their own reports. It aims to empower communities by promoting awareness and facilitating communication between residents and authorities.

![Screen Shot 2023-06-09 at 1 47 35 PM](https://github.com/AlphaIdylSaythTG/WatchfulEye/assets/123337877/cdfb5171-fb78-4702-81a6-4cf020622aab)

## Features

- **Report Suspicious Activity:** Users can submit reports of suspicious activities by providing the latitude, longitude, and description of the incident.
- **Interactive Map:** The application displays a map with markers representing reported suspicious activities. Users can view details of each incident by clicking on the markers.
- **Search Location:** Users can search for a location or ZIP code and retrieve the latitude and longitude coordinates of that area. The number of reported suspicious activities in the area is also displayed.

## Technologies Used

- Python
- Streamlit: For building the web application.
- Folium: For interactive map visualization.
- SQLite: As the database for storing reported suspicious activities.
- Geopy: For geocoding and retrieving location coordinates.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/community-safety.git
   cd community-safety
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

   The application will be accessible at `http://localhost:8501` in your browser.

## Authors
Made by Yash Thapliyal and Laxya Kumar
