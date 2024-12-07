import requests

API_KEY = '93980c5df83ff5b63ff872da7dd478ea'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
def kelvin_to_celsuis(tempK):
        tempCelsius = tempK -273.15
        return round(tempCelsius)


def get_weather(city):
    try:
        # Construct the API URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}"
        
        response = requests.get(url)
        response.encoding = 'utf-8'  # Ensure UTF-8 encoding
        data = response.json()
        print(data)
        # Check for API errors
        if data['cod'] != 200:
            print(f"Error: {data['message']}")
            return

        
       # Extract and display relevant weather data
        
        weather = data['weather'][0]['description']
        temp_kelvin = data['main']['temp']
        feels_like_kelvin = data['main']['feels_like']

        temp_celsius = kelvin_to_celsuis(temp_kelvin)
        feel_like_celsius = kelvin_to_celsuis(feels_like_kelvin)
        print(f"Weather in {city}:")
        print(f"  Description: {weather.capitalize()}")
        print(f"  Temperature: {temp_celsius}°C (Feels like: {feel_like_celsius}°C)")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main loop to get input and display weather
while True:
    city = input("Enter city name (or type 'exit' to quit): ")
    if city.lower() == 'exit':
        print("Goodbye!")
        break
    
    get_weather(city)



