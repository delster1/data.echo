from bs4 import BeautifulSoup as bs  # import for beautifulsoup
import requests  # this is so i can use a link to get html output

url = "https://www.w3schools.com"  # url to search

tutorialsDict = {}
tutUpperNodes = {}
response = requests.get(url) # turn url into html
w3HomeSoup = bs(response.content, 'html.parser')  # turn html into soup
# print(soup.prettify())

tutorial = "python"
topic = "arrays"

w3 = bs(response.content, 'html.parser')  # turn html into soup

data = w3.find_all(attrs={'class': 'w3-col l3 m6 w3-hide-medium'})
data += w3.find_all(attrs={'class': 'w3-col l3 m6'})

for item in data:
	print(item.name)