import joblib
import numpy as np
import pandas as pd

feature_names = joblib.load("model/feature_names.joblib")

encoder_Marital_status = joblib.load("model\encoder_Marital_status.joblib")
encoder_Application_mode = joblib.load("model\encoder_Application_mode.joblib")
encoder_Course = joblib.load("model\encoder_Course.joblib")
encoder_Daytime_evening_attendance = joblib.load("model\encoder_Daytime_evening_attendance.joblib")
encoder_Debtor = joblib.load("model\encoder_Debtor.joblib")
encoder_Tuition_fees_up_to_date = joblib.load("model\encoder_Tuition_fees_up_to_date.joblib")
encoder_Gender = joblib.load("model\encoder_Gender.joblib")
encoder_Scholarship_holder = joblib.load("model\encoder_Scholarship_holder.joblib")

pca_1 = joblib.load("model\pca_1.joblib")

scaler_Previous_qualification_grade = joblib.load("model\scaler_Previous_qualification_grade.joblib")
scaler_Admission_grade = joblib.load("model\scaler_Admission_grade.joblib")
scaler_Age_at_enrollment = joblib.load("model\scaler_Age_at_enrollment.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("model\scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model\scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model\scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_grade =joblib.load("model\scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("model\scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model\scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model\scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model\scaler_Curricular_units_2nd_sem_grade.joblib")

pca_numerical_columns_1 = ['Curricular_units_1st_sem_credited','Curricular_units_1st_sem_enrolled',
                'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
                'Curricular_units_2nd_sem_credited','Curricular_units_2nd_sem_enrolled',
                'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade'
]

def data_preprocessing(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    columns_used = ['Marital_status', 'Application_mode','Course','Daytime_evening_attendance',
                'Debtor','Tuition_fees_up_to_date','Gender','Scholarship_holder', 
                'Previous_qualification_grade', 'Admission_grade', 'Age_at_enrollment',
                'Curricular_units_1st_sem_credited','Curricular_units_1st_sem_enrolled',
                'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
                'Curricular_units_2nd_sem_credited','Curricular_units_2nd_sem_enrolled',
                'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',]
    
    data = data[columns_used]

    df = pd.DataFrame()

    def reshape_transform(data,encoder,feature):
        X = data[feature].values.reshape(-1, 1)
        encoded_feature = encoder.transform(X).toarray()
        result = pd.DataFrame(encoded_feature, columns=encoder.get_feature_names_out([feature]))
        return result
    
    df = pd.concat([df, reshape_transform(data=data,encoder=encoder_Marital_status,feature='Marital_status')], axis=1)
    df = pd.concat([df, reshape_transform(data=data,encoder=encoder_Application_mode,feature='Application_mode')], axis=1)
    df = pd.concat([df, reshape_transform(data=data,encoder=encoder_Course,feature='Course')], axis=1)
    df = pd.concat([df, reshape_transform(data=data,encoder=encoder_Daytime_evening_attendance,feature='Daytime_evening_attendance')], axis=1)
    df = pd.concat([df, reshape_transform(data=data,encoder=encoder_Debtor,feature='Debtor')], axis=1)
    df = pd.concat([df, reshape_transform(data=data,encoder=encoder_Tuition_fees_up_to_date,feature='Tuition_fees_up_to_date')], axis=1)
    df = pd.concat([df, reshape_transform(data=data,encoder=encoder_Gender,feature='Gender')], axis=1)
    df = pd.concat([df, reshape_transform(data=data,encoder=encoder_Scholarship_holder,feature='Scholarship_holder')], axis=1)

    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))[0]
    df["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1,1))[0]
    df["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    
    # PCA 1
    data["Curricular_units_1st_sem_credited"] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(data["Curricular_units_1st_sem_credited"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_credited"] = scaler_Curricular_units_2nd_sem_credited.transform(np.asarray(data["Curricular_units_2nd_sem_credited"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]
    
    df[["pc1_1", "pc1_2", "pc1_3"]] = pca_1.transform(data[pca_numerical_columns_1])
    
    df = df[feature_names]
    
    return df
