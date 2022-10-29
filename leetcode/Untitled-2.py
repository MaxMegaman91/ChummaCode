import requests
from bs4 import BeautifulSoup

songname="in my head"
html_file=requests.get("https://search.azlyrics.com/search.php?q="+songname).text
soup=BeautifulSoup(html_file,"lxml")
match=[x.extract() for x in soup.findAll('td',class_='text-left visitedlyr')]
link=str(list(match[0])[1]).split('"')

html_files=requests.get(link[1]).text
soup=BeautifulSoup(html_files,"lxml")
match=[x.extract() for x in soup.findAll('div',class_='col-xs-12 col-lg-8 text-center')]

lyrics=str(match).split("\n")
start=lyrics.index('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->\r')
end=lyrics.index('<!-- MxM banner -->')
print(lyrics[start+1:end-2])

for i in lyrics[start+1:end-2]:
    f=i.replace("<br/>","")
    print(f)