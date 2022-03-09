import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/newauto/marka-jeep/'
HEADERS = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70', 
    'accept' : '*/*'
}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r 

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_="proposition_link")
  
    cars = []
    for item in items:
        cars.append({
            'title' : item.find('div', class_="proposition_title").get_text(strip=True),
            'link' : item.find('a', class_="proposition_link").get('href'),
        })
        print(cars)
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error")

parse()