'''
Webscrapping using Beautifulsoup4.
This is a basic version for learning purposes
'''

from bs4 import BeautifulSoup
import requests

html_page = requests.get('https://djinni.co/jobs/?keywords=python&all-keywords=&any-of-keywords=&exclude-keywords=').text
soup = BeautifulSoup(html_page, 'lxml')
job = soup.find('li', class_='list-jobs__item list__item')
#print(job)
title = job.find('a', class_='profile')
#print(title)
title_text = title.find('span').text
#print(title_text)
desc = job.find('div', class_='truncated mw-100 fz-16 mb-0 js-show-more').text
#print(desc)
title_par = job.find('div', class_='mt-2')
title_sub_par = title_par.find('div', class_='list-jobs__details')
title_sub_par2 = title_sub_par.find('div', class_='list-jobs__details__info')
company = title_sub_par2.find('a').text
#print(company)
posted_by = company = title_sub_par2.find('a', class_='link-muted').text
#print(posted_by)

print(f'{company} is hiring a {title_text} with the following qualifications:')
print('================================================================================================')
print(f'{desc}')
