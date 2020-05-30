import configparser
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
with open('example.ini', 'w') as configfile:
    config.write(configfile)


test = config.sections()
print(test)
config.read('example.ini')
# ['example.ini']
config.sections()
# ['bitbucket.org', 'topsecret.server.com']
'bitbucket.org' in config
# True
'bytebong.com' in config
# False
config['bitbucket.org']['User']
# 'hg'
config['DEFAULT']['Compression']
# 'yes'
topsecret = config['topsecret.server.com']
topsecret['ForwardX11']
# 'no'
topsecret['Port']
# '50022'
for key in config['bitbucket.org']: print(key)
config['bitbucket.org']['ForwardX11']
