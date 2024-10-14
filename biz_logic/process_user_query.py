import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv('.env')

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_full_response_code(response):
    temp_response = response    
    temp_str = ""

    temp_str = response.replace("<pc>","")
    temp_str = temp_str.replace("</pc>","")

    # while "<pc>" in temp_response:
    #     # find nearest <pc> and retrieve details
    #     start = temp_response.find("<pc>")+4
    #     end = temp_response[start.index:].find("</pc>")
    #     temp_str = temp_str+"\n"+temp_response[start:end]

    #     # continue to search in remaining portion of string
    #     temp_response = temp_response[end:]

    return temp_str

