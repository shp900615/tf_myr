import json
import uuid

import requests

# from .models import FacilityToken

BASE_URL = 'http://127.0.0.1:8000/'


def generate_token():
    return str(uuid.uuid4())

print("generate_token",generate_token() )
# #Create a FacilityToken
# def create_facility_token(facility_name, token):

#     # Generate a token if not provided
#     if token is None:
#         token = generate_token()

#     url = f'{BASE_URL}facility_tokens/'
#     data = {
#         'facility_name': facility_name,
#         'token': token,
#     }
#     response = requests.post(url, data=data)
#     if response.status_code == 201:  # Assuming 201 Created
#         # Store the token in the database using Django ORM
#         FacilityToken.objects.create(facility_name=facility_name, token=token)
#     return response.json()

# # # Example usage
# token = create_facility_token('CRH', None)
# print("token", token)





# #Read Facility Token
# def get_facility_tokens():
#     url = f'{BASE_URL}facility_tokens/'
#     response = requests.get(url)
#     return response.json()

# # Example usage
# print(get_facility_tokens())


# #Update a facility token 
# def update_facility_token(id, facility_name=None, token=None):
#     url = f'{BASE_URL}facility_tokens/{id}/'
#     data = {}
#     if facility_name:
#         data['facility_name'] = facility_name
#     if token:
#         data['token'] = token
#     response = requests.put(url, data=data)
#     return response.json()

# # Example usage
# print(update_facility_token(1, facility_name='Updated Facility', token='UpdatedToken'))


import pandas as pd

# file_path = 'uploaded_files/CRH-PD-DIAGNOSIS-AUG22.xlsx'
def read_excel_file(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, skiprows=1)

        # If you want to access the data as a list of dictionaries
        data = df.to_dict(orient='records')
        # print('data',data)
        return data
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None




def read_excel_file(file_path):
    # Read the Excel file, skipping the first row
    df = pd.read_excel(file_path, skiprows=1)
    return df



def validate_data(df):
    errors = []

    # Validate number of header columns
    expected_columns = ['Visit No', 'clinic', 'Diagnosis Name', 'Location']
    if len(df.columns) != len(expected_columns):
        errors.append(f"Expected {len(expected_columns)} columns, but found {len(df.columns)}.")

    # Validate names of header columns
    for column_name in expected_columns:
        if column_name not in df.columns:
            errors.append(f"Column '{column_name}' not found in the Excel file.")
    
    # Validate 'Visit No' column
    if 'Visit No' in df.columns:
        visit_no_errors = df['Visit No'].apply(validate_visit_no)
        errors.extend(visit_no_errors[visit_no_errors.notnull()])

    # Validate 'clinic' column
    if 'clinic' in df.columns:
        clinic_errors = df['clinic'].apply(validate_clinic)
        errors.extend(clinic_errors[clinic_errors.notnull()])

    # Validate 'Diagnosis Name' column
    if 'Diagnosis Name' in df.columns:
        diagnosis_errors = df['Diagnosis Name'].apply(validate_diagnosis_name)
        errors.extend(diagnosis_errors[diagnosis_errors.notnull()])

    # Validate 'Location' column
    if 'Location' in df.columns:
        location_errors = df['Location'].apply(validate_location)
        errors.extend(location_errors[location_errors.notnull()])

    return errors

import re


def validate_visit_no(visit_no):
    # Check if visit_no is null or empty
    if not visit_no:
        return "Visit No cannot be empty."

    # Check if visit_no contains only digits
    # if not re.match(r'^\d+$', visit_no):
    #     return "Invalid Visit No format. Should contain only digits."

    # Check if visit_no is not negative
    if int(visit_no) < 0:
        return "Visit No cannot be negative."

    return None


def validate_clinic(clinic):
    # Example validation function for 'clinic' column
    # You can implement your validation logic here
    return None

def validate_diagnosis_name(diagnosis_name):
    # Example validation function for 'Diagnosis Name' column
    # You can implement your validation logic here
    return None

def validate_location(location):
    # Example validation function for 'Location' column
    # You can implement your validation logic here
    return None


# df = read_excel_file(file_path)
# errors = validate_data(df)
# print(errors)
