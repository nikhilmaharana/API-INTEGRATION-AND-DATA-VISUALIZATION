import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

API_KEY = ""  # My API KEY, I Can's Expose here

cities = ["Bhubaneswar", "Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore", "Hyderabad"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data.get("main", {})
        temp = main.get("temp")
        humidity = main.get("humidity")
        pressure = main.get("pressure")
        return {
            "City": city,
            "Temperature (°C)": temp,
            "Humidity (%)": humidity,
            "Pressure (hPa)": pressure
        }
    else:
        print(f"❌ Error fetching data for {city}: {response.json().get('message')}")
        return None

weather_data = []

for city in cities:
    result = fetch_weather(city)
    if result:
        weather_data.append(result)

if weather_data:
    df = pd.DataFrame(weather_data)
    print("\n--- Weather Data ---\n")
    print(df)

    plt.figure(figsize=(12, 6))
    sns.barplot(x="City", y="Temperature (°C)", data=df, palette="coolwarm")
    plt.title("Current Temperature in Indian Cities")
    plt.ylabel("Temperature (°C)")
    plt.xlabel("City")
    plt.show()
else:
    print("⚠️ No weather data available to display.")
