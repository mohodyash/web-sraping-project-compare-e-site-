from bs4 import BeautifulSoup
from urllib.request import urlopen

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
link = list(range(0, len(containers)))
title = list(range(0, len(containers)))
count = 0
for container in containers:
    link[count] = container.a["href"]
    title[count] = container.a.img['alt']
    count = count + 1

# print(len(link))
# print(len(title))

link_url = link[0]
new_connection = urlopen(link_url)
page_html = new_connection.read()

page_soup = BeautifulSoup(page_html, "html.parser")

# print(page_soup)

full_infos = page_soup.find_all('div', {'class': 'plinks'})

# print(len(full_infos))
print(full_infos)

all_data = full_infos[0].find_all('fieldset')
# print(len(all_data))
counter = 0

# print(len(all_data))

# dls = all_data[0].find_all('dl')
# print(len(dls))

# print(all_data[0].dl.dt.text)
# print(all_data[0].dl.dd.text)

# d = {}
# key = input('key? ')
# value = input('value? ')
# d[key] = value

real_data = {}
count = 0
count1 = 0
# dlss = all_data[1].find_all('dl')
# # print(len(dlss))
# print(dlss[0].dt.text)
# print(dlss[0].dd.text)

for fieldset in all_data:
    dlss = fieldset.find_all('dl')
    for dls in dlss:
        key = dls.dt.text
        value = dls.dd.text
        real_data[key] = value

print(real_data.get('GPU Series'))

    # print(real_data.keys())

import csv
csv_columns = ['Brand', 'Series', 'Model', 'Interface', 'Chipset Manufacturer', 'GPU Series', 'GPU', 'Core Clock',
                   'Boost Clock', 'Stream Processors', 'Effective Memory Clock', 'Memory Size', 'Memory Interface',
                   'Memory Type', 'OpenGL', 'HDMI', 'Multi-Monitor Support', 'DisplayPort', 'Max Resolution', 'CrossFireX Support',
                   'Virtual Reality Ready', 'Cooler', 'System Requirements', 'Power Connector', 'HDCP Ready', 'Features',
                   'Max GPU Length', 'Card Dimensions (L x H)', 'Slot Width', 'Package Contents']

csv_file = "Names.csv"
    # try:
    #     with open(csv_file, 'w') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #         writer.writeheader()
    #         writer.writerow(real_data)
    # except IOError:
    #     print("IOError")
try:
    with open(csv_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writerow(real_data)
except IOError:
    print("IOError")

    # print(real_data)
