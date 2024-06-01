import streamlit as st
import datetime
import requests
import pandas as pd
from shapely.geometry import Point, Polygon
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

'''
# TaxiFareModel
'''

st.markdown(''' ## We're going to give you a good idea of the fare for your taxi ride in NYC !
''')

'''
### Please fill below:

'''


url = 'https://taxifare.lewagon.ai/predict'

label_0= "Insert date"
label_1= "Insert time"
label_2 = "Insert pickup longitude"
label_3 = "Insert pickup latitude"
label_4 = "Insert dropoff longitude"
label_5 = "Insert dropoff latitude"
label_6 = "Insert passenger count"



# street = st.sidebar.text_input("Street", "75 Bay Street")
# city = st.sidebar.text_input("City", "Toronto")
# province = st.sidebar.text_input("Province", "Ontario")
# country = st.sidebar.text_input("Country", "Canada")

# geolocator = Nominatim(user_agent="GTA Lookup")
# geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
# location = geolocator.geocode(street+", "+city+", "+province+", "+country)

# lat = location.latitude
# lon = location.longitude


with st.form("my_form"):

    pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_datetime = f'{pickup_date} {pickup_time}'


    # pickup_street = st.text_input("Pickup Street", "75 Bay Street")
    # pickup_city = st.text_input("Pickup City", "Toronto")
    # pickup_province = st.text_input("Pickup Province", "Ontario")
    # pickup_country = st.text_input("Pickup Country", "Canada")

    # dropoff_street = st.text_input("Dropoff Street", "75 Bay Street")
    # dropoff_city = st.text_input("Dropoff City", "Toronto")
    # dropoff_province = st.text_input("Dropoff Province", "Ontario")
    # dropoff_country = st.text_input("Dropoff Country", "Canada")


    pickup_longitude = st.number_input(label_2, min_value=None, max_value=None, value = -73.989, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Type longitude...", disabled=False, label_visibility="visible")
    pickup_latitude = st.number_input(label_3, min_value=None, max_value=None, value=40.747, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Type latitude...", disabled=False, label_visibility="visible")
    dropoff_longitude = st.number_input(label_4, min_value=None, max_value=None, value=-73.956, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Type longitude...", disabled=False, label_visibility="visible")
    dropoff_latitude = st.number_input(label_5, min_value=None, max_value=None, value=40.802, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Type latitude...", disabled=False, label_visibility="visible")

    passenger_count = st.selectbox('Select number of passengers',('1', '2', '3', '4', '5', '6' ))

    submitted = st.form_submit_button("Submit")

# geolocator = Nominatim(user_agent="GTA Lookup")
# geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
# pickup_location = geolocator.geocode(pickup_street+", "+pickup_city+", "+pickup_country+", "+pickup_country)
# pickup_latitude = pickup_location.latitude
# pickup_longitude = pickup_location.longitude

# dropoff_location = geolocator.geocode(dropoff_street+", "+dropoff_city+", "+dropoff_province+", "+dropoff_country)
# dropoff_latitude = dropoff_location.latitude
# dropoff_longitude = dropoff_location.longitude



if submitted:
        params = {'pickup_datetime' : pickup_datetime, 'pickup_longitude' : pickup_longitude, 'pickup_latitude' : pickup_latitude,
          'dropoff_longitude' : dropoff_longitude, 'dropoff_latitude' : dropoff_latitude,'passenger_count' : passenger_count }
        response = round((requests.get(url, params= params).json()['fare']), 2)
        st.header(f'Your taxi fare will be : ${response}')



        data = pd.DataFrame({
        'lat': [pickup_latitude, dropoff_latitude],
        'lon': [pickup_longitude, dropoff_longitude]
        })
        st.map(data)
