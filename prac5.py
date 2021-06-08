from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import sys, json
class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for (key, value) in attrs:
                if key == "href":
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]           
    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if "text/html" in response.getheader("Content-Type"):
            htmlContent = response.read() 
            htmlString = htmlContent.decode("utf-8")
            self.feed(htmlString)
            response.close()
            return htmlString, self.links
        else:
            return "", []
    def crawl(url, word):
        # List of found urls
        foundUrl = []
        # List of already visited url to prevent revisiting the same url twice
        visitedURL = []
        # Keeping count of all the pages visited
        numberVisited = 0; 
        # If no words found show error
        foundWord = False # Starting the parser class
        parser = LinkParser()
        # Checking the first url
        data, links = parser.getLinks(url)
        links.append(url)
        # Looping all the links
        for link in links:
            # Kinda straight foward...
            numberVisited = numberVisited + 1
            try:
                # Checking if link has not been visited yet
                if link not in visitedURL:
                    # Appending link to VisiterURL list
                    visitedURL.append(link)
                    data, li = parser.getLinks(link)
                    print (numberVisited, "Scanning URL ", link)
                    if data.find(word) > -1:
                        foundWord = True
                        foundUrl.append(link)
                        print("-" * 10)
                        print(" ")
                        print("The word", word, "was found at", link)
                        print(" ")
                        print("-" * 10)
                    else:
                        print ("Matches Not Found")
            except:
                print (" **Failed **", "")
        #If the word was never found show the error
        if foundWord == False:
            print ("The word", word, "was not found!")
        print ("Finished, crawled", numberVisited, "pages")
        print (json_list(foundUrl))
def json_list(list):
    lst = []
    d = {}
    for pn in list:
        d=pn
        lst.append(d)
    return json.dumps(lst, separators=(',',':'))
LinkParser.crawl("https://www.facebook.com", "login")
