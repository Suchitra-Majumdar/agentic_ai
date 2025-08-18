from dotenv import load_dotenv


load_dotenv()
import os
API_KEY = os.getenv("WEATHER_API_KEY")
API_URL = os.getenv("WEATHER_API_URL")
import requests
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(API_URL, params=params)
    print("response:",response.json())
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    else:
        return None 
    
if __name__ == "__main__":
    while True:
        city = input("Enter a city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye! ☀️")
            break
        print(get_weather(city))