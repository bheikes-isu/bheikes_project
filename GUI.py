import WIP2
import streamlit as st
st.title("Dress for the Weather")
place = st.text_input("Enter your location")
activity = st.selectbox("Select your activity", WIP2.activities)
weatherdata = WIP2.getweather(place)
st.write("The place is", place)
st.write("The temperature is", round(weatherdata,1), "degrees")
st.write("Suggested outfit is:", WIP2.weather(weatherdata))
#