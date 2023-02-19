import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://vandal.elespanol.com/noticias/videojuegos')
soup = BeautifulSoup(res.text, 'html.parser') # Convert the request from a string to html

links = soup.select('.mt1 .caja620 >a')  
subtext = soup.select('.fleft .mr05')


def sort_stories_by_comments(hnlist):
    return sorted(hnlist, key=lambda k: k['comments'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].getText()
        hn.append({'title': title, 'link': href, 'comments': int(vote)})
    return sort_stories_by_comments(hn)


pprint.pprint(create_custom_hn(links,subtext ))