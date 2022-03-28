import requests
from bs4 import BeautifulSoup



def scraping(my_url):
    """

    """

    url = my_url 
    response = requests.get(url)
    html = response.content

    return BeautifulSoup(html, 'html.parser') 

# if __name__ == '__main__':
#     print('Starting scrapping')