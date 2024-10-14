import streamlit as st
from utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

st.title('About Us')

st.text_area("Background",
             "Not all users are trained in coding, hence being unable to do detailed data analysis despite having ideas on exploring potential trends or hypotheses.")

st.text_area("Problem Statement",
             "How can we allow users to retrieve insights from data using natural language?")

st.text_area("Proposed Solution",
             "We plan to implement a model to allow users to input data query questions in natural language to do basic filtering of the data.")

st.text_area("Use cases",
             "1) Generate queries based on natural language into python-pandas query to retrieve the required data.\n2) Use the filters to see the details in the dataset.")

st.text_area("Impact",
             "This would grant more flexibility to users to query large datasets, and reduce the duration to retrieving useful insights.")

st.text_area("Stakeholders and Users",
             "Users interested in this dataset")

st.text_area("Data Source",
             "Data.gov.sg -- https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view")

