import requests
import urllib.parse
import json
from bs4 import BeautifulSoup
import os

def createcss(title):
    with open('main.css','r',encoding='utf-8') as f:
        css = f.read()
    with open('./'+title+'/main.css','w',encoding='utf-8') as f:
        f.write(css)
        print(title+'.css')
def xiazaiyemian(url,title):
    if not os.path.exists(title):
        os.makedirs(title)
        print("Create")
    url = url
    baijing = requests.get(url).text
    with open('./'+title+'/index.html', 'w', encoding='utf-8') as f:
        f.write(baijing)
        print(title+'.html')
    createcss(title)

L = []
S = []
url = 'https://soraties.pages.dev/OutOfPlan/'
neirong = requests.get(url).text
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(neirong)
    print('index.html')
soup = BeautifulSoup(neirong, 'html.parser')
for a_tag in soup.find_all('a', href=True):
    href_value = a_tag['href']
    L.append(href_value)
    span_text = a_tag.find('span').get_text(strip=True) if a_tag.find('span') else 'No Span Text'
    S.append(span_text)
    print(f"Link: {href_value}, Span Text: {span_text}")

qd = len(L)
for i in range(1,qd):
    yuban = L[i]
    yuban = yuban[2:]
   # print(f"\'{yuban}\',")
    yubanurl = url + yuban+'/'
    xiazaiyemian(yubanurl,yuban)
    certain = requests.get(yubanurl).text
    youlinaixv = BeautifulSoup(certain, 'html.parser')
    for img_tag in youlinaixv.find_all('img', src=True):
        img_src = img_tag['src']
        img_url = yubanurl + img_src
        img_name = img_src[7:]
        filepath = './'+yuban+'/'+'images'+'/'
        if not os.path.exists(yuban+'/'+'images'):
            os.makedirs(yuban+'/'+'images')
            print("Create")
        if os.path.exists(filepath+img_name):
            print(img_name+'已存在')
        else:
            with open(filepath+img_name, 'wb') as f:
                f.write(requests.get(img_url).content)
                print(img_name)
       