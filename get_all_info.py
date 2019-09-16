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

    # print(len(link))
    # print(len(title))
    real_data = {}
    csv_columns = ['Brand', 'Series', 'Model', 'Interface', 'Chipset Manufacturer', 'GPU Series', 'GPU', 'Core Clock',
                    'Boost Clock', 'Stream Processors', 'Effective Memory Clock', 'Memory Size', 'Memory Interface',
                    'Memory Type', 'OpenGL', 'HDMI', 'Multi-Monitor Support', 'DisplayPort', 'Max Resolution', 'CrossFireX Support',
                    'Virtual Reality Ready', 'Cooler', 'System Requirements', 'Power Connector', 'HDCP Ready', 'Features',
                    'Max GPU Length', 'Card Dimensions (L x H)', 'Slot Width', 'Package Contents', 'CUDA Cores','DirectX','SLI Support',
                    'Form Factor', 'Other Ports', 'Thermal Design Power','Eyefinity Support', 'DVI', 'Dual-Link DVI Supported','Operating Systems Supported',
                    'Link']

    csv_file = "Names.csv"
    # print(len(link))
    for link in links:
        new_connection = urlopen(link)
        page_html = new_connection.read()
        page_soup = BeautifulSoup(page_html, "html.parser")
        full_infos = page_soup.find_all('div', {'class': 'plinks'})
        all_data = full_infos[0].find_all('fieldset')
        # print(len(all_data))
        try:
            for fieldset in all_data:
                print()
                print("@")
                dlss = fieldset.find_all('dl')
                try:
                    for dls in dlss:
                        print("*", end="")
                        key = dls.dt.text
                        value = dls.dd.text
                        real_data[key] = value       
                except IOError:
                    print("IOError in dls")   
            with open(csv_file, 'a') as csvfile:
                    real_data['Link'] = link
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writerow(real_data)              
        except IOError:
            print("IOError in fieldset")            
except IOError:
    print("IOError in main links")                
         
