import streamlit as st
from requirement_analysis import extract_features
from task_generation import generate_tasks
from timeline_estimation import estimate_time

st.title("Intelligent Requirement-to-Delivery Project Automation")

st.write("Enter the client project requirement below")

requirement = st.text_area("Project Requirement")

if st.button("Generate Project Plan"):

    features = extract_features(requirement)

    st.subheader("Extracted Features")
    st.write(features)

    tasks = generate_tasks(features)

    st.subheader("Generated Tasks")
    for t in tasks:
        st.write(t)

    duration = estimate_time(tasks)

    st.subheader("Estimated Project Duration")
    st.write(str(duration) + " days")
    
    