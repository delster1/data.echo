from bs4 import BeautifulSoup as bs  # import for beautifulsoup

import requests  # this is so i can use a link to get html output
import re  # python regex library (used ln 11)

url = "https://www.w3schools.com"  # url to search

dict = {}

response = requests.get(url) # turn url into html
w3HomeSoup = bs(response.content, 'html.parser')  # turn html into soup
# print(soup.prettify())

w3treeHtml = open("w3tree.html","r")
tutorialsBS = bs(w3treeHtml,'html.parser') #

for a in tutorialsBS.find_all('a', href=True):
	link = url+a['href'].replace(" ","")
	name = a.get_text().replace("Learn","")

	dict[link] = name
	
	

