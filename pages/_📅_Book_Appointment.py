import streamlit as st
from pymongo import MongoClient
import requests
import pandas as pd
from streamlit_extras.colored_header import colored_header
import uuid  # To generate unique booking numbers


def example():
    colored_header(
        label="Appointment Scheduler",
        description="Book an appointment with an expert dermatologist",
        color_name="violet-70",
    )


example()


client = MongoClient("mongodb+srv://iamuser:HYIW9tt5vtxjCgMA@cluster0.ibmseyj.mongodb.net/derm_ai?retryWrites=true&w=majority")

db = client["derm_ai"]
collection = db["appointment"]


doctors = ["Dr. Smith", "Dr. Johnson", "Dr. Williams", "Dr. Brown", "Dr. Jones"]


with st.form("user_details"):
    st.header("Enter Your Details")
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    selected_doctor = st.selectbox("Choose a Dermatologist", doctors)
    appointment_time = st.date_input("Select a Time")
    submit_user_details = st.form_submit_button("Submit")


if submit_user_details:
    # Generate a unique booking number
    booking_number = str(uuid.uuid4())[:8]  # Using the first 8 characters of UUID
    
    data = {
        "name": name,
        "phone": phone,
        "doctor": selected_doctor,
        "booking_number": booking_number,  # Include the booking number in the data
    }
    
    # Insert the data into MongoDB
    collection.insert_one(data)
    
    # Display the booking number to the user
    st.success(f"Appointment booked! Your booking number is: {booking_number}")
