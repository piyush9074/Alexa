import requests
from bs4 import BeautifulSoup

URL = "https://www.androidauthority.com/news"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

article_titles = soup.find_all('div', class_='rc')


def getheadlines():
    headlines = ""
    for text in article_titles:
        headlines += str(text.text) + ".....\n\n"

    return headlines


getheadlines()
# print(soup.prettify())


# with open('home.html', 'r') as html_file:
#     content=html_file.read()
#
#     soup=BeautifulSoup(content, 'lxml')
#     course_names=soup.find_all('h5')
#     for i in course_names:
#         print(i.text)
