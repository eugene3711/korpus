import requests
from datetime import datetime

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

url = 'http://api.openweathermap.org/data/2.5/forecast?q=chelyabinsk,ru&units=metric&mode=json&APPID=74ca83beeee5d7e15167c1608b40f2b4'

def unique(list): 
    unique_list = [] 
   
    for x in list: 
        if x not in unique_list: 
            unique_list.append(x)
    return unique_list
         

json_data = requests.get(url).json()

sundayTemp = []

for i in range(len(json_data['list'])):
    timestamp = int(json_data['list'][i]['dt']+3600*5)
    fullDate = datetime.utcfromtimestamp(timestamp).strftime('%a %Y-%m-%d %H:%M:%S') 
    if (fullDate[:3]=='Sun'):
        temp = int(json_data['list'][i]['main']['temp'])
        sundayTemp.append(temp)
        print ('Температура воздуха {}* C'.format(temp))

if sundayTemp == 0:
    print("Прогноз дается лишь на 5 дней, подождите до вторника")
    input()
    quit()

sundayTemp = sundayTemp[2:6]
print(sundayTemp)
temp= [min(sundayTemp), max(sundayTemp)]
temp.append((temp[0]+temp[1])/2)
print(temp)

lubricants = [] # Type A,B,C 
for i in temp: # от -13 до -5 расстояние 7 градусов
    if i<-13:
        lubricants.append("Type C")
    elif i>-13 and i<-5:
        lubricants.append("Type B")
    else:
        lubricants.append("Type A")

lubricants = unique(lubricants)
print(lubricants)

if len(lubricants) == 1:
    print ("Ожидается температура от {}* С до {}* C, лучше взять смазку {}".format(min(sundayTemp),max(sundayTemp),lubricants[0]))
elif len(lubricants) == 2:
    print ("Ожидается температура от {}* С до {}* C, лучше взять смазки {} и {}".format(min(sundayTemp),max(sundayTemp),lubricants[0],lubricants[1]))
elif len(lubricants) == 3:
    print ("Ожидается температура от {}* С до {}* C, лучше взять смазки {} и {} и даже {}".format(min(sundayTemp),max(sundayTemp),lubricants[0],lubricants[1],lubricants[2]))


#a) если температура воздуха -13 градусов Цельсия и холоднее рекомендуйте покупать смазку “Type C”.
#b) Если от -13 до -5, то подойдет “Type B”.
#c) Если теплее -5, то только “Type A”
