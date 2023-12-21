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

# 페이지 이동
browser.get(r'https://map.naver.com/p/search/%EB%B6%80%EB%8F%99%EC%82%B0?c=15.00,0,0,0,dh')

soup = BeautifulSoup(browser.page_source, 'html.parser')

browser.implicitly_wait(10)

browser.find_element(By.XPATH, f'//*[@id="_pcmap_list_scroll_container"]/ul/li[1]').click()
browser.implicitly_wait(10)
soup = BeautifulSoup(browser.page_source, 'html.parser')
naver_div = soup.find_all('div', id='_pcmap_list_scroll_container')
print(naver_div)