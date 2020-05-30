import goslate

text = "Hello Universe!"

# Service is mostly unavailable
# gs = goslate.Goslate()
gs = goslate.Goslate(writing=goslate.WRITING_NATIVE_AND_ROMAN, retry_times=100, timeout=100,
                     service_urls=['https://translate.google.com/', 'https://translate.google.co.in/'])

print(gs.translate('hello world', 'hi')) # Hindi
print(gs.translate('hello world', 'ac')) # English ???
print(gs.translate('hello world', 'ad')) # ???
print(gs.translate('hello world', 'af')) # African ???
print(gs.translate(text,'fr')) # French
print(gs.translate(text,'de')) # Denmark ???
print(gs.translate('hello world', 'zh')) # Chinese

