import sys
import requests
from bs4 import BeautifulSoup

def webSites(entry):
    if not entry.startswith("http"):
        entry = "https://" + entry
    try:
        response = requests.get(entry
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
        url_val = link.get("href")
        if url_val:
            print(url_val)
if len(sys.argv) < 2:
    print("Looks like there was an issue, please give some valid urls")
    sys.exit() 
entry = sys.argv[1]
webSites(entry)
