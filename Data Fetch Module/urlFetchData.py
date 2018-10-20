from bs4 import BeautifulSoup
import re
import urllib.request as urllib2
import urllib

def urlFetchData(url):
    string = ""
    var = ""
    print(url)
    #lets fetch the text from the url
    try :
        soup = BeautifulSoup(urllib2.urlopen(url).read(), 'html')

        #print("The title is : " + soup.find_all('title')[0].getText())
        string = "\"url\" : \"" + url + "\","
        string = string + "\"title\" : \"" + soup.find_all('title')[0].getText() + "\","
        string = string + "\"data\" : \""
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            # extract information
            var += p.getText()
            #print(var)
            #fo.write(var)
            #append the text to the file
        string = string + var + "\""
        return string
    except:
        return ""