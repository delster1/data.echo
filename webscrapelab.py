from bs4 import BeautifulSoup as bs  # import for beautifulsoup

import requests  # this is so i can use a link to get html output
import random

url = "https://www.w3schools.com"  # url to search

tutorialsDict = {}

response = requests.get(url) # turn url into html
w3HomeSoup = bs(response.content, 'html.parser')  # turn html into soup
# print(soup.prettify())

tutorial = input("what tutorial\n")
topic = input("what topic\n")
w3treeHtml = open("w3tree.html","r")
tutorialsBS = bs(w3treeHtml,'html.parser') # code with tutorials list

for a in tutorialsBS.find_all('a', href=True): # get links from tutorials to dictionary
	link = url+a['href'].replace(" ","")
	last = link.rindex("/") 
	# print(last)
	link = link[0:last]+"/"
	name = a.get_text().replace("Learn","").casefold()
	name = name.replace(" ","")
	# print(name)
	tutorialsDict[name] = link
	
print(tutorialsDict)
urlToSearch = tutorialsDict[tutorial]# testing tutorial
print(urlToSearch)
# topic = "arrays"

print(urlToSearch) 

searchResponse = requests.get(urlToSearch) 
w3HomeSoup = bs(searchResponse.content, 'html.parser')  

topics = w3HomeSoup.find("div",id="leftmenuinnerinner") # find list of tutorial's topics

topicSoup = bs(str(topics), 'html.parser')  # turn topics into bs

for obj in topicSoup.find_all('a', href=True): # create list 
	name = obj.get_text().casefold()
	topicLink = urlToSearch +obj['href'] 
	if topic in name:
		print(topicLink)