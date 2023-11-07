import requests
import time
import sys
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QMessageBox, QApplication

def myreq(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'lxml')

def req_by_num(num):
    url = f"https://sea.dragonnest.com/news/notice/all/{str(num)}"
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

def popup():
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("This is the main text!")
    msg.show()
    app.exec()

def test():
    while True:
        if "Game service resumed" in my_soup(req_by_num(1128)):
            popup()
        print('Check')
        time.sleep(1*60)


if __name__ == "__main__":
    test()
