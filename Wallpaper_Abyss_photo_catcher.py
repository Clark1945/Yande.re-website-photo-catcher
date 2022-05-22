import requests,os,time,re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

insert_url = "https://wall.alphacoders.com/by_sub_category.php?id=315662&name=Elden+Ring+Wallpapers"#input('請輸入URL')
Keyword = input("請輸入儲存資料夾名稱")
req = requests.get(insert_url)
print(req)

soup = BeautifulSoup(req.text,'html.parser')
total_pic=soup.find('meta',{'name':'description'}).get('content')
pic_amount = re.search(r'\d+',total_pic).group()
#print(pic_amount)#找出全圖片的數量
pic_page=int(int(pic_amount)/30)
print(pic_page)

options = Options()
options.add_argument("--disable-notifications")
#取消網頁的彈出視窗


chrome = webdriver.Chrome('./chromedriver', chrome_options=options)#建立webdriver物件，傳入瀏覽器驅動物件及瀏覽器設定。
chrome.get("https://wall.alphacoders.com/by_sub_category.php?id=315662&name=Elden+Ring+Wallpapers")

for x in range(1, pic_page+3):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
#執行滾動捲軸，一次停擺5秒

soup2 = BeautifulSoup(chrome.page_source, 'html.parser')

soupFindPage = soup2.find_all('div',{'class':'boxgrid'})
now_dir = os.path.dirname(__file__)#顯示當前目錄
for href in soupFindPage:
    c = href.a.picture.source.get("srcset")  #從srcset取得字串
    #print(c)
    front_url = c[:36]
    if front_url.endswith("t"):
        front_url = c[:35]
    #print(front_url)
    combine_url = front_url + c[-12:-5]+".jpg"
    #print(combine_url)  #取得全長URL
    output_url = requests.get(combine_url) #用Requests 重新get URL
    if not os.path.exists(now_dir+"\\"+Keyword):
        os.mkdir("./" +Keyword)
        os.chdir(now_dir+"\\" +Keyword)
    #print(output_url)
    with open(c[-12:-5]+".jpg",'wb') as f:  #選擇檔名並儲存
        f.write(output_url.content)
print("擷取完成！")
chrome.quit()