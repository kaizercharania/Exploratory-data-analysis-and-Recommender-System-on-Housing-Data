 
1. First step is to import all the libraries needed:
```
import requests
import pandas
import re
from bs4 import BeautifulSoup
import lxml
```
2.We need a list of cities for which we are going to scrape.
 * We need to understand the pattern of the url. The site century21 needs:
 * domain_name/ + "city name" + "-" + "state_initials ('ca' in this case)"/ + "LCCA"+ "city name in CAPS"/
 * I am creating a list of cities (uploaded here as cities.txt) and using this list, generating the above pattern and storing it in search list
```
data = []
myfile = open("/Users/kaizer/Desktop/cities.txt",encoding='utf-8')
data1 = myfile.read()
myfile.close()
data1 = list(data1.splitlines())
search_list = []
s=1
for i in range(len(data1)):
    string_name = data1[i]+"-ca/LCCA" 
    string_name = string_name.replace(" ","-")
    string_name = string_name + data1[i].upper().replace(" ","")
    search_list.append(string_name)
print (search_list)
```
3.
```
for i in (range(len(search_list))):
    page_requests =  requests.get("https://www.century21.com/real-estate/" + str(search_list[i]) )
    page_content = page_requests.content
    page_soup = BeautifulSoup(page_content,"html.parser")
    if page_soup.find('a',{"class":"bug"}) != None:
        num_results = int(page_soup.find('a',{"class":"bug"}).text)
        num_pages = int(num_results/20) + (num_results % 20 > 0)
        url = ("https://www.century21.com/real-estate/" + str(search_list[i]))
        print("url: " + url)
        print("number of pages: {}".format(num_pages))
        print("number of results: {}".format(num_results))
```
******************************************************************************************************************************



# Heading
## H1

1. asdd
2.s sss
3.  scdcd

* hello 

**hello:**

[html](https://github.com/kaizercharania/Web-Scraping/edit/master/different-sites-code/century21-dot-com/readme.md)

<b>wjwdwjbdjw</b>
