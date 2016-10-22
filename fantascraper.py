#!/usr/bin/env python

import csv
import sys
import argparse
import requests

from mechanize import Browser
from configparser import ConfigParser
from BeautifulSoup import BeautifulSoup

# Weird names in EPL from other alphabets
reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="Specify config file location", default="fantascraper.conf", dest='conf_file')
parser.add_argument("-t", "--team", help="Specify team file location", default="team.csv", dest='team_file')
parser.add_argument("--version", help="Print version", action="version", version="%(prog)s 0.1.0-alpha")
args, remaining_argv = parser.parse_known_args()

team_file = args.team_file
conf_file = args.conf_file
conf = ConfigParser()
conf.read([conf_file])
league_id = conf.get('config', 'league_id')
team_id = conf.get('config', 'team_id')

roster_table_outfield = 'rosterTable_5010'
roster_table_keepers = 'rosterTable_5020'
mech = Browser()
url = 'http://www.fantrax.com/newui/fantasy/teamRoster.go?teamId={}&leagueId={}&isSubmit=y'.format(team_id,league_id)
page = mech.open(url)
html = page.read()
soup = BeautifulSoup(html)

players = []

def rename_player(first, last):
    player = first[:1], last
    players.append(player)
    return players

def find_players(soup, roster_table):
    player_table = soup.find('table', {'id':roster_table})
    for row in player_table.findAll('tr'):
        names = row.findAll('a', {'class': 'hand '})
        for name in names:
            if name.find('img'):
                continue
            else:
                if ',' not in name.string:
                    if ' ' not in name.string:
                        player = name.string,
                        players.append(player)
                    else:
                        first, last = name.string.split(' ')
                        rename_player(first, last)
                else:
                    last, first = name.string.split(', ')
                    rename_player(first, last)
    return players

def write_players(players, team_file):
    with open(team_file, 'wb') as team:
        f = csv.writer(team,delimiter=' ')
        for player in players:
            f.writerow(player)

if __name__ == '__main__':
    find_players(soup, roster_table_outfield)
    find_players(soup, roster_table_keepers)
    write_players(players, team_file)
