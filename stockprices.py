import requests
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
API_KEY='lY64JAv5_d6GfRletlQ3OiBukMCQC8_F'
GOOGLE_API_KEY='AIzaSyDqONh-h_eUK8bSPRWVtzG-y-XSaPHTPdY'

def getStock_price(stockname):
    response = requests.get('https://financialmodelingprep.com/api/v3/quote-short/'+stockname+'?apikey='+API_KEY)
    print(response.content)
    return response
getStock_price('AADI')