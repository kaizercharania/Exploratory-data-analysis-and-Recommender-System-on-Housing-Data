 
1. First step is to import all the libraries needed:
```
import requests
import pandas
import re
from bs4 import BeautifulSoup
import lxml
```
2.
We need a list of cities for which we are going to scrape.
We need to understand the pattern of the url. The site century21 needs:
domain_name/ + "city name" + "-" + "state_initials ('ca' in this case)"/ + "LCCA"+ "city name in CAPS"/
I am creating a list of cities (uploaded here as cities.txt) and using this list, generating the above pattern and storing it in search list.
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
