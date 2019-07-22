from helpers import async_web
from urllib.request import urlopen, Request
import urllib.request
from bs4 import BeautifulSoup
import pickle
import datetime

DAY = datetime.datetime.today().strftime('%Y-%m-%d')
SOURCE_LINKS = "DATA/LINKS/init_links_dt=2019-07-21.pkl"
DEST_PATH = f'DATA/TEXT/{DAY}.txt'
#url = "http://www.prupescoop.com/post/2"

def extractText(response):
    soup = BeautifulSoup(response.decode('utf-8','ignore'),features="lxml")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)+'\n'

    #output the text to file
    with open(DEST_PATH,"a") as outfile:
        outfile.write(text)


#print(extractText("https://www.fifthdomain.com/industry/2019/06/27/hackers-are-repeatedly-targeting-navy-contractors/"))
#"""
filehandler = open(SOURCE_LINKS, 'rb')
links = pickle.load(filehandler, encoding='utf-8')

async_web(extractText,links)
#"""
