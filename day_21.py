import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')



with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
my_bar = st.progress(slider_val)

for percent_complete in range(slider_val,100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)




st.write("Outside the form")

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

st.snow()
st.balloons()




