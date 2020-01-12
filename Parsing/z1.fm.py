import requests
from bs4 import BeautifulSoup
from lxml import html

url = 'https://z1.fm/new?sort=date&page=2'

responce = requests.get(url)

soup = BeautifulSoup(responce.text,"html.parser")

container = soup.find('section',{'id':"container"})
songs = container.find_all('div',{'class':'songs-list-item'})

string = ''
urls = ''

for song in songs[1:]:
	name = song.find('div',{'class','song-name'}).text.strip()
	artist = song.find('div',{'class':'song-artist'}).text.strip()
	time = song.find('div',{'class':'song-info'}).text.strip()
	url = song.find('span',{'class':'song-download'})

	string += ('{} {} {} https://z1.fm{}\n'.format(artist,name,time,url['data-url']))
	urls+=('https://z1.fm{}\n'.format(url['data-url']))


print(string)

with open('songs2.txt','w') as file:
	file.write(urls) 
