#This mini script is used to get the starting links relating to the top S&P Companies
import requests
import json
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import pickle
from pprint import pprint


PATH_TO_SP500 = "Data/Stocks/SP500.xlsx"
DAY = datetime.datetime.today().strftime('%Y-%m-%d')
MONTH_AGO = (datetime.datetime.today() - relativedelta(months=1)).strftime('%Y-%m-%d')

table = pd.read_excel(PATH_TO_SP500)
links = set()
for company in table['Security']:
    response = requests.get(f'https://newsapi.org/v2/everything?q={company}'
                        f'&from={MONTH_AGO}&sortBy=relevancy&apiKey=37ca4ee89dd9402ebd2399b331aad366'
                        f'&language=en&pageSize=100').json()
    try:
        for article in response['articles']:
            #print(article['url'])
            links.add(article['url'])
    except:
        #usually once you hit the rate limit 500/day its all ogre
        pprint(response)

with open(f"Data/Links/init_links_dt={DAY}.pkl", 'w') as outfile:
    pickle.dump(links, outfile)
