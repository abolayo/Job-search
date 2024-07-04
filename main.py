# Import packages
from dash import Dash, html, dash_table
from bs4 import BeautifulSoup, SoupStrainer
import requests
import json
import pandas as pd


# Let's plan a trip to Austrian Alps
airbnb_url = "https://docs.google.com/spreadsheets/d/1n71WqF1ifLuDwz2UDr0TNXxj5KYlvCBm7Afl6WMLUxA/edit?gid=0#gid=0"
soup = BeautifulSoup(requests.get(airbnb_url).content)
print(soup.prettify())

