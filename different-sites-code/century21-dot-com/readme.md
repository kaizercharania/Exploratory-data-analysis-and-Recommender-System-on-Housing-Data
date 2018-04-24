 
1. First step is to import all the libraries needed:
```
import requests
import pandas
import re
from bs4 import BeautifulSoup
import lxml
```
2. We need a list of cities for which we are going to scrape.
 * We need to understand the pattern of the url. The site century21 needs:
 * <b>domain_name/ + "city name" + "-" + "state_initials ('ca' in this case)"/ + "LCCA"+ "city name in CAPS"/</b>
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
3. Now once you have the url, you need request the html file to perform extraction of the details you need to scrape.
 * I have used requests library for getting the html file and saving it the variable. 
 * Now after getting the html file, we will parse that file with BeautifulSoup using "html.parser"
```
for i in (range(len(search_list))):
    page_requests =  requests.get("https://www.century21.com/real-estate/" + str(search_list[i]) )
    page_content = page_requests.content
    page_soup = BeautifulSoup(page_content,"html.parser")
```
4. As there are multiple pages in the search query for the particular city, you need to take out the number of pages so that you can iterate to all the pages. As, the Century21 site is dynamic and does not have next page links, I needed to find out how many pages are there. So, I found a way to get the number of pages. For that I used total search results number which is stored in <b>class ="bug"</b>. As there page only shows 20 results per page, I used that to find out number of pages. 
```
    if page_soup.find('a',{"class":"bug"}) != None:
        num_results = int(page_soup.find('a',{"class":"bug"}).text)
        num_pages = int(num_results/20) + (num_results % 20 > 0)
        url = ("https://www.century21.com/real-estate/" + str(search_list[i]))
        print("url: " + url)
        print("number of pages: {}".format(num_pages))
        print("number of results: {}".format(num_results))
```
5. After getting the pages, I need to iterate through every page and extract the information for each and every search.
 * There was no unique class available for all the search results, so I compared the part of the class which was same for all the house informations using regex and then I used Beautiful soup to extract that data
 * At the end of every page, there was a href tag which showed the next page link. So, I extracted that link and again the data was extracted from that till that link was not present.
 
```
        
        for i in range(num_pages):
            print ("total_entries: {}".format(s))
            html_req = requests.get(url)
            html_content = html_req.content
            html_soup = BeautifulSoup(html_content,"html.parser")
            regex = re.compile('.*infinite-item property-card clearfix property-card*')
            data_all = html_soup.find_all("div",{"class":regex})
            for items in range(len(data_all)):
                if  data_all[items].find('a',{"class":"listing-price"}) != None:
                    price = data_all[items].find('a',{"class":"listing-price"}).text.replace("\n","").replace(" ","")

                if  data_all[items].find('div',{"class":"property-beds"}) != None:
                    beds = data_all[items].find('div',{"class":"property-beds"}).text.replace("\n","").replace(" ","").replace("beds","").replace("bed","")

                if  data_all[items].find('div',{"class":"property-baths"}) != None:
                    baths = data_all[items].find('div',{"class":"property-baths"}).text.replace("\n","").replace(" ","").replace("baths","").replace("bath","")
                if  data_all[items].find('div',{"class":"property-sqft"}) != None:
                    area = data_all[items].find('div',{"class":"property-sqft"}).text.replace("\n","").replace(" ","").replace("sq.ft","")
                if  data_all[items].find('div',{"class":"property-address"}) != None:
                    street = data_all[items].find('div',{"class":"property-address"}).text.replace("\n","").replace("   ","")
                if  data_all[items].find('div',{"class":"property-city"}) !=None:
                    city_state_pin = data_all[items].find('div',{"class":"property-city"}).text.replace("\n","").replace("   ","").split(" ")
                    if len(city_state_pin) >=5:
                        city = city_state_pin[0] + " " + city_state_pin[1]+ " " + city_state_pin[2]
                        state = city_state_pin[3]
                        pin = city_state_pin[4]
                    elif len(city_state_pin) ==4 :
                        city = city_state_pin[0] + " " + city_state_pin[1]
                        state = city_state_pin[2]
                        pin = city_state_pin[3]
                    elif len(city_state_pin) <4:
                        city = city_state_pin[0] 
                        state = city_state_pin[1]
                        pin = city_state_pin[2]
                d = {"an0": s ,"area":area,"beds":beds,"baths":baths,"street":street,"city":city,"state":state,"pin":pin,"price": price}
                s +=1
                data.append(d)
            print(s)
            if html_soup.find('link',{"rel":"next"}) != None:
                url = html_soup.find('link',{"rel":"next"}, href=True)['href']
```
6. Export the data collected to csv file
```
df = pandas.DataFrame(data)
df.to_csv("scraped_century21_data.csv")

```
7. Here is the sample for that data generated:

```

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
