

import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv('API_KEY')
print(api_key)

# Get weather for multiple cities
data_pull_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=charlotte&appid='+ api_key)
print(data_pull_request.text)

