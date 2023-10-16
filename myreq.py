import requests
from bs4 import BeautifulSoup

def myreq(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'lxml')

def req_by_num(num):
    url = f"https://sea.dragonnest.com/news/notice/all/{num}"
    soup = myreq(url)
    return soup.find_all("div", {"class": "cont"})[0]

def notive_all():
    url = 'https://sea.dragonnest.com/news/notice/all'
    soup = myreq(url)
    return [num.text for num in soup.find_all("td", {"class": "num"})]

def my_soup(soup):
    content = soup.text
    content = content.replace("\xa0", "")
    content = content.replace("\n\n\n\n", "\n\n")
    content = content.replace("\n\n\n", "\n\n")
    return content[2:-1]


