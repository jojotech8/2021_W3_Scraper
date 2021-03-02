import requests
from bs4 import BeautifulSoup

def scape_sportsrecreation(url):
    page_html = requests.get(url)
    html_soup = BeautifulSoup(page_html.text, 'html.parser')
    sport_items = html_soup.find_all('li', class_="premium")
    sportsList = []

    for sports in sport_items:
        #title = sports.find('div', class_="premium_text").text
        address = sports.find('div', class_="listing_content").text
        telephone = sports.find('li', class_="more_info").text
        sportsList.append([address, telephone])
        print(str(address) + str(telephone))
    return sportsList

scape_sportsrecreation("https://www.nzdirectory.co.nz/sport-recreation.html")