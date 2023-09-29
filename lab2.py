import requests
city = "Moscow,RU"
appid = "57b1d1fe41ea370a5cdb80497fc974f6"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q':city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print('Город: ', city)
print('Погодные условия: ', data['weather'][0]['description'])
print('Температура: ', data['main']['temp'])
print('Минимальная температура', data['main']['temp_min'])
print('Максимальная температура', data['main']['temp_max'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q':city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print('Прогноз погоды на неделю')
for i in data['list']:
    print("Дата <", i['dt_txt'], ">\r\nСкорость ветра в М/С <",
          i['wind']['speed'], ">")
    print("Видимость <",
          i['visibility'], ">")
    print("_______________")
    break