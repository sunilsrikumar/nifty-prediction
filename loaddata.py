import quandl
import os
import pandas as pd
import pickle
import bs4 as bs
import requests 

quandl.ApiConfig.api_key='DaxY2-cRWvRyDQVno54P'

startdate="2012-11-16"
enddate="2022-11-16"

def nifty_50_list():
    resp = requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
    soup = bs.BeautifulSoup(resp.text, 'lxml')

    table = soup.find('table', {'class': 'wikitable sortable'},'tbody')

    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker)

    with open("nifty50_list.pickle","wb") as f:
        pickle.dump(tickers,f)

    tickers.append('BAJAJ_AUTO')#Adding it manually since ticker name obtained from Wikipedia contains a hypen whereas quandl code expects an underscore
    tickers.append('MM')#Adding it manually since quandl code is different than the ticker symbol obtained from Wiki which is M&M
    tickers.append('NIFTY_50')#Fetching data for NIFTY50 index whose price we want to predict
    tickers.remove('VEDL')
    tickers.remove('UPL')
    tickers.remove('IBULHSGFIN')
    return tickers
