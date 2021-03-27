import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
    print(words)
    os.system("say " + words)

talk("Привет! Спроси меня что нибудь")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-нибудь")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + task)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        task = command()

    return task

def makeSomething(task):
    if 'открыть веб-сайт' in task:
        talk("Уже открываю")
        url = 'https://google.com'
        webbrowser.open(url)
    elif 'стоп' in task:
        talk("Хорошо! Конечно")
        sys.exit()
    elif 'имя' in task:
        talk("Меня зовут сири!")
    elif 'погода в москве' in task:
        talk("Уже ищу погоду в москве")
        import requests
        s_city = "Moscow, RU"
        city_id = 524901
        appid = "7fc48d355390dd501686310d0604be52"
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            print("conditions:", data['weather'][0]['description'])
            print("temp:", data['main']['temp'])
            print("temp_min:", data['main']['temp_min'])
            print("temp_max:", data['main']['temp_max'])
        except Exception as e:
            print("Exception (weather):", e)
            pass
    elif 'погода в харькове' in task:
        talk("Уже ищу погоду в харькове")
        import requests
        s_city = "Kharkiv, UA"
        city_id = 706483
        appid = "7fc48d355390dd501686310d0604be52"
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            print("conditions:", data['weather'][0]['description'])
            print("temp:", data['main']['temp'])
            print("temp_min:", data['main']['temp_min'])
            print("temp_max:", data['main']['temp_max'])
        except Exception as e:
            print("Exception (weather):", e)
            pass
while True:
    makeSomething(command())