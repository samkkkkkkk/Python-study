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

'''
- with문을 사용하면 with 블록을 벗어나는 순간
 객체가 자동으로 해제됩니다. (자바의 try with resource와 비슷)

- with 작성 시 사용할 객체의 이름을 as 뒤에 작성해 줍니다.
'''

# 페이지 이동
target_page = f'https://100.daum.net/book/630/list'
browser.get(target_page)

browser.implicitly_wait(10)

num = 1
page_num = 1
while True:
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    b = soup.find('ul', class_='list_register')
    browser.implicitly_wait(10)
    # print(b)
    a = b.select('li')
    for c in a:
        d = c.select_one('a')['href']
        # print(d)
        browser.get('https://100.daum.net' + d)

        soup = BeautifulSoup(browser.page_source, 'html.parser')

        browser.implicitly_wait(10)
        # browser.find_element(By.XPATH, f'//*[@id="mArticle"]/div/div[2]/table/tbody/tr[1]/td').click()
        browser.implicitly_wait(10)
        h3 = soup.find('h3').text
        print(h3)
        a = soup.find('a', class_='link_figure')
        img_url = a.select_one('img')
        print(img_url['src'])
        # d = soup.find_all('div', class_='info_cont info_details')
        # d = soup.find_all('div', class_='info_desc')
        table = soup.find_all('table', class_='list_summary')
        # print(table)

        # for a in table:
        #     tr =a.select('th')
        #     # if len(tr) == 5:
        #     #     print(tr[3].text.strip())
        #     #     print(tr[4].text.strip())
        #     # print(tr[3].text.strip())

        #     # if not tr[4] :
        #     #     print('')
        #     count = 0
        #     while count < len(tr):
        #         print(tr[count].text.strip())
        #         count +=1

        #     td =a.select('th')
        #     while count < len(tr):
        #         print(tr[count].text.strip())
        #         count +=1
        for a in table:
            th =a.select('th')
            td = a.select('td')
            # print(tr[3].text.strip())
            # print(tr[4].text.strip())
            count = 0
            while count < len(th):
                while count < len(td):
                    print(th[count].text.strip() + " " + td[count].text.strip())            
                    count += 1
# //*[@id="mArticle"]/div/div[3]/span/a[1]
# //*[@id="mArticle"]/div/div[3]/span/a[2]
# //*[@id="mArticle"]/div/div[3]/span/a[3]
        # recipe_div = soup.find('div', class_='section_desc')
        #     # print(recipe_div)
        # recipe = recipe_div.select_one('p.desc_section').text
        # print(recipe)
        recipe_div = soup.find_all('div', class_='section_desc')

        for recipe_div_detail in recipe_div:
            recipe = recipe_div_detail.select_one('h4').text.strip()
            recipe_detail = recipe_div_detail.select_one('p', class_='desc_section').text.strip()
            print(recipe)
            print(recipe_detail)
        print('===========================')
        # pyautogui.hotkey('alt', 'left')
        browser.back()
        browser.implicitly_wait(10)
    
    # browser.get(f'https://100.daum.net/book/630/list')
    browser.find_element(By.XPATH, f'//*[@id="mArticle"]/div/div[3]/span/a[{page_num}]').click()
    page_num += 1
    if page_num == 12:
        page_num = 2
    elif num == 10:
        page_num = 2
    

    num += 1

    print("==================\n\n==================\n\n=================\n num: ", num)
    # //*[@id="mArticle"]/div/div[3]/span/a[1]/span
    # //*[@id="mArticle"]/div/div[3]/span/a[2]/span
    if num == 44:
        break




#     query = 'INSERT INTO tbl_recipe (data_url) VALUES(%s)'
#     values = (d,)
        
#     mycursor.execute(query, values)

# mydb.commit()

# browser.close()
mycursor.close()
mydb.close()