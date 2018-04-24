```python
import requests
import pandas
import re
from bs4 import BeautifulSoup
import lxml

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
