# Import all needed libraries
from bs4 import BeautifulSoup
import requests
from datetime import datetime

# Get the current year
    # Note: we do this because the website updates the href every year with the current year
now = datetime.now()
current_year = now.year

# Get to the Drivers' Results page
drivers_URL = f"https://www.formula1.com/en/results/{current_year}/drivers"
drivers_page = requests.get(drivers_URL).text
drivers_doc = BeautifulSoup(drivers_page, "html.parser")

# Get all F1 Racing Season Years
years_table = drivers_doc.find_all(attrs={'data-name': 'year'})

# Go year by year, driver by driver, grabbing all information (Grand Prix, Date, Car, Race Position, PTS)
# Note: this gets all time career stats for each driver for each race and year
    # Other Note: need to optimize :(((((
for i in years_table:
    year = i.text
    url = f"https://www.formula1.com/en/results/{year}/drivers"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    drivers = doc.find_all(attrs={'data-name': 'drivers'})
    for driver in drivers:
        driver_href = driver.find('a', href=True)
        driver_URL = f"https://www.formula1.com{driver_href['href']}"
        driver_page = requests.get(driver_URL).text
        driver_doc = BeautifulSoup(driver_page, "html.parser")
        tbody = driver_doc.find("tbody")
        trs = tbody.contents
        for i in trs:
            tr = list(i)
            grand_prix = tr[0].text
            date = tr[1].text
            car = (tr[2].text)[:-3]
            pos = tr[3].text
            pts = tr[4].text
            print(driver.text, grand_prix, date, car, pos, pts)
        print()
    print()
