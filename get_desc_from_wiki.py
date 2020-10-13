import re

from bs4 import BeautifulSoup 
from requests import get

topic_list = [ x.strip() for x in open("/tmp/list").readlines() ]

for topic in topic_list:
	try:
		wiki = BeautifulSoup(get('https://ru.wikipedia.org/wiki/%s' % topic).content, "lxml")
		desc_pars = wiki.find('div', 'mw-parser-output')('p')[0:3]
		desc = ""
		for p in desc_pars:
			desc += p.text

		print("### Инструмент %s " % topic)
		print()
		print(desc)

		try:
			img_container = wiki.find('span', 'wikidata-main-snak')
			src = re.sub(pattern=r'\/\d+px', string=img_container.a.img['src'], repl='/800px')
			alt = img_container.a.img['alt']
			print("!'[%s](https://%s)" % (alt, src))
		except AttributeError:
			print("#### noimage")
	except TypeError:
		print("######################################### %s " % topic)