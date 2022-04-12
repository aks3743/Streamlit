import streamlit as st

st.header('Day 11 App')

options = st.multiselect(
     'How many days has passed since you started the Challenge',
     range(1,12),
     [1,11])

st.write('You selected:', options)