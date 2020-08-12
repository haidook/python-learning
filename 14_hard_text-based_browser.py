from pathlib import Path
import argparse
import requests
from bs4 import BeautifulSoup
import colorama

parser = argparse.ArgumentParser(description='Save webpages')
parser.add_argument("directory", help="create new directory")
args = parser.parse_args()

dir_name = args.directory
a = Path(dir_name)
a.mkdir(parents=True, exist_ok=True)
webpages = []

# while True:
#     link = input()
#     web_name = link.replace('.', '_')
#     if link == 'exit':
#         exit()
#     if link == 'back':
#         with open(f'{dir_name}/{webpages[-2]}.txt') as f:
#             print(f.read())
#     elif '.' in link:
#         # print(f'{web_name=}')
#         if web_name == 'bloomberg_com' or web_name == 'nytimes_com':
#             name = link.split('.')[0]
#             with open(f'{dir_name}/{name}.txt', 'w+') as f:
#                 if name == 'bloomberg':
#                     f.write(bloomberg_com)
#                 if name == 'nytimes':
#                     f.write(nytimes_com)
#             webpages.append(name)
#             with open(f'{dir_name}/{name}.txt') as f:
#                 print(f.read())
#         else:
#             print('Error: Webpage does not exist')
#     elif link in webpages:
#         with open(f'{dir_name}/{name}.txt') as f:
#             print(f.read())
#     elif link not in webpages:
#         print('Error: Incorrect URL')

def read_page(url):
    colorama.init()
    r = requests.get(full_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for x in soup.body.div.find_all('a'):
        print(x.text)
    # print(soup.body.h1.text)
    tags = ['h1', 'h2', 'h3', 'h4', 'a', 'p', 'ol', 'ul', 'li']
    # test = soup.find('body').find('div', 'body').findChildren()
    test = soup.find('html').findChildren()
    page = []
    for x in test:
        if x.name in tags:
            page.append(colorama.Fore.BLUE + x.text)
    return page

# print(colorama.Fore.BLUE + 'some red text')
while True:
    url = input()#'docs.python.org'#
    if url == 'exit':
        exit()
    if url.startswith('htt'):
        full_url = url
    else:
        full_url = 'https://' + url

    name = url.replace('.', '_')
    web_name = url.split('.')[0]
    # print(f'{full_url=}')
    # print(f'{web_name=}')
    # print(web_name in webpages)

    if web_name in webpages:
        with open(f'{dir_name}/{web_name}.txt') as f:
            print(f.read())

    elif '.' in url:
        r = requests.get(full_url)
        # soup = BeautifulSoup(r.content, 'html.parser')
        # for x in soup.body.div.find_all('a'):
        #     print(x.text)
        # # print(soup.body.h1.text)
        # tags = ['h1', 'h2', 'h3', 'h4', 'a', 'p', 'ol', 'ul', 'li']
        # # test = soup.find('body').find('div', 'body').findChildren()
        # test = soup.find('html').findChildren()
        # for x in test:
        #     if x.name in tags:
        #         print(x.text)
        yeap = read_page((full_url))
        for x in yeap:
            print(x)
        with open(f'{dir_name}/{web_name}.txt', 'w+') as f:
            for x in yeap:
                f.write(x)
            webpages.append(web_name)
        with open(f'{dir_name}/{web_name}.txt') as f:
            print(f.read())
    elif web_name not in webpages:
        print('Error: Incorrect URL')
    # print(webpages)
