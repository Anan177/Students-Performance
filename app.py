import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Marital_status, encoder_Application_mode, encoder_Course, encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Tuition_fees_up_to_date, encoder_Gender, encoder_Scholarship_holder
from prediction import prediction

data = pd.DataFrame()
st.image("image.jpg")
st.title("Student's Performance App (Prototype)")
Description, Input_Model= st.tabs(["Description", "Predict a Student"])
 
with Description:
    st.subheader("About App")
    st.markdown("""
                + This is a simple app for predicting a student's performance and determining whether the student will graduate or drop out.
                + DISCLAIMER: This model is trained by using Random Forest algorithm and requires several inputs or characteristics from the student.
                """)
    st.info("##Created by Ananta A.T to complete the Dicoding Class.")
with Input_Model:
    with st.expander("Categorical Input"):
        col1, col2, col3 = st.columns(3)
    
        with col1:
            Application_mode = st.selectbox(label='Application mode', options=encoder_Application_mode.categories_[0], index=0)
            data["Application_mode"] = [Application_mode]
        
        with col2:
            Course = st.selectbox(label='Course', options=encoder_Course.categories_[0], index=0)
            data["Course"] = [Course]
        
        with col3:
            Daytime_evening_attendance = st.selectbox(label='Daytime/evening attendance', options=encoder_Daytime_evening_attendance.categories_[0], index=0)
            data["Daytime_evening_attendance"] = [Daytime_evening_attendance]

        col1, col2, col3 = st.columns(3)
    
        with col1:
            Tuition_fees_up_to_date = st.selectbox(label='Tuition fees up to date', options=encoder_Tuition_fees_up_to_date.categories_[0], index=0)
            data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
        
        with col2:
            Scholarship_holder = st.selectbox(label='Scholarship holder', options=encoder_Scholarship_holder.categories_[0], index=0)
            data["Scholarship_holder"] = [Scholarship_holder]
        
        with col3:
            Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.categories_[0], index=0)
            data["Debtor"] = Debtor

        col1, col2 = st.columns(2)
    
        with col1:
            Marital_status = st.selectbox(label='Marital status', options=encoder_Marital_status.categories_[0], index=0)
            data["Marital_status"] = [Marital_status]
        
        with col2:
            Gender = st.selectbox(label='Gender', options=encoder_Gender.categories_[0], index=0)
            data["Gender"] = [Gender]

    with st.expander("Numerical Input"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Previous_qualification_grade = st.number_input(label='Previous qualification (grade)', value=0)
            data["Previous_qualification_grade"] = Previous_qualification_grade
        
        with col2:
            Admission_grade = st.number_input(label='Admission grade', value=0)
            data["Admission_grade"] = Admission_grade
        
        with col3:
            Age_at_enrollment = st.number_input(label='Age at enrollment', value=0)
            data["Age_at_enrollment"] = Age_at_enrollment

        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            Curricular_units_1st_sem_credited = st.number_input(label='Curricular units 1st sem (credited)', value=0)
            data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited
        
        with col2:
            Curricular_units_1st_sem_enrolled = st.number_input(label='Curricular units 1st sem (enrolled)', value=0)
            data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled
        
        with col3:
            Curricular_units_1st_sem_approved = st.number_input(label='Curricular units 1st sem (approved)', value=0)
            data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

        with col4:
            Curricular_units_1st_sem_grade = st.number_input(label='Curricular units 1st sem (grade)', value=0)
            data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            Curricular_units_2nd_sem_credited = st.number_input(label='Curricular units 2nd sem (credited)', value=0)
            data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited
        
        with col2:
            Curricular_units_2nd_sem_enrolled = st.number_input(label='Curricular units 2nd sem (enrolled)', value=0)
            data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled
        
        with col3:
            Curricular_units_2nd_sem_approved = st.number_input(label='Curricular units 2nd sem (approved)', value=0)
            data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

        with col4:
            Curricular_units_2nd_sem_grade = st.number_input(label='Curricular units 2nd sem (grade)', value=0)
            data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

    with st.expander("View the Raw Data"):
        st.dataframe(data=data, width=800, height=10)

    if st.button('Predict'):
        new_data = data_preprocessing(data=data)
        with st.expander("View the Preprocessed Data"):
            st.dataframe(data=new_data, width=800, height=10)
        st.write("Student's Status Prediction:".format(prediction(new_data)))
        st.write(prediction(new_data))