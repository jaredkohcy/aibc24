import streamlit as st
from utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

st.title('Methodology')

st.text_area("Use cases",
             "1) Generate queries based on natural language into python-pandas query to retrieve the required data.\n2) Use the filters to find the suitable places to select the house of choice",
             height = 100)

st.text_area("Use case 1",
             """1) The data set is preloaded upon initialising of the app.

2) Using the LLM, we generate the python code using the pandas library to query the dataframe. 

3) The dataset is then filtered, transformed, or aggregated to give the results desired.
             """, height = 160)



st.text_area("Use case 2",
             """1) Useful filters based on the dataset is available for manual slicing.

2) These slicers are widgets available in streamlit, to allow filtering and aggregation of data.

3) The final output is displayed.
             """, height = 160)