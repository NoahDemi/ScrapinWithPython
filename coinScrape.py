from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://coinmarketcap.com/'

#opening up connection, grabbing the page.
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")


print(page_soup.h1)
