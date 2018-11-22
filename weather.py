import requests
endpoint = "https://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"53e09c00e33b84ed98ba9f9f619d8e37"}
response = requests.get(endpoint, params=payload)

data = response.json()

#print data["main"]
temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print "It's {temperature}C in {name}, and the sky is {weather}".format(temperature, name, weather)
#print response.url
#print response.status_code
#print response.headers["content-type"]
#print response.text