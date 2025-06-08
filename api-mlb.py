import requests
url = "https://data.nba.net/10s/prod/v1/today.json"
response = requests.get(url)
data = response.json()
print(data)