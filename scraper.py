import re
import requests
from bs4 import BeautifulSoup


#URL = "https://realpython.github.io/fake-jobs/"
URL = "https://www.maxpreps.com/print/schedule.aspx?schoolid=adc0c0d1-7886-4994-9f44-89d040e8415d&ssid=94be351a-c29f-4add-839c-4236b8d04b7c"
#URL = "https://nazarethathletics.bigteams.com/main/teamschedule/id/3620975/seasonid/4756168"
page = requests.get(URL, verify=False)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="schedule")

event_elements = results.find_all("tr", class_=re.compile("dual-contest$"))

for event_element in event_elements:
    print (event_element, end="\n"*2)