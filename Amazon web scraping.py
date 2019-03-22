##Pass link of the product as argument

from urllib.request import urlopen as uReq
from  urllib.request import Request
from bs4 import BeautifulSoup as soup

def amazon_search(a):
    req= Request(a,None,{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'})
    my_url=req
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup=soup(page_html,'lxml')
    containers=page_soup.findAll("span",{"class": "a-size-large","id":"productTitle"})
    container=containers[0].text
    print('\n')
    print("Brand: ".ljust(26," ")+((container).replace('\n',' ')).strip(" "))

    containers1=page_soup.findAll("span",{"class": "a-size-medium a-color-price"})
    container1=containers1[0].text
    print("Price: ".ljust(26," ")+((container1).replace('\n',' ')).strip(" "))

    containers2=page_soup.findAll("a",{"class": "a-popover-trigger a-declarative"})
    container2=containers2[0].text


    if(str(container2[1]).isdigit()):
        print("Ratings: ".ljust(26," ")+((container2).replace('\n',' ')).strip(" "))

    else:
        print("Ratings: ".ljust(26," ")+"Not rated yet")
    
print("Enter the link of the product selected from amazon website:")
a=str(input()) 
# you still write it as
#a = input()
amazon_search(a)

