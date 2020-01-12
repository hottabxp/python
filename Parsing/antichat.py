import requests
from bs4 import BeautifulSoup
from lxml import html
import  sys

url = 'https://forum.antichat.ru/forums/news/'

responce = requests.get(url)
soup = BeautifulSoup(responce.text,"html.parser")

data = soup.find('div',{'class':'discussionList section sectionMain'})
d = data.find_all('li',{'class':'discussionListItem visible'})
string = ''

for x in d:
	title = x.find('a',{'class','PreviewTooltip'}).text
	date = x.find('a',{'class':'faint'}).text
	url = x.find('a',{'class':'PreviewTooltip'})['href']

	string += '{}|{}|https://forum.antichat.ru/{}\n'.format(title,date,url)
print(string)

with open('news.csv','w') as file:
	file.write(string)
