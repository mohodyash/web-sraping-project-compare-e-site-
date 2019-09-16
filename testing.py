from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv


my_url = 'https://www.newegg.com/global/in-en/p/pl?d=graphic+card'

# open a connection and get page
uClient = urlopen(my_url)
# grab the html
page_html = uClient.read()
# close a connection
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser")

# print(page_soup.h1)
# print(page_soup.p)
# print(page_soup.body.span)

# grabs each project
containers = page_soup.find_all("div", {"class": "item-container "})
# print(len(containers))
# print(containers[0])
# contain = containers[0]
# container = containers[0]

# print(container.a["href"])
# print(container.a.img["alt"])
links = list(range(0, len(containers)))
title = list(range(0, len(containers)))



count = 0
try:
    for container in containers:
        links[count] = container.a["href"]
        title[count] = container.a.img['alt']
        count = count + 1
except BaseException:
    print("Error")
# print(len(links))
# print(links[5])
# print(links[0])

html_for_link = urlopen(links[0])
soup_for_link = BeautifulSoup(html_for_link, "html.parser")

print(soup_for_link.find_all('div', {'class':'aside'}))

# soup_for_link = soup_for_link.prettify("utf-8")
# with open("test.html", "wb") as file:
#     file.write(soup_for_link)


