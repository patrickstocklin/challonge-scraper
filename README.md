# Challonge Bracket Scraper

![Challonge](./doc/img/challonge.png)

## Abstract

I wanted some Challonge brackets in JSON format.

This python script fires requests at the Challonge Developer API for all iterations of a tournament series hosted on Challonge. Specify a target directory for your jsons and it will generate 3 sub directories containing pretty-print jsons for your (1) tournament, (2) participants, and (3) matches.

```
-/targetDir
---/tournamentSeries
-----/matches
-----/participants
-----/tournaments
```

## Setup

```
git clone https://github.com/patrickstocklin/challonge-scraper.git

virtualenv --no-site-packages challonge-scraper

cd challonge-scraper
source bin/activate

pip install -r requirements.txt
```

## Requirements

* Challonge Account and a corresponding API Key. You can visit the Developer Settings of your account to generate one.

## Usage

```
~/challonge-scraper$ python challonge-scraper.py -h
usage: challonge-scraper.py [-h] -u USER -k APIKEY -o TOURNAMENTOWNER -n
                            TOURNAMENTNAME -t TARGETDIRECTORY

This program scrapes Challonge brackets using the Challonge Developer API

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER
  -k APIKEY, --apikey APIKEY
  -o TOURNAMENTOWNER, --tournamentOwner TOURNAMENTOWNER
  -n TOURNAMENTNAME, --tournamentName TOURNAMENTNAME
  -t TARGETDIRECTORY, --targetDirectory TARGETDIRECTORY
```

## Example

```
python challonge-scraper.py -u XXX -k XXX -o tloc -n MNM -t ../data/tournaments

-/data/tournaments
---/MNM
-----/matches
-----/participants
-----/tournaments
```

I really enjoy TourneyLocator's Monday Night Melee dataset. As of writing this, it has ~200 weekly brackets for Super Smash Brothers Melee. Almost 4 years of Melee tournament-data.

If you want to borrow, please take note of what cURL commands are being made and modify them accordingly. I'm too lazy at the moment to make this work for all series of brackets.

For further information, visit the [Challonge API Documentation](https://api.challonge.com/v1)
