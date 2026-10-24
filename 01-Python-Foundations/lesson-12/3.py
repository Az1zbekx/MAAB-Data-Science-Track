import requests
import json

url = "https://api.demoblaze.com/bycat"
payload = {"cat": "notebook"} 
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

laptops = []

for item in data["Items"]:
    laptop = {
        "name": item["title"],
        "price": item["price"],
        "description": item["desc"]
    }
    laptops.append(laptop)


with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=4, ensure_ascii=False)

print("Laptops data saved to laptops.json")
