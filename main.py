import streamlit as st
import pandas as pd
import numpy as np

from biz_logic.load_data import get_data
from utility import check_password

def main():
    # Do not continue if check_password is not True.  
    if not check_password():  
        st.stop()

    st.title('ATTENTION')

    st.text_area("Disclaimer","""IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

    Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

    Always consult with qualified professionals for accurate and personalized advice.""", height = 200)

df = get_data()

if __name__ == "__main__":
    main()
