#Really good helper function for running async tasks
#Author: Joshua Prupes 2019/07/21 joshua.prupes@ibm.com

#aiohttp allows for asyncronous http requests
import aiohttp
import asyncio
#handle possible errors (TBD) which occur for some http requests
from aiohttp import ClientSession
from aiohttp import ClientOSError
#from bs4 import BeautifulSoup


async def apply_func(func, url):
    async with ClientSession() as session:
        try:
            async with session.get(url,timeout=2) as response:
                response = await response.read()
                print(url)
                func(response)
        #error handling
        except:
            print(f'{url} \t failed')

def async_web(func, urls):
    loop = asyncio.get_event_loop()
    tasks = []
    counter = 0
    for url in urls:
        task = asyncio.ensure_future(apply_func(func,url.strip()))
        tasks.append(task)
        counter +=1
        if counter%300 == 0:
            loop.run_until_complete(asyncio.wait(tasks))
            tasks = []
    if len(tasks) != 0:
        loop.run_until_complete(asyncio.wait(tasks))

'''
testing

sites = ['https://www.computerweekly.com/news/252466636/Most-influential-women-in-UK-tech-The-2019-longlist',
'https://searchdatabackup.techtarget.com/tip/Cloud-backup-versus-cloud-storage-comparison',
'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0219180',
'https://www.bizjournals.com/houston/news/2019/06/24/chevron-phillips-chemical-qatar-petroleum-agree-to.html?ana=RSS&s=article_search&utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+bizj_houston+%28Houston+Business+Journal%29',
'https://www.entrepreneur.com/article/336803',
'https://success.salesforce.com/issues_view?id=a1p3A0000003d8DQAQ',
'https://seekingalpha.com/article/4275483-retirees-dividend-portfolio-john-janes-june-taxable-account-update-danger-making-assumptions']


def extractText(response):
    soup = BeautifulSoup(response.decode('utf-8','ignore'),features="lxml")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()
    #print(text)

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)+'\n'
    #print(text)
    #return text
async_web(extractText, sites)
'''
