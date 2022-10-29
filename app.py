import lxml
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

#headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mozili/15E148"}

header = {"User-Agent": UserAgent().random}

r = requests.get('https://www.imdb.com/name/nm0634240/?ref_=fn_al_nm_1', headers=header).text()
#print(r)

soup = BeautifulSoup(r, 'lxml')