import requests

url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url)
total_records = response.json().get("count")

print(total_records)

all_data = []

for i in range(0,total_records,20):
    paginated_url = f"{url}?offset={i}&limit=20"
    response = requests.get(paginated_url)
    data = response.json()
    all_data.append(data)

print(len(all_data))    