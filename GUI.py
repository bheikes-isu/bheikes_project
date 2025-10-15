import WIP2
import streamlit as st
st.title("Dress for the Weather")
place = st.text_input("blah")
st.write("The place is", place)
st.write("The coordinates are", WIP2.getcoordinates(place))