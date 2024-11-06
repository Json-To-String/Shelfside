from bs4 import BeautifulSoup
import re
import requests


def get_categories(url) -> 'List':
    '''
    Params: str: Board game url (ex: https://boardgamegeek.com/xmlapi/boardgame/{gameID})

    Returns: List: List of categories
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    cat_text = soup.find_all('boardgamecategory')
    cat_list = []
    for cats in cat_text:
        s = str(cats)

        # extract important text between <stuff> important text </stuff>
        c = re.sub(r'<[^>]+>', '', s)
        cat_list.append(c)

    return(cat_list)

def get_description(url) -> 'str':
    '''
    Params: str: Board game url (ex: https://boardgamegeek.com/xmlapi/boardgame/{gameID})

    Returns: str: string of description
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    cat_text = soup.find_all('description')

    return(cat_text)

def get_thumbnail(url) -> 'str':
    '''
    Params: str: Board game url (ex: https://boardgamegeek.com/xmlapi/boardgame/{gameID})

    Returns: str: string of thumbnail
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='lxml')

    cat_text = soup.find_all('thumbnail')

    s = str(cat_text)
    result = re.sub(r'<[^>]+>', '', s)
    return(result)

result = get_thumbnail('https://boardgamegeek.com/xmlapi/boardgame/13')
print(result)
