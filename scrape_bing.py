import webbrowser
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from pywebcopy import save_webpage

url = "https://www.bing.com/search?q=van+gogh"

# download_folder = "/Users/alextai/Documents/CS338/watchmework"

# save_webpage(url, download_folder)

html = requests.get(url).content
print(html)

with urlopen(url) as webpage:
    content = webpage.read().decode()

soup = BeautifulSoup(content, 'html.parser')

print(soup.prettify())
# #print(soup.title.string)
# #print(soup.find_all("div"))
# #print(soup.find_all("div", class_ = "lc_expfact"))

