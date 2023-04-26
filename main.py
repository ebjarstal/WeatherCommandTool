import requests
import config

# API key from OpenWeatherMap
api_key = config.api_key

base_url = "https://api.openweathermap.org/data/2.5/weather?q="

if __name__ == "__main__":
    city_name = input("Enter city name : ")
    complete_url = base_url + city_name + "&appid=" + api_key

    response = requests.get(complete_url)

    data = response.json()

    # Checks if response contains weather data
    if data["cod"] != "404":
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"]-273.15, 0)
        humidity = data["main"]["humidity"]

        print("Weather:", weather)
        print("Temperature:", temperature, "C")
        print("Humidity:", humidity, "%")

    else:
        print(data["message"])
