#!/usr/bin/env python

import sys
import argparse

from mechanize import Browser
from slackclient import SlackClient
from configparser import ConfigParser
from BeautifulSoup import BeautifulSoup

# Weird names in EPL from other alphabets
reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="Specify config file location", default="physioroom.conf", dest='conf_file')
parser.add_argument("-t", "--team", help="Specify team file location", default="team.csv", dest='team_file')
parser.add_argument("--version", help="Print version", action="version", version="%(prog)s 0.5.0-beta")
args, remaining_argv = parser.parse_known_args()

team_file = args.team_file
conf_file = args.conf_file
conf = ConfigParser()
conf.read([conf_file])
slack_channel = conf.get('slack', 'channel_id')
slack_token = conf.get('slack', 'token')

slack_client = SlackClient(slack_token)
teams = ["Arsenal", "Liverpool", "Manchester City", "West Bromwich Albion", "Tottenham Hotspur", "Middlesbrough", "Burnley", "Swansea City", "Manchester United", "Crystal Palace", "Chelsea", "Bournemouth", "Leicester City", "Everton", "Southampton", "Stoke City", "Watford", "Hull City", "West Ham United", "Sunderland"]

mech = Browser()
url = 'http://www.physioroom.com/news/english_premier_league/epl_injury_table.php'
page = mech.open(url)
html = page.read()
soup = BeautifulSoup(html)

def send_message(channel_id, message):
    """ Post injured list to slack """
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='Injurybot',
        icon_emoji=':hospital:'
    )

def get_team(team_file):
    """ Get list of players on our team """
    players = []
    with open(team_file) as team:
        for player in team:
            player = player.replace('\\','')
            players.append(player.rstrip())
    return players

def get_epl_injured():
    """ Get a list of all the injuries in the EPL """
    epl_injured = []
    for row in soup.find('table', {'id':'epl-table'}).tbody.findAll('tr'):
        for guy in row.find('a'):
            if guy in teams:
                break
            else:
                epl_injured.append(str(guy.lower()))
    return epl_injured

def check_players(players, epl_injured):
    """ Check if anyone on our team is injured """
    injured = []
    for player in players:
        if player.lower() in epl_injured:
            injured.append(player)
    return injured

if __name__ == '__main__':
    team = get_team(team_file)
    epl = get_epl_injured()
    injured = check_players(team, epl)
    if injured:
        send_message(slack_channel, "The following players are injured:")
        for player in injured:
            send_message(slack_channel, player)
    else:
        send_message(slack_channel, "Nobody is listed as injured")
