# -*- coding: utf-8 -*-

# from fdscraper.scrape.download import Companies
# from fdscraper.preprocess.preprocess_financials import preprocess_financials
from fdscraper.score.score import Score

companies_list = ['my_list','ITC','HDFCBANK']

# comps = Companies(companies=companies_list,driver_path='D:/Code/SM/chromedriver.exe')

# data_comps = comps.get_financials(verbose=1)

# proc_data = preprocess_financials(data_comps)

sco = Score(companies=companies_list,driver_path='D:/Code/SM/chromedriver.exe')

print(sco.fundamental_score())

