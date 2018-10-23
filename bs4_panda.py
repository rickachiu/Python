import requests
import pandas as pd
from bs4 import BeautifulSoup

#send request
url = 'https://www.zillow.com/homes/for_sale/Rancho-Cucamonga-CA-91730'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# review text element
review_text_elem = soup.find_all(class_='listing-street-address')
print(review_text_elem)
review_text = []
for item in review_text_elem:
review_text.append(item.text)
print(review_text)