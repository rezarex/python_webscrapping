'''
Webscrapping using Beautifulsoup4.
Scrapping data and saving to database.
This is a basic version
'''

from bs4 import BeautifulSoup
import requests

html_page = requests.get('https://djinni.co/jobs/?keywords=python&all-keywords=&any-of-keywords=&exclude-keywords=').text
soup = BeautifulSoup(html_page, 'lxml')