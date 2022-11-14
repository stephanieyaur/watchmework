#!/usr/bin/python3

import webbrowser
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
#from pywebcopy import save_webpage
import json

def scrape_wiki(term):

    # returns a dicionary containing:
        # title: the title of the page (string)
        # link_to_article: a link to the page (string)
        # infobox: the infobox (html)
        # snippet: the first paragraph of the article, usually (html)
        # description: very short (a few words) description of what it is (string)

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "opensearch",
        "namespace": "0",
        "search": term,
        "limit": "5",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    if not DATA[3]: return {}

    print(DATA[3][0])

    url = DATA[3][0]

    # download_folder = "/Users/alextai/Documents/CS338/watchmework"

    # save_webpage(url, download_folder)

    html = requests.get(url).content
    #print(html)

    with urlopen(url) as webpage:
        content = webpage.read().decode()

    soup = BeautifulSoup(content, 'html.parser')

    ret = {}

    title = soup.find('span', class_="mw-page-title-main")
    print(title.get_text())
    ret["title"] = title.get_text()
    ret["link_to_article"] = url

    #print(soup.prettify())
    table = soup.find('table', class_ = "infobox")
    ret["infobox"] = str(table).replace("/wiki/", "en.wikipedia.org/wiki/")
    
    snip = soup.find('b')
    print(snip.parent)
    ret["snippet"] = str(snip.parent).replace("/wiki/", "en.wikipedia.org/wiki/")

    short_descr = soup.find('div', class_ = "shortdescription")
    print(short_descr.get_text())
    ret["description"] = short_descr.get_text()

    return ret
    #return str(table).replace("/wiki/", "en.wikipedia.org/wiki/")



# print(str(table).replace("/wiki/", "en.wikipedia.org/wiki/"))
# with open("italy_tbl.html", "w", encoding='utf-8') as file:
#     file.write(str(table).replace("/wiki/", "https://en.wikipedia.org/wiki/"))
# rows = table.find_all('tr')
# ret = {}
# for r in rows:
#     #print(r)
#     if r.find('th', class_ = "infobox-above"):
#         #print(r.find('th', class_ = "infobox-above"))
#         ret['title'] = r.find('th', class_ = "infobox-above").get_text()
#     if r.find('th', class_ = "infobox-label"): 
#         label = r.find('th').get_text()
#         #print(label)
#         if (label == "Born") and (0==1):
#             ret["Birthday"] = r.find('span', class_ = "bday").get_text()
#             ret["Birthplace"] = r.find('div', class_ = "birthplace").get_text()
#         else:
#             data = r.find('td')
#             ret[label] = data
#         print(data)
#         print()
#print(ret["Born"])
#print(ret["Population"])
#print(ret["Died"])
#print(ret["Born"])
#print(json.dumps(ret, indent=4))

# """
#     parse.py

#     MediaWiki API Demos
#     Demo of `Parse` module: Parse content of a page

#     MIT License
# """

# import requests

# S = requests.Session()

# URL = "https://en.wikipedia.org/w/api.php"

# PARAMS = {
#     "action": "parse",
#     "page": "Vincent van Gogh",
#     "format": "json"
# }

# R = S.get(url=URL, params=PARAMS)
# DATA = R.json()

# print(DATA["parse"]["text"]["*"])

if __name__ == "__main__":
    info = scrape_wiki("asdfasderfawe")
    print()
    print()
    print()
    print(json.dumps(info, indent=4))