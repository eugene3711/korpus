import requests
from datetime import datetime

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

url = 'http://api.openweathermap.org/data/2.5/forecast?q=chelyabinsk,ru&units=metric&mode=json&APPID=74ca83beeee5d7e15167c1608b40f2b4'

json_data = requests.get(url).json()
print(json_data)

ts = int(json_data['list'][0]['dt']+3600*5)
print(ts)
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
for i in range(len(json_data['list'])):
    ts = int(json_data['list'][i]['dt']+3600*5)
    print(datetime.utcfromtimestamp(ts).strftime('%a %Y-%m-%d %H:%M:%S'))
    print ('Температура воздуха {} *C'.format(json_data['list'][i]['main']['temp']))