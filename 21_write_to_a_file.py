import requests
from bs4 import BeautifulSoup

r = requests.get(r'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
soup = BeautifulSoup(r.text,'html.parser')

headline = soup.find('h1',class_='hed').text
print(headline)

summary = soup.find('div',class_='dek').text
print(summary)

text = [a.text for a in soup.find_all('p')]
# print('\n'.join(text))

with open('test.txt','w') as f:
    f.write(headline+'\n')
    f.write(summary+'\n')
    f.write('\n'.join(text))