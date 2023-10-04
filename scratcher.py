import requests
from bs4 import BeautifulSoup
'''
This will scrap the top 10 videos from youtube using selenium
Then there will be lambda function to automate this periodically on AWS
'''
YOUTUBE_TOP_TEN_SONGS = "https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D"

resp = requests.get(YOUTUBE_TOP_TEN_SONGS)

print('Status Code: ',resp.status_code)

with open('trending.html', 'w', encoding="utf-8") as f:
    f.write(resp.text)

doc = BeautifulSoup(resp.text, 'html.parser')

print('Page Title ni:', doc.title)

#find all the video divs

video_divs = doc.find_all('div', class_='ytd-video-renderer')

print(f"Found {len(video_divs)} videos")