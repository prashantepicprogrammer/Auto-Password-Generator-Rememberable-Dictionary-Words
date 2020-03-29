# install requests
# install bs4

import requests
import bs4
import random

res = requests.get('https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/')
soup = bs4.BeautifulSoup(res.text,'lxml')
data = soup.select('p')
words = data[1].text.split()
# print(words)

def password_generator():
    password = str()
    one = random.randint(0,5)
    strong_texts = '1234567890!@#$%&*()'
    for i in range(one):
        password = password + random.choice(strong_texts)
    password = password + random.choice(words)
    two = random.randint(0,5)
    for i in range(two):
        password = password + random.choice(strong_texts)
    print(password)

password_generator()

