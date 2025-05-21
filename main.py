import requests
import matplotlib.pyplot as plt

def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def plot_weather_data(data):
    metrics = {
        "Temperature (°C)": data["main"]["temp"],
        "Humidity (%)": data["main"]["humidity"],
        "Wind Speed (m/s)": data["wind"]["speed"]
    }
    plt.figure(figsize=(8, 5))
    plt.bar(metrics.keys(), metrics.values(), color=["blue", "green", "orange"])
    plt.title(f"Weather Data for {data['name']} ({data['weather'][0]['description'].capitalize()})")
    plt.ylabel("Value")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("weather_visualization.png")
    plt.show()

def main():
    API_KEY = "3f19a7fd08370577lll704e5aafb1db1"
    city = input("Enter city name: ").strip()
    data = get_weather_data(city, API_KEY)
    if data and data.get("cod") == 200:
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Condition: {data['weather'][0]['description'].capitalize()}")
        plot_weather_data(data)
    else:
        print("Could not fetch weather data. Please check the city name or API key.")

if __name__ == "__main__":
    main()
