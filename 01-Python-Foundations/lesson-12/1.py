from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

rows = soup.find("tbody").find_all("tr")

days = []
maxt = 0

for row in rows:
    data = row.find_all("td")
    d = data[0].text
    t = int(data[1].text.replace("°C", ""))
    c = data[2].text
    maxt = max(t, maxt)
    days.append([d, t, c])
print("Weather Forecast:")
for d, t, c in days:
    print(f"{d}: {t}°C, {c}")
print("The hottest days")
for d, t, c in days:
    if t == maxt:
        print(f"{d}: {t}°C, {c}")
print("Sunny days")
for d, t, c in days:
    if c == "Sunny":
        print(f"{d}: {t}°C, {c}")

T = sum(t for d, t, c in days) / len(days)
print("Average temperature:", round(T, 2), "°C")
