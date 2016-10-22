# Fantascraper
General scripts for fantasy EPL

Fantascraper.py is pretty much nonfunctional at the moment.

physioroom.py works.

### Prereqs

1. python
2. pip
3. virtualenv (optional, but suggested)

Use pip to install required pip packages
```
$ pip install -r requirements.txt
```

### Configuration

```
$ git clone https://github.com/soehlert/fantascraper.git
```

Replace team.txt with a file full of your players (One player per line, first initial and last name):

```
H Kane
E Dier
```

Edit the .conf file by entering a channel id and a token.

To get the channel id (works with public, private or DMs), go to [groups.list page](https://api.slack.com/methods/groups.list/test) if you want to use a private room, [IMs list page](https://api.slack.com/methods/im.list/test) if you want to use a DM though you'll have to figure out user id numbers, or [channels list page](https://api.slack.com/methods/channels.list/test) to use a public room. Once on the page, click `Test method` and then search for the room you want.

To get a token, go to [this page](https://api.slack.com/web) and click `Generate test tokens` This is a little dirty to use test tokens like this, but I don't wanna figure out how to make it an app just yet.

### Usage

```
usage: physioroom.py [-h] [--version] [-c CONF_FILE] [-t TEAM_FILE]

optional arguments:
  -h, --help                        show this help message and exit
  --version                         Print version
  -c CONF_FILE, --config CONF_FILE  Specify config file location
  -t TEAM_FILE, --team TEAM_FILE    Specify team file location
```

That should get you able to run the script once through no problem. If you'd like to set it to run on a schedule (once a day? once a week before the games start?), you'll need to use cron or something similar. (No promises any of this works on Windows).

##TODO

1. Automate filling out team list
2. Add script to check starting lineups via twitter
3. Turn into an app so we can use oauth instead of test tokens
