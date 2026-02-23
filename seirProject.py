import sys
import requests
from bs4 import BeautifulSoup

def pageDetail(input_link):
    try:
        response = requests.get(input_link)
    except:
        print("Sorry, Please give input in right way")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    print("PAGE DETAILS")

    print("Title of the Page:")
    if soup.title:
        print(soup.title.text)
    else:
        print("Sorry, This page does not have title")
    print()

    print("Body of the Page:")
    if soup.body:
        print(soup.body.get_text())
    else:
        print("Sorry,This Page doesn't have body")
    print()

    print("URLs of the Page:")
    links = soup.find_all("a")
    for link in links:
        url_value = link.get("href")
        if url_value:
            print(url_value)

    print()
    for link in links:
        print(link.get("href"))

if len(sys.argv) < 2:
    print("Sorry, please give some valid urls")
    sys.exit()
    
input_link = sys.argv[1]
pageDetail(input_link)
