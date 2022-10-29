import lxml
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

#headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mozili/15E148"}

header = {"User-Agent": UserAgent().random}

r = requests.get('https://www.imdb.com/name/nm0000245/?ref_=nv_sr_srsg_0', headers=header).text
#print(r)

#r = requests.get('https://www.imdb.com/name/nm0634240/?ref_=fn_al_nm_1').text

soup = BeautifulSoup(r, 'lxml')

title = soup.find('title')
print(title.text)

mn = soup.find('div', class_='inline')
print(mn.text)

knownfor = []
for i in soup.find_all('div', class_='knownfor-title'):
    knownfor.append(i.text.replace('\n', ''))
print(knownfor)


movies = []
filmography = soup.find('div', class_='filmo-category-section')
for movie in filmography.find_all('div', class_='filmo-row odd') and filmography.find_all('div', class_='filmo-row odd'):
    movies.append(movie.text)
print(movies)
