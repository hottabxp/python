#https://oauth.vk.com/authorize?client_id=3682744&v=5.7&scope=wall,offline&redirect_uri=http://oauth.vk.com/blank.html&display=page&response_type=token
import urllib
text = "Test message!!!"
token = ""
base = "https://api.vk.com/method/wall.post?owner_id=34254853&message="+text+"&v=5.0&access_token="+token+""
page = urllib.urlopen(base).read()
print page