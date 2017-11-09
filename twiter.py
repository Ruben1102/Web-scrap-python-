from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as up

url = 'http://garage4hackers.com/content.php?r=176-Indian-Hackers-Infosec-guys-groups-you-should-be-following-in-Twitter'

uClient = up(url)
html = uClient.read()
uClient.close()

soup_html = bs(html, "html.parser")

scpe = soup_html.findAll("table",{"class":"cms_table_grid"})
scp = soup_html.findAll("tr",{"class":"cms_table_grid_tr"})
# print(soup_html.title.string)
# print(scp[0].a["href"])

file_name = "twiter.txt"
f = open(file_name, "w")
header = "twitter accounts to foll0w:\n \n"
f.write(header)
for sc in scp:
	td = sc.b
	tw = sc.a["href"]
	f.write("   " + td.text.strip() + ":  " +tw +"\n \n")
f.close()