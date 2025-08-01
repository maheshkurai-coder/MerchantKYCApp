import streamlit as st

st.title("Merchant KYC Form")

business_type = st.selectbox("Business Type", ["Proprietor", "Private Ltd", "LLP", "Trust", "NGO", "Freelancer", "Referral Partner"])
name = st.text_input("Full Name")
pan = st.text_input("PAN Number")
aadhaar = st.text_input("Aadhaar Number")
gst = st.text_input("GSTIN (if applicable)")
address = st.text_area("Business Address")
contact = st.text_input("Contact Number")
email = st.text_input("Email Address")

if st.button("Submit"):
    st.success("KYC Submitted Successfully!")