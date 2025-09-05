
import requests
import time

lat = 52.3083875
lon = 4.7639984
# lat = 53.219383
# lon = 6.566502 # Groningen
api_key = "e7370d7beb124310f455c7c769a1f6f2"

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)

    return response.text

if __name__ == "__main__":
    with open("weather_data.txt", 'a') as wf:
        while True:
            weather_data = get_weather()
            wf.write(weather_data)
            wf.write("\n")
            time.sleep(1)