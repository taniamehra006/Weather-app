import requests 

API_KEY = "abs.api"

city = input("Enter you city name:-")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if data["cod"] != 200:
    print("❌ City not found!")
else:
    city = data["name"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n------ Weather Report ------")
    print("City        :", city)
    print("Temperature :", temperature, "°C")
    print("Feels Like  :", feels_like, "°C")
    print("Humidity    :", humidity, "%")
    print("Weather     :", weather)
    print("Description :", description)
    print("Wind Speed  :", wind_speed, "m/s")