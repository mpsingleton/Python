import requests
from bs4 import BeautifulSoup
#import pandas as pd

my_file = open("ScraperOutput.txt", "w")
my_file = open("ScraperOutput.txt", "a")


def write(data):
	my_file.write(str(data) + "\n" + "\n")


page = requests.get("https://forecast.weather.gov/MapClick.php?textField1=33.05&textField2=-97.02")
soup = BeautifulSoup(page.content, "html.parser")
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

write(short_descs)
write(temps)
write(descs)




#this part doesn't work without installing pandas, which I'm not up to at the moment.
# weather = pd.dataframe({
# 		"period": periods,
# 		"short_desc": short_descs,
# 		"temp": temps,
# 		"desc": descs
# 	})




# period = tonight.find(class_="period-name").get_text()
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()

# img = tonight.find("img")
# desc = img["title"]


# write(period)
# write(short_desc)
# write(temp)
# write(desc)

# img = tonight.find("img")
# desc = img("title")

# page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# soup = BeautifulSoup(page.content, 'html.parser')

# p_tags = soup.find_all('p', class_='outer-text')
# write(p_tags)




#write(soup.prettify())
#write(list(soup.children))

#stuff = [type(item) for item in list(soup.children)]
#write(stuff)

#html = list(soup.children)[2]
#write(html)

#body = list(html.children)[3]
#write((list(body.children)))

#p = list(body.children)[1]
#write((list(p)))
#write(p.get_text())

#write(soup.find_all('p')[0].get_text())



my_file.close()