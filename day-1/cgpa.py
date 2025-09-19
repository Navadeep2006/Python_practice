import streamlit as st
st.title("📘 CGPA Calculator")
semester_count = st.number_input(
    "Enter your current semester number:",
    min_value = 1,
    max_value = 12,
    step = 1
)
all_cgpas = []
for sem in range(1, semester_count + 1):
    value = st.number_input(
        f"Enter the CGPA for Semester {sem}:",
        min_value = 0.0,
        max_value = 10.0,
        step = 0.01,
        format = "%.2f"
    )
    all_cgpas.append(value)
if st.button("Calculate Total CGPA"):
    if all_cgpas:
        total_cgpa = sum(all_cgpas) / semester_count
        st.success(f"🎯 Your total CGPA up to Semester {semester_count} is: **{round(total_cgpa, 2)}**")
    else:
        st.warning("Please enter the CGPA for all semesters.")
