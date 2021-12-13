import json

import requests

API_KEY='ad5d3955dacd1dc8af3c20dbedd8954e'




def getweather(cityname):

    response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY}")
    #print(response.json())
    response_dict=response.json()
    return(response_dict['weather'][0]['main'])
    #return(response_dict['weather'])


#print(getweather('america'))