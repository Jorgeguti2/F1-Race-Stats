# Import all needed libraries
from bs4 import BeautifulSoup
import requests
import re
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
for i in years_table:
    print(i.text)
# Go year by year grabbing all information (Grand Prix, Date, Winner, Car, Laps)

