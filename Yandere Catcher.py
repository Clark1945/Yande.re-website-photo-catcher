import requests
from bs4 import BeautifulSoup
import os

Keyword=input('請輸入作品/畫家名稱(以羅馬拼音)：')

url="https://yande.re/post?page=1&tags="+Keyword
url2="https://yande.re"
re=requests.get(url)
soup=BeautifulSoup(re.text,'html.parser')
soupFindPage=soup.find_all('div',{'class':'pagination'})
Page=""
for x in soupFindPage:
        Page=x.text
NPage=int(Page[-8:-6].strip())
# print(NPage)
# print(Npage)

for y in range(1,NPage+1):
    url="https://yande.re/post?page="+str(y)+"&tags="+Keyword
    url2="https://yande.re"
    re=requests.get(url)
    soup=BeautifulSoup(re.text,'html.parser')
    soupFind=soup.find_all('a',{'class':'thumb'})
    
    pic=[]
    for x in soupFind:
        string=""
        tem=x.get('href')
        string=url2+tem
        pic.append(string)
    
    for y in pic:
        re2=requests.get(y)
        soup2=BeautifulSoup(re2.text,'html.parser')
        soupFind2=soup2.find_all('img',id='image')
        pic2=[]
        for gg in soupFind2:
            temp=gg.get('src')
            pic2.append(temp)
        for gh in pic2: 
            K=gh.find('/yande.re')
            gh2=gh[72:]
            r=requests.get(gh)
            if not os.path.exists("D:\\python題目\Yandere實驗"+"\\" +Keyword):
                os.mkdir("D:\\python題目\Yandere實驗"+"\\" +Keyword)
            os.chdir("D:\\python題目\Yandere實驗"+"\\" +Keyword)
            with open(gh2,'wb') as f:
                f.write(r.content)