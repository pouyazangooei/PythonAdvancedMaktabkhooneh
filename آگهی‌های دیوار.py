import requests
from bs4 import BeautifulSoup
import arabic_reshaper
from bidi.algorithm import get_display

r = requests.get('https://divar.ir/s/tehran/jobs')
soup = BeautifulSoup(r.text, 'html.parser')
ads = soup.find_all('div', attrs={'class': 'kt-post-card__body'})
for item in ads:
    ad_title_element = item.find('h2', class_='kt-post-card__title')
    ad_description_element = item.find('div', class_='kt-post-card__description')
    if ad_title_element and ad_description_element:
        ad_title = ad_title_element.text.strip()
        ad_description = ad_description_element.text.strip()
        
        ad_title_reshaped = get_display(arabic_reshaper.reshape(ad_title))
        ad_description_reshaped = get_display(arabic_reshaper.reshape(ad_description))
        if 'ﯽﻘﻓﺍﻮﺗ' in ad_description_reshaped:
            print("Title:", ad_title_reshaped)
