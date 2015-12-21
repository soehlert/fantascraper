import requests
import sys

from mechanize import Browser
from BeautifulSoup import BeautifulSoup

full_name = str(sys.argv[1])
first_name, last_name = full_name.split(' ', 1)
first_initial = first_name[0]
player_name = " ".join([first_initial, last_name])

session = requests.session()
response = session.get('http://www.physioroom.com/news/english_premier_league/epl_injury_table.php')

mech = Browser()
url = 'http://www.physioroom.com/news/english_premier_league/epl_injury_table.php'
page = mech.open(url)

html = page.read()
soup = BeautifulSoup(html)

injured = False
for row in soup.find('table', {'id':'epl-table'}).tbody.findAll('tr'):
    for player in row.find('a'):
        if player_name.lower() in player.lower():
            print "{} {} is injured".format(first_name, last_name)
            injured = True
            break

if not injured:
    print "{} {} is not injured".format(first_name, last_name)
