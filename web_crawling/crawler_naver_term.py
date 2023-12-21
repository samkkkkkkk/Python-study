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
browser.get('https://terms.naver.com/list.naver?cid=48182&categoryId=48272&page=1')

browser.implicitly_wait(10)

cur_page_num = 1
target_page_num =33
click_num = 1

while True:
    soup = BeautifulSoup(browser.page_source, 'html.parser') 
        # //*[@id="content"]/div[3]/ul/li[1]/div[2]/div[1]/strong/a[1]
        # //*[@id="content"]/div[3]/ul/li[1]/div[2]/div[1]/strong/a[1]
        # //*[@id="content"]/div[3]/ul/li[2]/div[2]/div[1]/strong/a[1]
        

    browser.find_element(By.XPATH, f'//*[@id="content"]/div[3]/ul/li[{click_num}]/div[2]/div[1]/strong/a[1]').click()
    # browser.implicitly_wait(10)
    time.sleep(2)

    cocktail_name_all = soup.find_all('#content')
    for cocktail_name in cocktail_name_all:
        browser.implicitly_wait(10)
        name = cocktail_name.select_one('div.image_area a').text
        print("1", name)

        time.sleep(2)
        pyautogui.hotkey('alt', 'left')
            # browser.implicitly_wait(1)
        click_num += 1
        
   
    # click_num += 1
    # print(div)
    # //*[@id="content"]/div[2]/div[1]/h2
    # //*[@id="content"]/div[2]/div[1]/h2
# browser.close()

