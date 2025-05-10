import streamlit as st
from riskcalc import calculate_bmi, categorize_bmi, categorize_waist_circumference, identify_diabetes_risk

st.title("Medical Classification for Weight")
gender = st.selectbox("Gender",["Male","Female"])
height = st.number_input("Height in cms",value=168)
weight = st.number_input("Weight in kgs",value=68)
waist = st.number_input("Waist Circumference in cms", value=88)

try:
    bmi = calculate_bmi(height, weight)
    if bmi is not None:
        bmi_category = categorize_bmi(bmi)
        wc_category = categorize_waist_circumference(waist, gender)
    
    st.text(f"\nBMI: {bmi:.2f} ({bmi_category} with {wc_category})")

    rr, absolute_risk = identify_diabetes_risk(
        bmi_category, wc_category, gender
        )
    st.text(f"Absolute Risk (5 years) for Type 2 Diabetes Mellitus: {absolute_risk}%.")

    if absolute_risk < 1.0:
        st.text("Medical Classification: P1")

    if 1.0 < absolute_risk <=5.0:
        abn = st.selectbox("Co-morbidities/ abnormal bio-chemistry/ abnormal ECG",["No","Yes"])
        if abn == 'No':
            st.text("Medical Classification: P1")
            
        else:
            st.text("Medical Classifiation: P2")
    
    if absolute_risk > 5.0:
        st.text("Medical Classification: P2")



except ValueError:
        st.text(
            "Please enter valid numeric values for height, weight, and waist circumference."
        )