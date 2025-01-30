import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()
api_key = os.getenv('API_KEY')

def fetch_air_quality_data(api_key, city):
    url = f"https://api.openaq.org/v1/measurements?city={city}&limit=10"  
    headers = {"X-API-Key": api_key}
    
  
    response = requests.get(url, headers=headers)

   
    if response.status_code == 200:
        data = response.json()
        

        if "results" in data and data["results"]:
            df = pd.DataFrame(data['results'])
            print(df.head())
      
            if not os.path.exists('data'):
                os.makedirs('data')
            
            # Save the JSON response to a file
            with open("data/air_quality.json", "w") as file:
                json.dump(data, file, indent=4)
            
            print("Data successfully saved to data/air_quality.json")
            return data["results"] 
        else:
            print("No air quality data found in the response.")
            return None
    else:
        print(f"Error fetching data: {response.status_code}")
        return None


data = fetch_air_quality_data(api_key, "London")


if data:
    print("Fetched Data:")
    for item in data:
        print(item) 
else:
    print("No data fetched.")