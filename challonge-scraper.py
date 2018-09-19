import os
import sys
import argparse

################################################################################################################################
# Challonge Bracket Scraper
#
# Requires an api-key associated with your challonge account!
#
# python -u [ACCOUNT] -k [API-KEY] -o [TOURNAMENTOWNER] -n [TOURNAMENTNAME] -t [TARGETDIR]
#
# ex) python challonge-scraper.py -u XXX -k XXX -o tloc -n MNM -t ../data/tournaments
################################################################################################################################

def scrape(user, apikey, owner, name, target):
	#Most Challonge users iterate their bracket URLs, so this should suffice for most series
	for n in range(198,199):
		print "Fetching Challonge Bracket: %s%s" %(str(name),str(n))
		os.system(
			"curl -XGET -k -v https://%s:%s@api.challonge.com/v1/tournaments/%s-%s%s.json " \
			"| python -m json.tool > " \
			"%s/%s/tournaments/%s-%s-tournament.json" %(str(user),str(apikey),str(owner),str(name),str(n),str(target),str(name),str(name),str(n)))
		os.system(
			"curl -XGET -k -v https://%s:%s@api.challonge.com/v1/tournaments/%s-%s%s/participants.json " \
			"| python -m json.tool > " \
			"%s/%s/participants/%s-%s-participants.json" %(str(user),str(apikey),str(owner),str(name),str(n),str(target),str(name),str(name),str(n)))
		os.system(
			"curl -XGET -k -v https://%s:%s@api.challonge.com/v1/tournaments/%s-%s%s/matches.json " \
			"| python -m json.tool > " \
			"%s/%s/matches/%s-%s-matches.json" %(str(user),str(apikey),str(owner),str(name),str(n),str(target),str(name),str(name),str(n)))

	print "Completed Fetching Challonge Brackets"

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This program scrapes Challonge brackets using the Challonge Developer API')
	parser.add_argument('-u', '--user', type=str, required=True)
	parser.add_argument('-k', '--apikey', type=str, required=True)
	parser.add_argument('-o', '--tournamentOwner', type=str, required=True)
	parser.add_argument('-n', '--tournamentName', type=str, required=True)
	parser.add_argument('-t', '--targetDirectory', type=str, required=True)

	args = parser.parse_args()

	if not os.path.isdir("%s/%s" %(str(args.targetDirectory),str(args.tournamentName))):
		os.makedirs("%s/%s" %(str(args.targetDirectory),str(args.tournamentName)))
		os.mkdir("%s/%s/tournaments" %(str(args.targetDirectory),str(args.tournamentName)))
		os.mkdir("%s/%s/matches" %(str(args.targetDirectory),str(args.tournamentName)))
		os.mkdir("%s/%s/participants" %(str(args.targetDirectory),str(args.tournamentName)))


	scrape(args.user, args.apikey, args.tournamentOwner, args.tournamentName, args.targetDirectory)
