from bs4 import BeautifulSoup as bs  # import for beautifulsoup
import requests  # this is so i can use a link to get html output
import random

tutUpperNodes = {}
def getW3HomepageSoup():
	url = "https://www.w3schools.com"  # url to search

	
	response = requests.get(url) # turn url into html
	w3HomeSoup = bs(response.content, 'html.parser')  # turn html into soup


def getTutorialsDict():
	url = "https://www.w3schools.com"  # url to search
	tutorialsDict = {}

	w3treeHtml = open("w3tree.html","r")
	tutorialsBS = bs(w3treeHtml,'html.parser') # code with tutorials list
	for a in tutorialsBS.find_all('a', href=True): # get links from tutorials to dictionary
		link = url+a['href'].replace(" ","")
		last = link.rindex("/") 
		link = link[0:last]+"/"
		name = a.get_text().replace("Learn","").casefold()
		name = name.replace(" ","").casefold()
		# print(name, " ",link)
		tutorialsDict[name] = link
	return tutorialsDict
		

# topic = "arrays"

# print(tutorialsDict[tutorial])
# print(urlToSearch)
def getTopicsSoup(tutorialsDict,tutorial,topic):
	urlToSearch = tutorialsDict[tutorial]# testing tutorial


	searchResponse = requests.get(urlToSearch+"default.asp") 
	w3HomeSoup = bs(searchResponse.content, 'html.parser')  

	topics = w3HomeSoup.find("div",id="leftmenuinnerinner") # find list of tutorial's topics

	topicSoup = bs(str(topics), 'html.parser')  # turn topics into bs
	# print(topicSoup)
	topicLinks = []

	for obj in topicSoup.find_all('a', href=True): # create list 
		name = obj.get_text().casefold()
		topicLink = urlToSearch +obj['href'] 
		if topic in name:
			topicLinks.append(topicLink)
			pass
	return topicLinks

def getExamples(topicLinks):

	links = requests.get(topicLinks[0]) 
	exampleSoup = bs(links.content, 'html.parser') 

	examples = exampleSoup.find_all("div", class_="w3-example")

	choice = random.choice(examples)

	return choice
def main():
	tutorial = "javascript"
	topic = "loop"

	getW3HomepageSoup()

	tutorialsDict = getTutorialsDict()
	topicLinks = getTopicsSoup(tutorialsDict,tutorial,topic)
	out = getExamples(topicLinks)

	# print(out)
	return out

if __name__ == "__main__":
	main()