import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Define the hard-coded data for the dermatologists
dermatologists = [
    {
        "Name": "Dr. Michael Brown",
        "Designation": "Clinical Dermatologist",
        "Available Days": "Mon, Wed, Fri",
        "Timings": "9am - 5pm"
    },
    {
        "Name": "Dr. Jessica Davis",
        "Designation": "Cosmetic Dermatologist",
        "Available Days": "Tue, Thu, Sat",
        "Timings": "10am - 6pm"
    },
    {
        "Name": "Dr. Jane Smith",
        "Designation": "Pediatric Dermatologist",
        "Available Days": "Mon, Wed, Fri",
        "Timings": "8am - 4pm"
    },
    {
        "Name": "Dr. John Doe",
        "Designation": "Clinical Dermatologist",
        "Available Days": "Tue, Thu, Sat",
        "Timings": "11am - 7pm"
    },
    {
        "Name": "Dr. Emily Johnson",
        "Designation": "Dermatopathologist",
        "Available Days": "Mon, Wed, Fri",
        "Timings": "9am - 5pm"
    }
]

# Set the title of the app
st.title("Available Dermatologists")

# Create a DataFrame to display the data in a table
import pandas as pd
df = pd.DataFrame(dermatologists)

# Style the DataFrame
st.dataframe(df.style.set_properties(**{
    'background-color': 'black',
    'color': 'white',
    'border-color': 'gray'
}))

# Add additional styling to the app
st.markdown("""
    <style>
    
    .streamlit-expanderHeader {
        font-size: 18px;
        font-weight: bold;
    }
    .css-1d391kg {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    </style>
""", unsafe_allow_html=True)




# Display additional information about the dermatologists
st.subheader("Note:")
st.markdown("""
- Please book an appointment in advance to avoid waiting.
- In case of emergency, contact the dermatologist directly.
- Always check for the latest availability as schedules may change.
""")

# Add a call to action button
if st.button('Book an Appointment'):
    switch_page('appointment')
    