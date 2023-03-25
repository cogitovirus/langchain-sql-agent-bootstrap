import os
import pandas as pd

from dotenv import load_dotenv
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI

load_dotenv()

open_api_key = os.getenv("OPENAI_API_KEY")

df = pd.read_csv('data/kc_house_data_NaN.csv')

agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)

# agent.run("What is the average of price column?")
# agent.run("Does the price increase with the number of id?")
# agent.run("How many null values are there in the bedrooms column?")




