from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as up

url = 'https://en.wikipedia.org/wiki/Frank_Abagnale'

uClient = up(url)
html = uClient.read()
uClient.close()

soup_html = bs(html, "html.parser")

scpe = soup_html.findAll("th",{"scope":"row"})

print(soup_html.title.string)
print(len(scpe))