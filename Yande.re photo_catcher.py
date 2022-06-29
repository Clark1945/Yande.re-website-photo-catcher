import requests
from bs4 import BeautifulSoup
import os

fictionName=input('請輸入作品名稱：')

frontUrl="https://yande.re/post?page="
endUrl="&tags="+fictionName
url=frontUrl+"1"+endUrl

url2="https://yande.re"
re=requests.get(url)
soup=BeautifulSoup(re.text,'html.parser')
surl=url.find("page=")
eurl=url.find("&tags")
nowPage=url[surl+5:eurl]
#print(nowPage)當前頁
totalPage=soup.find("div",{"role":"navigation"}).find_all("a")[-2].text
#print(totalPage)總共頁

now_dir = os.path.dirname(__file__)
if not os.path.exists(fictionName):
    os.mkdir(fictionName)
os.chdir(now_dir+"\\" +fictionName)

for nPage in range(3,int(totalPage)+1):
    re=requests.get(frontUrl+str(nPage)+endUrl)
    soup=BeautifulSoup(re.text,'html.parser')
    soupFind=soup.find_all('a',{'class':'thumb'}) 
    #print(soupFind)
    pic=[]
    pic_count = 0
    for x in soupFind:
        string=""
        tem=x.get('href')
        string=url2+tem
        pic.append(string)
        #每個圖片網址的URL
    for y in pic:
        re2=requests.get(y)
        soup2=BeautifulSoup(re2.text,'html.parser')
        soupFind2=soup2.find_all('img',id='image')
        pic2=[]
        for gg in soupFind2:
           temp=gg.get('src')
           
        #print(temp) 
        gh=temp[72:80]+".jpg"
        #print(gh)
        r=requests.get(temp)
        with open(gh,'wb') as f:   
            f.write(r.content)
        pic_count +=1
        print("擷取第%s頁，第%d張中......" %(nPage,pic_count))
                
print("擷取完成！")