import urllib
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)

@app.route('/schedule')
def getTodaysSchedule():
    url = 'https://eastvalleycrossfit.sites.zenplanner.com/calendar.cfm'
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    todayList = soup.find("td", { "class" : "today" }).text
    todayList = todayList.replace(" ", "\n")
    return todayList, 200, {'Content-Type': 'text/css; charset=utf-8'}

@app.route('/workouts')
def getWorkouts():
    list = ""
    url = 'http://eastvalleycrossfit.com/'
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    fullList = soup.find_all("div", { "class" : "hentry" })
    for entry in fullList:
        list += entry.text
        # print(entry.text)
    return list, 200, {'Content-Type': 'text/css; charset=utf-8'}

if __name__ == '__main__':
    app.run()

# list = ""
# url = 'http://eastvalleycrossfit.com/'
# page = urllib.urlopen(url)
# soup = BeautifulSoup(page, "html.parser")
# fullList = soup.find_all("div", { "class" : "hentry" })
# for entry in fullList:
#     list += entry.text
# print(list)



