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


