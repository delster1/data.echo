from bs4 import BeautifulSoup as bs  # import for beautifulsoup
import requests  # this is so i can use a link to get html output

url = "https://www.w3schools.com"  # url to search

tutorialsDict = {}
tutUpperNodes = {}

response = requests.get(url) # turn url into html

tutorial = "python"
topic = "arrays"

w3 = bs(response.content, 'html.parser')  # turn html into soup

for div in w3.find_all(attrs={'class': 'w3-col 13 m6'}):
	print(div)

for obj in topicSoup.find_all('a', href=True): # create list 
	name = obj.get_text().casefold()
	topicLink = urlToSearch +obj['href'] 
	if topic in name:
		print(topicLink)
		pass