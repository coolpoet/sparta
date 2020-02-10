import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta                      


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://studypie.co/ko',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')


studies = soup.select('body > main > section:nth-child(2) > div > section')
print(studies)