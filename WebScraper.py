import requests
from bs4 import BeautifulSoup

my_file = open("ScraperOutput.txt", "w")
my_file = open("ScraperOutput.txt", "a")


def write(data):
	my_file.write(str(data) + "\n" + "\n")


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

#write(soup.prettify())
#write(list(soup.children))

stuff = [type(item) for item in list(soup.children)]
#write(stuff)

html = list(soup.children)[2]
#write(html)

body = list(html.children)[3]
#write((list(body.children)))

p = list(body.children)[1]
#write((list(p)))
#write(p.get_text())

write(soup.find_all('p')[0].get_text())









my_file.close()