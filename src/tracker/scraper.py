import requests
from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError


def get_data_from_jumia(url):
    try:
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        bs = BeautifulSoup(page.content, 'html.parser')
        price = bs.find("span", {'class': "-b -ltr -tal -fs24"}).get_text().replace("₦", '').strip().replace(',', '')
        title = bs.find("h1", {'class': '-fs20 -pts -pbxs'}).get_text()
        clean_price = int(price)
    except:
        return ValidationError('The Url you entered is not for jumia, please double check')
    return {"price": clean_price, "title": title}

# get_data_from_jumia(url)

    # User Agent = Mozilla/5.0

# https://www.jumia.com.ng/fashion-mens-slip-on-sneakers-black-63622762.html

# <h1 class="-fs20 -pts -pbxs">Panda 32" Inch LED TV, HD Ready</h1>