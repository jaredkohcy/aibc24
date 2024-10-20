import streamlit as st
import pandas as pd

from biz_logic.load_data import query_df, get_data
#from biz_logic.process_user_query import get_full_response_code
from utility import check_password

def generate_table(df, month_list, flat_type_list, flat_model_list, town_list, area_val_min, area_val_max):
    temp_df = df
    temp_df = temp_df[temp_df["month"].isin(month_list)] if len(month_list) != 0 else temp_df
    temp_df = temp_df[temp_df["flat_type"].isin(flat_type_list)] if len(flat_type_list) != 0 else temp_df
    temp_df = temp_df[temp_df["flat_model"].isin(flat_model_list)] if len(flat_model_list) != 0 else temp_df
    temp_df = temp_df[temp_df["town"].isin(town_list)] if len(town_list) != 0 else temp_df
    temp_df = temp_df[temp_df["floor_area_sqm"] >= area_val_min]
    temp_df = temp_df[temp_df["floor_area_sqm"] <= area_val_max]

    return temp_df
    



# # Do not continue if check_password is not True.  
# if not check_password():  
#     st.stop()

st.title('Filter the data to get the details required')

df = get_data()

month_list = st.multiselect("Select month", sorted(df.month.drop_duplicates()))
flat_type_list = st.multiselect("Select Flat type", sorted(df.flat_type.drop_duplicates()))
flat_model_list = st.multiselect("Select Flat model", sorted(df.flat_model.drop_duplicates()))
town_list = st.multiselect("Select town", sorted(df.town.drop_duplicates()))
area_val_min = st.slider("Select min floor area (sqm)",min_value=1, max_value=int(max(df.floor_area_sqm)), step=1)
area_val_max = st.slider("Select max floor area (sqm)",min_value=1, max_value=int(max(df.floor_area_sqm)), step=1)

# st.button("Submit", on_click=button_on_click(df, month_list, flat_type_list, flat_model_list, area_val_min, area_val_max))
# st.slider(min_value=)
temp_df = generate_table(df, month_list, flat_type_list, flat_model_list, town_list, area_val_min, area_val_max)

st.write(temp_df)
st.scatter_chart(temp_df, y="resale_price", x ="floor_area_sqm")
