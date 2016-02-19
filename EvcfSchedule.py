import urllib
from bs4 import BeautifulSoup

url = 'https://eastvalleycrossfit.sites.zenplanner.com/calendar.cfm'
page = urllib.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

todayList = soup.find("td", { "class" : "today" }).text

print todayList



