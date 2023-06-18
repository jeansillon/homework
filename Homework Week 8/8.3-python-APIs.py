

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
weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=charlotte&appid='+ api_key)
print(weather.text)

# Convert the JSON data to a DataFrame
df = pd.DataFrame(weather)

# Print the DataFrame
print(df)


# Export the DataFrame to a CSV file
df.to_csv('weather.csv', index=False)

print("Data exported successfully!")