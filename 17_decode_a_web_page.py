import requests
from bs4 import BeautifulSoup
import re

def main():
    request = requests.get('http://www.nytimes.com/')
    soup = BeautifulSoup(request.text,'html.parser')
    
    titles = soup.findAll(re.compile(r'h*'),'story-heading')
    titles = [title.string.strip() for title in titles if type(title.string) != type(None)]
    
    print('\n'.join(titles))


if __name__ == '__main__':
    main()
