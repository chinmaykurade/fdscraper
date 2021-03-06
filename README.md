# Indian Stocks - Fundamental(Financials) Data Downloader

A web scrapper using Selenium Python to download the fundamentals as well as price data from [Screener.in](https://www.screener.in)


# Introduction

Fundamental analysis of any company includes the financial statement analysis
of the respective company. This package helps to download the financial data 
of companies listed on the NSE - India. Also, some tools are provided to 
help analyse the financial data of the companies as well.

# Installation - using pip
```pip install fdscraper```
 
# Usage

First, either create the list of companies or create a file containing the
names of companies. The elements of the list must be the stock symbols on NSE.
NOTE: The first element of the list is the name of the list and will be ignored.

You also need to download the chrome web driver for your respective Chrome
browser version. Note that this version of the package currently supports only
Google Chrome browser, support for other browsers will be added in future versions. 

## 1. Downloading the financials of companies
    
1. Import the module and define the webdriver path
```python
from fdscraper.scrape.download import Companies
driver_path = 'chromedriver.exe'
```   
2. Downloading the financial data
- Downloading from a list
    
```python
companies_list = ['my_list','ITC','HDFCBANK']
comps = Companies(companies=companies_list,driver_path='chromedriver.exe')
data_comps = comps.get_financials()
```

- Downloading from a text file:  
Create a text file in the following format:
    
```
my_list,TCS,HDFCBANK
```

And then download the data:
```python
file_path = 'input.txt' # Path to the input file
comps = Companies(driver_path='chromedriver.exe')
data_comps = comps.get_financials(file_path=file_path)
```
