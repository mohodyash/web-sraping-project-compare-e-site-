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
print(links[0])

for link in links:
    new_connection = urlopen(link)
    html_page = new_connection.read()
    page_soup = BeautifulSoup(html_page, 'html.parser')
    full_infos = page_soup.find_all('div', {'class': 'plinks'})
    all_data = full_infos[0].find_all('fieldset')
    try:

        get_first_fildset_from_all_data = all_data[0]
        get_second_dl_from_fildset= get_first_fildset_from_all_data.find_all('dl')
        # print(get_second_dl_from_fildset[1].dd.text)
    except IndexError:
        print("index error ignor")



