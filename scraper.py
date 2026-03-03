import sys
import requests
from bs4 import BeautifulSoup

def pageDetail(input_link):
    if not input_link.startswith("http"):
        input_link = "https://" + input_link
    try:
        response = requests.get(input_link)
    except:
        print("Sorry, Please give input in right way")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    print("PAGE DETAILS")
    print()
    print("Title of the Page:")
    if soup.title:
        print(soup.title.text.strip())
    else:
        print("Sorry, This page does not have title")
    print()

    print("Body of the Page:")
    if soup.body:
        print(soup.body.get_text())
    else:
        print("Sorry, This Page doesn't have body")
    print()
    print("URLs of the Page:")
    links = soup.find_all("a")

    for link in links:
        url_value = link.get("href")
        if url_value:
            print(url_value)
if len(sys.argv) < 2:
    print("Sorry, please give some valid urls")
    sys.exit()
    
input_link = sys.argv[1]
pageDetail(input_link)
