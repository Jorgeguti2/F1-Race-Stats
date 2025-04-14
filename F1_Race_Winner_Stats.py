# Notes:
    # 1. SQLite
    # 2. Django Backend
    # 3. React Frontend
    # 4. SSRS

# Import all needed libraries
from bs4 import BeautifulSoup
import requests
from datetime import datetime

# Get the current year
    # Note: we do this because the website updates the href every year with the current year
now = datetime.now()
current_year = now.year

# Get to the Results page
results_URL = f"https://www.formula1.com/en/results/{current_year}/races"
results_page = requests.get(results_URL).text
results_doc = BeautifulSoup(results_page, "html.parser")

# Get all F1 Racing Season Years
years_table = results_doc.find_all(attrs={'data-name': 'year'})

# Go year by year grabbing all information (Grand Prix, Date, Winner, Car, Laps)
    # Note: this is only getting winner information of all grand prixes, need to get
    #       overall data for each individual driver next
for i in years_table:
    year = i.text
    url = f"https://www.formula1.com/en/results/{year}/races"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    tbody = doc.find("tbody")
    trs = tbody.contents
    # Need to optimize this after :(
    for i in trs:
        tr = list(i)
        grand_prix = tr[0].text
        date = tr[1].text
        winner = (tr[2].text)[:-3]
        car = tr[3].text
        laps = tr[4].text
        time = tr[5].text
        print(grand_prix, date, winner, car, laps, time)

    print()
