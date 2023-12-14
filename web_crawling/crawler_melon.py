
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 엑셀 처리 모듈 임포트
# pip install xlsxwriter
import xlsxwriter

# user-agent 정보를 변환해 주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
# pip install fake_useragent
from fake_useragent import UserAgent

# 이미지를 바이트 변환 처리 모듈
from io import BytesIO

# 요청 헤더 정보를 꺼내올 수 있는 모듈
import urllib.request as req

d = datetime.today()

file_path = f'C:/test/멜론top100_{d.year}_{d.month}_{d.day}.xlsx'

# User Agent 정보 변환 (필수는 아닙니다.)
opener = req.build_opener # 헤더 정보를 초기화
opener.addheaders = [('User-agent', UserAgent().edge)]
req.install_opener(opener) # 새로운 헤더 정보를 삽입

# 엑셀 처리 선언
# Workbook 객체를 생성해서 엑셀파일을 하나 생성 (매개값으로 저장될 경로를 지정)
workbook = xlsxwriter.Workbook(file_path)

# 워크 시트 생성
worksheet = workbook.add_worksheet() # 워크시트를 만들어야 데이터를 넣을 수 있다.

# 크롬 드라이버에게 전달할 옵션 설정.
options = webdriver.ChromeOptions()
options.add_experimental_option

# 브라우저 안뜨게 하기
# options.add_argument('--headless')

# 크롬 드라이버를 버전에 맞게 자동으로 지워해주는 객체
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버 구동
browser = webdriver.Chrome(service=service, options=options)

# 브라우저 사이즈 조정
browser.set_window_size(800, 600)

# 페이지 이동 (베스트셀러 페이지)
browser.get('https://www.melon.com/chart/index.htm')

# 브라우저 내부 대기
# time.sleep(10) -> 브라우저 로딩에 상관없이 무조건 10초 대기

# 웹 페이지 전체가 로딩괼 때 까지 대기 후 남은 시간 무시
browser.implicitly_wait(10)



cur_page_num = 2 # 현재 페이지 번호
target_page_num = 9 # 목적지 페이지 번호
rank = 1 # 순위 
cnt = 2 # 엑셀 행 수 카운트 해줄 변수

while True:
    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    cnt += 1
    lst50_list = soup.find_all('tr', class_='lst50')

    for lst50 in lst50_list:
        div = lst50.select_one('div.wrap_song_info')
        # print(div)
        # 타이틀
        title = div.select_one('div.rank01 > span > a').text
        singer = div.select_one('div.rank02 > span > a').text
        book = div.select_one('div. > a').text.strip()

        print(title)
        print(singer)
        print(book)
    
    
    if cnt < 4:
        break
    
    
        

# //*[@id="lst50"]/td[6]/div/div/div[1]/span/a
# //*[@id="lst50"]/td[6]/div/div/div[2]/a
#//*[@id="lst50"]/td[6]/div/div/div[1]/span/a

# //*[@id="lst50"]/td[1]/div
# /html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[1]
# /html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[2]

        
#         # 작가 
#         # 위에서 얻은 title의 부모요소 li의 다음 형제 li를 지목 -> 작가, 출판사, 출판일 존재
#         author = title.find_parent().find_next_sibling()

#         # 작가쪽 영역 데이터 상세 분해
#         author_data = author.text.split('|')
#         author_name = author_data[0].strip()
#         company = author_data[1].strip()
#         pub_day = author_data[2].strip()

#         # 가격
#         price = author.find_next_sibling()
#         price_data = price.text.split(', ')[0]

#         # 책 상세 정보 페이지 링크
#         # title이라는 변수에 a태그를 지목해 놓은 상태
#         # title -> a태그의 요소 전부를 가지고 있는 상태.
#         # href로 작성된 키를 전달하고 해당 value를 받아 변수에 저장.
#         page_link = title['href']

#         try:
#             # 이미지 바이트 변환 처리
#             # ByteIO 객체의 매개값으로 아까 준비해 놓은 img 태그의 src값을 전달.
#             img_data = BytesIO(req.urlopen(img_url['src']).read())

#             # 엑셀에 이미지 저장
#             # worksheet.insert_image('배치할 셀 번호', 이미지제목, {'image_data':바이트로 변환한 이미지, 기타 속성...})
#             worksheet.insert_image(f'A{cnt}', img_url['src'], {'image_data':img_data, 'x_sacle':0.5, 'y_scale':0.5})
        
#         except:
#             # 파이썬에서는 블록구조에 아무것도 쓰지 않으면 에러입니다.
#             # 블록 구조 내부에 딱히 작성할 코드가 없어서 넘길 때
#             # pass라는 키워드를 사용합니다.
#             pass

#         # 엑셀에 나머지 텍스트 저장
#         worksheet.write(f'B{cnt}', title.text)
#         worksheet.write(f'C{cnt}', author_name)
#         worksheet.write(f'D{cnt}', company)
#         worksheet.write(f'E{cnt}', pub_day)
#         worksheet.write(f'F{cnt}', price_data)
#         worksheet.write(f'G{cnt}', page_link)        

#         # 다음 행에 다음 데이터를 배치하기 위해 cnt 값 증가
#         cnt += 1

#     # 다음 페이지(탭)로 전환
#     cur_page_num += 1 
#     browser.find_element(By.XPATH, f'//*[@id="newbg_body"]/div[3]/ul/li[{cur_page_num}]/a').click()
#     del soup # 다음페이지 넘어가기 전에 초기화
#     browser.implicitly_wait(3)
    
#     if cur_page_num == target_page_num:
#         print('크롤링 종료')
#         break # while True break


browser.close()










