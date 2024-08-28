# import streamlit as st
# import pandas as pd
# from util import Util
# import time, random

# st.set_page_config(
#     page_title="Liver Disease Prediction",
# )

# util = Util(file_path='indian_liver_patient.csv')
# st.header("LIVER DISEASE PREDICTION APPLICATION")

# # Define function to load data
# @st.cache(allow_output_mutation=True)
# def load_data(file_path):
#     return util.get_data()

# # Create a text element and let the reader know the data is loading.
# data_load_state = st.info('Loading data...')
# # Load rows of data 
# patient_data = load_data('indian_liver_patient.csv')

# # Define function to split data
# @st.cache(allow_output_mutation=True)
# def split_data(patient_data):
#     return util.split_data(patient_data)

# X_train, X_test, y_train, y_test = split_data(patient_data)

# #train model
# data_load_state.info("Training the model..")
# model = util.build_model(X_train, y_train)

# # Notify the reader that the data was successfully loaded.
# data_load_state.info('Application is ready for predictions.')


# ## FORM for Prediction
# st.subheader("Fill in your patient data here for diagnosis")

# with st.sidebar:
#     st.subheader("Try other values")

#     randomize = st.button("Generate test patient values")

#     if randomize:
#         data_list = util.sample_data(patient_data)
#         idx = random.randint(0, len(data_list))
#         input_vals = data_list[idx]
#         st.json(input_vals)

# util.form_functions(model)

# st.markdown(util.page_footer(),unsafe_allow_html=True)








import streamlit as st
import pandas as pd
from util import Util
import time, random

st.set_page_config(
    page_title="CliniLiver",
)

util = Util(file_path='indian_liver_patient.csv')
st.header("LIVER DISEASE PREDICTION APPLICATION")

# Define function to load data
@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_data(file_path):
    return util.get_data()

# Create a text element and let the reader know the data is loading.
data_load_state = st.info('Loading data...')
# Load rows of data 
patient_data = load_data('indian_liver_patient.csv')

# Notify the reader that the data was successfully loaded.
data_load_state.info('Application is ready for predictions.')

# Define function to split data
@st.cache(allow_output_mutation=True)
def split_data(patient_data):
    return util.split_data(patient_data)

X_train, X_test, y_train, y_test = split_data(patient_data)

# Train model
model = None
with st.spinner('Training the model..'):
    model = util.build_model(X_train, y_train)
    st.success('Model training complete!')

## FORM for Prediction
st.subheader("Fill in your patient data here for diagnosis")

with st.sidebar:
    st.subheader("Try other values")

    randomize = st.button("Generate test patient values")

    if randomize:
        data_list = util.sample_data(patient_data)
        idx = random.randint(0, len(data_list))
        input_vals = data_list[idx]
        st.json(input_vals)

util.form_functions(model)

st.markdown(util.page_footer(), unsafe_allow_html=True)

