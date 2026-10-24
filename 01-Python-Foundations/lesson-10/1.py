import requests

Api_key = "531df4d106e33a49e21eff859031383c"
city = "Tashkent"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("Shahar:", data["name"])
print("Havo harorati:", data["main"]["temp"], "°C")
print("Bosim:", data["main"]["pressure"], "hPa")
print("Namlik:", data["main"]["humidity"], "%")
print("Ob-havo:", data["weather"][0]["description"])
