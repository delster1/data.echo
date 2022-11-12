from bs4 import BeautifulSoup as bs  # import for beautifulsoup

import requests  # this is so i can use a link to get html output
import re  # python regex library (used ln 11)

query = input("enter a search term")

url = "https://www.geeksforgeeks.org/python-programming-language/?ref=shm"  # url to search

response = requests.get(url) # turn url into html


soup = bs(response.content, 'html.parser')  # turn html into soup

# print(soup.prettify())
ptags = soup.find_all(
 re.compile('^p|^h|^d|^s|^a'))  # array of tags that start with 'h' or 'p'

text = query  # text to search

for i in ptags:  #iterate through array of tags
	if text in str(i.string):  #if text is in tag's NavigableString
		print(i.prettify())
