import requests
from bs4 import BeautifulSoup
import os

insert_url = input('請輸入URL')
Keyword = input("請輸入儲存資料夾名稱")
re = requests.get(insert_url)
#print(re)
soup = BeautifulSoup(re.text,'html.parser')
soupFindPage = soup.find_all('div',{'class':'boxgrid'})
now_dir = os.path.dirname(__file__)#顯示當前目錄
for href in soupFindPage:
    c = href.a.picture.source.get("srcset")  #從srcset取得字串
    # print(c)
    front_url = c[:36]
    if front_url.endswith("t"):
        front_url = c[:35]
    # print(front_url)
    combine_url = front_url + c[-12:-5]+".jpg"
    # print(combine_url)  #取得全長URL
    output_url = requests.get(combine_url) #用Requests 重新get URL
    if not os.path.exists(now_dir+"\\"+Keyword):
        os.mkdir("./" +Keyword)
        os.chdir(now_dir+"\\" +Keyword)
    # print(output_url)
    with open(c[-12:-5]+".jpg",'wb') as f:  #選擇檔名並儲存
        f.write(output_url.content)
print("擷取完成！")
                
                