import streamlit as st
import pandas as pd

from biz_logic.load_data import query_df, get_data
from biz_logic.process_user_query import get_full_response_code
from utility import check_password
from openai import OpenAI
#from helper_functions.llm import *


# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

st.title('Use natural language to query the dataset')

# explain function to user
st.text("""
        This is a sample of the dataset.        
        Using natural language, write prompts to draw insights from the data.
        """)


# retrieve the dataframe
df = get_data()
st.write(df.head(10))

# Set up OpenAI client
client = OpenAI(api_key=st.secrets["openai"]["openai_api_key"])

# Note that this function directly take in "messages" as the parameter.
def get_completion_by_messages(messages, model="gpt-4o-mini", temperature=0, top_p=1.0, max_tokens=1024, n=1):    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1
    )
    return response.choices[0].message.content


# give context to the prompt and prevent prompt injection
system_message = f"""
    You are a data scientist given a dataset assigned to variable df with the metadata details enclosed in #####
    
    #####
    month: Month of sale. datatype: Month (YYYY-MM)
    town: Designated residential area with its own amenities, infrastructure, and community facilities. datatype: text
    flat_type: Classification of units by room size. They range from 2 to 5 rooms, 3Gen units, and Executive units. datatype: text
    block: Classification of units by room size. They range from 2 to 5 rooms, 3Gen units, and Executive units. datatype: text
    street_name: A HDB building comprising multiple flats or apartments. datatype: text
    storey_range: Estimated range of floors the unit sold was located on. datatype: text
    floor_area_sqm: Total interior space within the unit, measured in square meters. datatype: numeric
    flat_model: Classification of units by generation of which the flat was made, ranging from New Generation, DBSS, Improved, Apartment. datatype: text
    lease_commence_date: Starting point of a lease agreement, marking the beginning of the lease term during which the tenant has the right to use and occupy the leased property. datatype: Year (YYYY)
    remaining_lease: Remaining amount of time left on the lease. datatype: text
    resale_price: Cost of the flat sold. datatype: numeric
    #####

    All values in the text datatype columns are fully uppercase.

    With the details above, translate the user query into python code using the pandas library, enclosed by the <pc> tag
    For example, to get the average floor_area_sqm, you will reply:
    <pc>df["floor_area_sqm"].mean()</pc>

    Should there be more than one line of code required, use separate <pc> tags for each line
    
    If the query is not relevant to the data set, reply with a message that informs the user on this.
    The user query is enclosed by a pair of <incoming-message> tags.

    Make sure you dont assign variable name to the query. 
    For example, do not do this: data_2020 = df["floor_area_sqm"]
    
    """

# get user prompt for query
form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")

    messages = [{"role":"system","content":system_message},
                {"role": "user", "content": f"<incoming-message>{user_prompt}</incoming-message>"}]

    response = get_completion_by_messages(messages) 
    # st.write(response)
    # print(f"User Input is {user_prompt}")
    

    temp_response = get_full_response_code(response=response)

    st.write(temp_response)

    output_df = query_df(temp_response)
    
    if "Error executing query" in str(output_df):
        st.error("There was an error in the response. Please try another question or be more specific.")    
    else:
        st.write(output_df)

    # process_query(df, user_prompt)

