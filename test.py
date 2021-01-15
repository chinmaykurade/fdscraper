# -*- coding: utf-8 -*-

from fdscraper.scrape.download import Companies

comps = Companies(companies=['my_list','ITC'],driver_path='D:/Code/SM/chromedriver.exe')

print(comps.get_financials())

