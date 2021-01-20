# -*- coding: utf-8 -*-

import urllib
import random
import webbrowser
import types

SMS_URL_SCHEME = "launchpro-messaging://?to=[PHONE_HERE]&body={0}"

TEMPLATES = [
	[
		['You ', ['can ', 'should '], 'make combining phrases. So your ', ['mother', 'girlfriend', 'wife'], ' ', ['will be happy', 'doesn\'t know you automated it'] ]
	]
]

def generateURL(message):
	return SMS_URL_SCHEME.format(urllib.quote(message))

def randomSMS(templateList):
	head = templateList[0]
	tail = templateList[1:]
	if type(head) == types.StringType:
		if len(tail) > 0:
			return '{0}{1}'.format(head, randomSMS(tail))
		else:
			return head
	elif type(head) == types.ListType:
		pos = random.randint(0, len(head)-1)
		if len(tail) > 0:
			if type(head[pos]) == types.ListType:
				return '{0}{1}'.format(rndMessage(head[pos]), randomSMS(tail))
			else:
				return '{0}{1}'.format(head[pos], randomSMS(tail))
		else:
			if type(head[pos]) == types.ListType:
				return randomSMS(head[pos])
			else:
				return head[pos]

def main():
	# FOR TESTING UNCOMMENT LINES BELOW
	print(randomSMS(TEMPLATES))
	print(randomSMS(TEMPLATES))
	print(randomSMS(TEMPLATES))
	print(randomSMS(TEMPLATES))
	# FOR TESTING COMMENT LINES BELOW
	# webbrowser.open(generateURL(randomSMS(TEMPLATES)))

if __name__ == '__main__':
	main()
