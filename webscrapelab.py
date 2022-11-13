from bs4 import BeautifulSoup as bs  # import for beautifulsoup

import requests  # this is so i can use a link to get html output
import re  # python regex library (used ln 11)

url = "https://www.w3schools.com/"  # url to search

response = requests.get(url) # turn url into html
soup = bs(response.content, 'html.parser')  # turn html into soup
# print(soup.prettify())
ptags = soup.find_all("nav",id="nav_tutorials")  # array of tags that start with 'h' or 'p'

tutorialsBS = bs(str(ptags[0]), "html.parser")
tutorials = tutorialsBS.find_all('a')

tutorialLinks = []
for ind,obj in enumerate(tutorials):
	print(obj)
	if ".asp\">Learn" not in obj or ".php\">Learn" not in obj or "https://" in obj: 
		# print(obj)
		tutorials.remove(obj)

for ind,obj in enumerate(tutorials):
	thing = str(obj)
	startInd = thing.find("href=") +6
	endInd = thing.find("\">Learn")
	toAppend = thing[startInd:endInd]
	
	tutorialLinks.append(toAppend)
	# print(toAppend)

for ind,obj in enumerate(tutorialLinks):
	print(obj[len(obj)-1] != "p")
	if obj[len(obj)-1] != "p":
		tutorialLinks.pop(ind)

print(tutorialLinks)