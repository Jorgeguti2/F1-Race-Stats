# Notes:
    # React Frontend
    # Django Backend
    # SQLite
    # SSRS

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

# Create a dictionary to store year as the keys and (grand prix, date, winner, car, laps, time) as values
years_winner_data = {}

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
    tmp_list = []
    # Need to optimize this after :(
    for i in trs:
        tr = list(i)
        tmp_list2 = []
        grand_prix = tr[0].text
        tmp_list2.append(grand_prix)
        date = tr[1].text
        tmp_list2.append(date)
        winner = (tr[2].text)[:-3]
        tmp_list2.append(winner)
        car = tr[3].text
        tmp_list2.append(car)
        laps = tr[4].text
        tmp_list2.append(laps)
        time = tr[5].text
        tmp_list2.append(time)
        tmp_list.append(tmp_list2)

    years_winner_data[year] = tmp_list

print(years_winner_data)
