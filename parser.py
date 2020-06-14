import requests
from bs4 import BeautifulSoup

url = 'https://999.md/ru/list/real-estate/apartments-and-rooms?applied=1&eo=12900&eo=12912&eo=12885&eo=13859&o_32_9_12900_13859=15667&ef=33&o_33_1=776&ef=31&r_31_2_from=15000&r_31_2_to=&r_31_2_unit=eur&r_31_2_negotiable=yes&ef=1073&r_1073_244_from=60&r_1073_244_to=60&r_1073_244_unit=m2'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

output = []

for each in soup.find('ul', {'class': 'ads-list-photo large-photo'}):
    title = soup.find_all('div', {'class': 'ads-list-photo-item-title'})
    price = soup.find_all('div', {'class': 'ads-list-photo-item-price-wrapper'})
    outlist = [title, price]
    output.append(outlist)

#print(title)
#print(str(title) + ' ' + str(price))
print(output)
#li.ads-list-photo-item