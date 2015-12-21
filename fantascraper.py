import ConfigParser
import requests
import sys
import urllib

from mechanize import Browser
from BeautifulSoup import BeautifulSoup
from selenium import webdriver

conf = ConfigParser.ConfigParser()
conf.read('fantascraper.conf')

usernm = conf.get('config', 'username')
passwd = conf.get('config', 'password')
leagueid = conf.get('config', 'leagueid')
team_name = str(sys.argv[1])

session = requests.session()
login_data = dict(username=usernm, password=passwd)
session.post('https://www.fantrax.com/login.go', data=login_data)

mech = Browser()
url = 'http://www.fantrax.com/fantasy/standings.go?leagueId={}'.format(leagueid)
page = mech.open(url)
html = page.read()
soup = BeautifulSoup(html)

driver = webdriver.Firefox()
driver.get(url)

teamnm = driver.find_element_by_xpath('//*/td[@class="team"]*/')
spreadsheet = driver.find_element_by_link_text('Download Spreadsheet')

teamnm.click()
spreadsheet.click()

















# kill all script and style elements
#for script in soup(["script", "style"]):
#    script.extract()    # rip it out

#table = soup.find("table", {"id":"rosterTable_5010"})
#rows = table.findChildren(['tr'])

#for row in rows:
#    players = row.findChildren(['a'])
#    for player in players[0]:
#        print player
