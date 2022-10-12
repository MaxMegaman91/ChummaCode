from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.icc-cricket.com/rankings/mens/player-rankings/4029"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")


        

# <div class="rankings-player-bio__name-wrapper">
# <div class="rankings-player-bio__info">
# 

def write():
    with open("read.txt", "w") as f:
        f.write(html)

write()

soup = BeautifulSoup(html,"html.parser")

print(soup.find_all(attrs={"class": "player-profile-header__title"}))
print(soup.find_all(attrs={"class": "player-profile-header__meta-text"}))
# print(soup.find_all(attrs={"class": "player-profile-header__meta-text"}))
