
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui

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

# 페이지 이동
target_page = f'https://100.daum.net/book/630/list'
browser.get(target_page)

browser.implicitly_wait(10)

num = 1
page_num = 1
while True:
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    b = soup.find('ul', class_='list_register') # 각항목으로 이동할 url 뒷부분 가져오기
    browser.implicitly_wait(10)
    
    a = b.select('li') 
    # a 태그의 href값을 추출하여 url 완성
    for c in a:
        d = c.select_one('a')['href'] 
        
        browser.get('https://100.daum.net' + d)

        soup = BeautifulSoup(browser.page_source, 'html.parser')

        browser.implicitly_wait(10)
        
        browser.implicitly_wait(10)
        h3 = soup.find('h3').text.strip() # 칵테일 이름이 있는 h3 태그에서 text 추출 후 공백 제거
        cocktail_name = h3 
        print(cocktail_name)
        a = soup.find('a', class_='link_figure') # img url이 있는 a 태그 찾기
        img_url = a.select_one('img') # a태그에서 img 태그 찾기
        
        cocktail_img = img_url['src'] #img 태그의 src 값만 가져오기
        print(cocktail_img)
        table = soup.find_all('table', class_='list_summary') # 제조방법이 있는 table 찾기
        
        
        recipe = ''
        for a in table:
            th =a.select('th')
            td = a.select('td')
            
            
            count = 0
            
            # th와 td의 인덱스 값을 이용하여 연관된 값들 연결하기
            while count < len(th):
                while count < len(td):
                    
                    recipe1 = th[count].text.strip()
                    recipe2 = td[count].text.strip()
                    recipe += recipe1 + ' ' + recipe2
                    if count < len(td)-1:
                        recipe += '/' # 나중에 '/'를 기준으로 replace()사용할 예정
                                
                    count += 1
                
        print(recipe)

        # 유래 및 만드는 법 가져오기
        recipe_div = soup.find_all('div', class_='section_desc')
        recipe_detail = ''
        for recipe_div_detail in recipe_div:
            recipe_ex = recipe_div_detail.select_one('h4').text.strip()
            recipe_discrip = recipe_div_detail.select_one('p', class_='desc_section').text.strip()
            
            recipe_detail += '/' +recipe_ex + '/' + recipe_discrip
            
        print(recipe_detail)
        print('===========================')
        # pyautogui.hotkey('alt', 'left')
        browser.back()
        browser.implicitly_wait(10)

        # DB에 저장
        query = 'INSERT INTO tbl_recipe (cocktail_name, cocktail_img, recipe, recipe_detail) VALUES(%s, %s, %s, %s)'
        values = (cocktail_name, cocktail_img, recipe, recipe_detail)
        
        mycursor.execute(query, values)

        
    
    mydb.commit()
    # num이 43일 때는 클릭할 요소가 없음
    if num < 43:
        browser.find_element(By.XPATH, f'//*[@id="mArticle"]/div/div[3]/span/a[{page_num}]').click()
    page_num += 1
    if page_num == 12:
        page_num = 2
    elif num == 10:
        page_num = 2
    
    num += 1

    if num == 44:
        break # while True 탈출
    

browser.close()
mycursor.close()
mydb.close()