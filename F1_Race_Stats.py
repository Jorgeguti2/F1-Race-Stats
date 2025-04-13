# Import all needed libraries
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

# Get the current year
    # Note: we do this because the website updates the href every year with the current year
now = datetime.now()
current_year = now.year

# Navigate to the Results page from the HomePage
homepage_URL = f"https://www.formula1.com/"
homepage = requests.get(homepage_URL).text
homepage_doc = BeautifulSoup(homepage, "html.parser")

results_URL = homepage_doc.find(href=f"https://www.formula1.com/en/results/{current_year}/races").get("href")
results_page = requests.get(results_URL).text
results_doc = BeautifulSoup(results_page, "html.parser")

# Get all F1 Racing Season Years
years_table = results_doc.find_all(attrs={'data-name': 'year'})


