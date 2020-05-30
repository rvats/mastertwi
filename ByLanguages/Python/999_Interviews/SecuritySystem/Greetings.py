"""
@Author: Rahul Vats
@AuthorEmail: vats.rahul@gmail.com
@Purpose: This file handles the logic to interact with user intelligently
@History: 
"""

import datetime as dt
from datetime import time

import configparser

def CreateDefaultConfig():
	config = configparser.ConfigParser()
	config['DEFAULT'] = {'ServerAliveInterval': '45',
						'Compression': 'yes',
						'CompressionLevel': '9'}
	config['bitbucket.org'] = {}
	config['bitbucket.org']['User'] = 'hg'
	config['topsecret.server.com'] = {}
	topsecret = config['topsecret.server.com']
	topsecret['Port'] = '50022'     # mutates the parser
	topsecret['ForwardX11'] = 'no'  # same here
	config['DEFAULT']['ForwardX11'] = 'yes'
	with open('GreetingsConfig.ini', 'w') as configfile:
		config.write(configfile) 

def GetGreetingMessage():
	CreateDefaultConfig()
	greeting = "Hello! How are you?"
	today = dt.datetime.now()
	now = today.time()
	# print(today)
	# print(now)
	
	# Set The Engine Greetings
	if time(4,0) <= now <= time(11,00):
		greeting = 'Good morning. ' + greeting
	elif time(11,1) <= now <= time(16,00):
		greeting = 'Good after noon. ' + greeting
	else:
		greeting = 'Good night. '
	
	return greeting