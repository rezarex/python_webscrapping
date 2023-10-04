import requests
from bs4 import BeautifulSoup
from selenium import webdriver

'''
This will scrap the top 10 videos from youtube using selenium
Then there will be lambda function to automate this periodically on AWS
'''
YOUTUBE_TOP_TEN_SONGS = "https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D"

driver = webdriver.Chrome('./chromedriver/chromedriver.exe')

driver.get(YOUTUBE_TOP_TEN_SONGS)

print('Page titties: ', driver.title)