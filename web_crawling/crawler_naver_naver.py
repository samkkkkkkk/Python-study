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
browser.get(f'https://map.naver.com/p/search/%EC%88%A0%EC%A7%91?c=13.00,0,0,0,dh')

browser.implicitly_wait(10)

# browser.switch_to.frame('searchIframe')
# 카테고리 창으로 이동
# browser.find_element(By.XPATH, f'//*[@id="app-root"]/div/div[1]/div/div/div/div/div/span[1]/a').click() 
# browser.implicitly_wait(10)
# 혼술 선택
# browser.find_element(By.XPATH, f'//*[@id="_place_portal_root"]/div/div[2]/div[1]/div/div/div[7]/div[2]/span[6]/a').click()
# browser.implicitly_wait(10)

# browser.switch_to.iframe(browser.find_element(By.CSS_SELECTOR('iframe#searchIframe')))
# frame_num = browser.find_elements(By.CSS_SELECTOR, 'iframe#searchIframe')
browser.switch_to.frame('searchIframe')
browser.find_element(By.XPATH, f'//*[@id="app-root"]/div/div[1]/div/div/div/div/div/span[1]/a').click() 
browser.implicitly_wait(10)
pyautogui.press('end', presses=2, interval=0.5)
browser.implicitly_wait(10)
browser.find_element(By.XPATH, f'//*[@id="_place_portal_root"]/div/div[2]/div[1]/div/div/div[7]/div[2]/span[6]/a').click()
browser.implicitly_wait(10)
time.sleep(1)
browser.find_element(By.XPATH, f'//*[@id="_place_portal_root"]/div/div[2]/div[2]/a[2]').click()
browser.implicitly_wait(20)
# time.sleep(2)  # Add a short delay to let the content load
soup = BeautifulSoup(browser.page_source, 'html.parser')

# scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
# browser.execute_script(scroll_script)
browser.implicitly_wait(10)
# browser.find_element(By.XPATH, f'//*[@id="_pcmap_list_scroll_container"]/ul/li[2]/div[1]/div[2]/div/span[1]').click()
# scroll_container =browser.find_element(By.ID, '_pcmap_list_scroll_container')
# browser.implicitly_wait(10)
# try:
#     while True:
#         for i in range(7):
#             browser.execute_script("arguments[0].scrollBy(0,2000)",scroll_container)
#             browser.implicitly_wait(10)
#         break

# except:
#     print('오류')
browser.find_element(By.XPATH, f'//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/div[2]/div/span[1]').click()
pyautogui.press('pagedown', presses = 100, interval=0.01) # 스크롤 맨 아래로 내리기
browser.implicitly_wait(20)
pyautogui.press('home', presses=3, interval=0.5)
browser.implicitly_wait(10)
pyautogui.press('pagedown', presses = 100, interval=0.01) # 스크롤 맨 아래로 내리기
browser.implicitly_wait(20)
pyautogui.press('end', presses = 5, interval=0.5)
browser.implicitly_wait(10)
pyautogui.press('home', presses=3, interval=0.5)
browser.implicitly_wait(10)
soup = BeautifulSoup(browser.page_source, 'html.parser')
browser.implicitly_wait(10)
time.sleep(4)

#검색결과가 모두 보이지 않기 때문에 page down을 눌러 끝까지 펼쳐준다.
# for scroll in range(0,30):
#     browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.2)
# browser.switch_to.frame('searchIframe')

#entryIframe

# div = soup.select('li.UEzoS')

# for a in div:
#     print(a.select_one('div.K0PDV'))

# print(len(div))
# for div_li in div:

# #     print(div_li.select_one('span'))
# place_name = list()
# img_url = list()
# place_address1 = list()
# div = soup.select('div#_pcmap_list_scroll_container ul > li')
# print(len(div))

# for div_li in div:
#     # browser.find_element(By.CLASS_NAME, 'TYaxT').click()
#     # browser.implicitly_wait(10)
#     # browser.switch_to.frame('entryIframe')
#     # browser.implicitly_wait(10)
#     # browser.find_element(By.CLASS_NAME, '_UCia').click()
#     # browser.implicitly_wait(10)
#     # print(soup.select_one('div.Y31Sf'))
#     place_name.append(div_li.select_one('div.K0PDV span.place_blind').text)
#     # browser.switch_to.frame('searchIframe')
#     browser.implicitly_wait(10)
#     # place_name = div_li.select_one('div.K0PDV span.place_blind').text

#     # print(place_name)
#     # print(div_li.select_one('div.K0PDV span.place_blind'))
#     img_url.append(str(div_li.select_one('div.K0PDV')).split('url(')[1].split(');')[0])
#     # print(img_url)
#     # print(str(div_li.select_one('div.K0PDV')).split('url(')[1].split(');')[0])

#     # browser.find_element(By.CLASS_NAME, 'TYaxT').click()
#     # browser.implicitly_wait(10)
#     # browser.switch_to.default_content()
#     # browser.switch_to.frame('entryIframe')
#     # browser.switch_to.default_content()
#     # browser.switch_to.frame('searchIframe')
#     # browser.implicitly_wait(10)
#     # browser.back()
#     # # browser.find_element(By.XPATH, f'//*[@id="app-root"]/div/div/header/a/svg').click()
#     # browser.implicitly_wait(10)

#     # soup = BeautifulSoup(browser.page_source, 'html.parser')
#     # print(soup.select_one('div.place_section_content span').text)
# # browser.close()
