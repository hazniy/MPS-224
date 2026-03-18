import requests
import xml.etree.ElementTree as tree
from bs4 import BeautifulSoup

def get_links_a(url):
    # This gives an object called response which is an instance of the class requests.models.Response
    # (as we could learn by typing type(response) in the console).  The attribute response.text is
    # a string containing the HTML code of the page.  (We could learn this by reading the documentation
    # or by typing dir(response) to get a list of all possible attributes and methods of response.)
    response = requests.get(url)
    # The next line constructs an instance of the class BeautifulSoup.  (It is a standard convention to
    # that names of classes have capital letters, and names of objects have lower-case letters.)
    soup = BeautifulSoup(response.text, 'html.parser')
    # We now use the find_all() method to find all HTML tags of the type 'a' (which are the tags for links).
    links = soup.find_all('a')
    for link in links:
        # The URL associated to a link is stored in the attribute 'href' of the tag.  We print it.
        print(link.get('href'))

def get_links_b(url):
    response = requests.get(url)
    # The next line constructs an instance of the class xml.etree.ElementTree.Element
    t = tree.fromstring(response.text)
    # We now use the findall() method to find the links.  The argument './/a' is an XPath expression.
    # XPath is a very powerful and flexible language for finding elements in an XML document;
    # you could use it to find all the links occuring in the third column of a table where 
    # the cell background is green, for example, which you could not do with BeautifulSoup.
    # However, for simple tasks like this one, there is little difference between the two libraries.  
    # See https://developer.mozilla.org/en-US/docs/Web/XPath for a tutorial on XPath.  
    links = t.findall('.//a')
    for link in links:
        print(link.attrib['href'])

url = 'https://strickland1.org/'
get_links_a(url)
get_links_b(url)
