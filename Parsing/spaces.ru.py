import requests
from bs4 import BeautifulSoup
from lxml import html

url = 'https://spac1.com/musicat/'


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
}


response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text,"html.parser")

main_block = soup.find('div',{'class':'widgets-group widgets-group_top'})
songs = main_block.find_all('div',{'class':'light_border_bottom t-bg3'})

for x in songs:
	s = x.find('div',{'class','player_item player_item_old p_i_tools oh'})
	string = '{} - {} - {}'.format(s['data-artist'],s['data-title'],s['data-src'])
	print(string)
