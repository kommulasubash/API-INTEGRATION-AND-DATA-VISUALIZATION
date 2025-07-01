import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Input: city name
city = input("Enter a city name: ")

# API setup
api_key = "3bda07ff829d628dc16426fe045f1397"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# API call
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    # Extract required weather metrics
    weather_data = {
        "Temperature (°C)": data['main']['temp'],
        "Feels Like (°C)": data['main']['feels_like'],
        "Humidity (%)": data['main']['humidity'],
        "Pressure (hPa)": data['main']['pressure'],
        "Wind Speed (m/s)": data['wind']['speed']
    }

    print(f"\nWeather Summary for {city.title()}:")
    for k, v in weather_data.items():
        print(f"{k}: {v}")

    # Visualization using matplotlib and seaborn
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(weather_data.keys()), y=list(weather_data.values()), palette="Blues_d")
    plt.title(f"Current Weather Metrics for {city.title()}", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print("Error fetching data. Please check the city name or your API key.")
