import eel  
import pyowm
import sys

eel.init("web")



owm=pyowm.OWM('db18ce8879e038232079d0f23309504d')
@eel.expose
def get_weather(city):
    mgr=owm.weather_manager()
    observation=mgr.weather_at_place()
    w=observation.weather
    temp=w.temperature('celsius')['temp']
    return "в городе "+ city + " сейчас "+ str(temp) + " градусов "
 
eel.start("main.html", size=(700, 700))



