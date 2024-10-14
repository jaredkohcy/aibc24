import pandas as pd
import streamlit as st
import numpy as np

df = pd.read_csv("./data/ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv")

@st.cache_data
def get_data():    
    df = pd.read_csv("./data/ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv")
    df["flat_model"] = df["flat_model"].str.upper()
    return df

def query_df(query, data = df):
    df = data
    try:
        result = eval(query)
        if isinstance(result, pd.DataFrame):
            return result
        elif isinstance(result, pd.Series):
            return result
        elif isinstance(result, np.ndarray):
            return result
        else:
            return result
    except Exception as e:
        return f"Error executing query: {str(e)}"
    



# eval('df_filtered = df[(df["town"] == "Bishan") & (df["month"].str.startswith("2018"))]  \ndf_filtered["floor_area_sqm"].max()')
exec('df_filtered = df[(df["town"] == "Bishan") & (df["month"].str.startswith("2018"))]  \ndf_filtered["floor_area_sqm"].max()')