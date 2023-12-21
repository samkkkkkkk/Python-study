from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
import time

import mysql.connector

# DB접속을 위한 정보 세팅 
mydb = mysql.connector.connect(
    host= 'localhost',
    user='root',
    passwd = 'mysql',
    database ='jpa'
)

# sql 실행을 위한 커서 생성
mycursor = mydb.cursor()



# user-agent 정보를 변환해 주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
# pip install fake_useragent
from fake_useragent import UserAgent

# 요청 헤더 정보를 꺼내올 수 있는 모듈
import urllib.request as req

# User Agent 정보 변환 (필수는 아닙니다.)
opener = req.build_opener() # 헤더 정보를 초기화
opener.addheaders = [('User-agent', UserAgent().edge)]
req.install_opener(opener) # 새로운 헤더 정보를 삽입

# 크롬 드라이버에게 전달할 옵션 설정.
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# 브라우저 안뜨게 하기
# options.add_argument('--headless')

# 크롬 드라이버를 버전에 맞게 자동으로 지원해주는 객체
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버 구동
browser = webdriver.Chrome(service=service, options=options)

# 브라우저 사이즈 조정
browser.set_window_size(800, 600)

# 페이지 이동 (베스트셀러 페이지)
browser.get(r'https://100.daum.net/encyclopedia/view/66XXXXXXX667')

browser.implicitly_wait(10)

cur_page_num = 1
target_page_num =33
click_num = 1

# while True:
soup = BeautifulSoup(browser.page_source, 'html.parser')
# browser.find_element(By.XPATH, f'//*[@id="mArticle"]/div/ul/li[1]/div/strong/a').click()
browser.implicitly_wait(10)
conut = 0

h3 = soup.find('h3').text
print(h3)
a = soup.find('a', class_='link_figure')
img_url = a.select_one('img')
print(img_url['src'])
# d = soup.find_all('div', class_='info_cont info_details')
# d = soup.find_all('div', class_='info_desc')
table = soup.find_all('table', class_='list_summary')
# print(table)

for a in table:
    th =a.select('th')
    td = a.select('td')
    # print(tr[3].text.strip())
    # print(tr[4].text.strip())
    count = 0
    while count < len(th):
        while count < len(td):
            # print(th[count].text.strip() + " " + td[count].text.strip())            
            count += 1
        
soup = BeautifulSoup(browser.page_source, 'html.parser')

recipe_div = soup.find_all('div', class_='section_desc')

for recipe_div_detail in recipe_div:
    recipe = recipe_div_detail.select('h4')
    print(recipe)
# print(recipe_div)
# recipe = recipe_div.select_one('p.desc_section').text
# print(recipe)


# for z in tr:
#     x = z.select('tr')
    # print(x)
    # recipe = x[3].text.split()
    # print(recipe)

# for k in recipe:
#     main_recipe = k[0]
#     recipe_detail = k
#     print(main_recipe)


# for t in p:
#     y = t.select('td')


#     name = y[3].text.strip()
#     print(name)


# recipe = a.find('tbody')
# print(recipe)

# for a in d:
#     div = a.select('span', class_='cont_summary')
#     tbody = div.select
    # print(recipe)
# print(d)
# browser.close()
# //*[@id="mArticle"]/div/div[2]/table/tbody/tr[4]/th/span
# //*[@id="mArticle"]/div/div[2]/table/tbody/tr[4]/td

