import streamlit as st

st.title("Operations Team - KYC Verification")

st.write("🔍 List of Submitted KYCs (Simulated)")
st.write("1. Name: Ramesh Kumar | PAN: ABCDE1234F | Status: Pending")
st.write("2. Name: Priya Sharma | PAN: XYZAB5678C | Status: Pending")
print("hello")

if st.button("Approve All"):
    st.success("All KYCs Approved and Synced with Government APIs (Simulated)")