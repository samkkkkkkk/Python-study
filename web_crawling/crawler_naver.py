# selenium import
from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import urllib.request as req
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import codecs
from selenium.webdriver.common.keys import Keys
import time
import pyautogui


d = datetime.today()

file_path = f'C:/test/네이버_혼술{d.year}년{d.month}월{d.day}일{d.hour}시기준.txt'
# 헤더 정보 초기화
opener = req.build_opener()
# User Agent 정보
opener.addheaders = [('User-agent', UserAgent().edge)]
# 헤더 정보 삽입
req.install_opener(opener)


# 크롬 드라이버에게 전달할 옵션 설정.
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


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



soup = BeautifulSoup(browser.page_source, 'html.parser')

    # _pcmap_list_scroll_container
    
    # map_list = soup.find('div', id='pcmap_list_scroll_container')
    # print(map_list)
    #body부분을 잡기 위해 쓸데없이 버튼을 클릭해줌

# //*[@id="mArticle"]/div/div[3]/span/em/span
# //*[@id="mArticle"]/div/div[3]/span/a[1]
# //*[@id="mArticle"]/div/div[3]/span/a[2]
# //*[@id="mArticle"]/div/div[3]/span/a[9]
# //*[@id="mArticle"]/div/div[3]/span/a[10]

# browser.find_element(By.XPATH, '//*[@id="mArticle"]/div/ul/li[1]/div/a/span').click()
browser.implicitly_wait(10)
# browser.find_element(By.XPATH, '//*[@id="mArticle"]/div/div[1]/div/div/div[1]/h3/span').click()
browser.implicitly_wait(10)
# browser.execute_script("window.scrollTo(0, 200)")

b = soup.find('ul', class_='list_register')
browser.implicitly_wait(10)
# print(b)
a = b.select('li')
for c in a:
    d = c.find('a')['href']
    print(d)



    #검색결과가 모두 보이지 않기 때문에 page down을 눌러 끝까지 펼쳐준다.
    # for scroll in range(0,30):
    #     browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    #     time.sleep(0.2)
# pyautogui.hotkey('alt', 'left')
    
    # next_iframe = browser.find_element('#searchIframe')
 
   


   

    

    # f.write(f'# 순위: {rank}\n')
    # f.write(f'# 가수명: {artist_name}\n')
    # f.write(f'# 앨범명: {album_name}\n')
    # f.write(f'# 노래 제목: {song_name}\n')
    # f.write('-' * 40 + '\n')


# browser.close()