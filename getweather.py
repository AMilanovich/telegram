import requests


API = "http://api.openweathermap.org/data/2.5/weather?q=Minsk,blr&APPID=e876f3b4b56e27cfc2fa61e94bcf3fb2"

response = requests.get(API)
if response.ok:
    data = response.json()

print(data)
