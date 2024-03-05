# 웹 크롤링 (Crawling) : 브라우저 드라이버를 이용하여 실제로 각 페이지를 이동하며 '동적'으로 데이터를 수집하는 방법  // 여러 페이지를 이동하며 작동

# 웹 스크래핑 (Scrapping) : 웹 페이지의 응답을 받아 데이터를 분석하여 필요한 데이터를 수집하는 방법  // 하나의 페이지에서만 작동

# 파이썬 스크래핑 패키지 : beautifulsoup4

# 파이썬 크롤링 패키지 : selenium

# pip install beautifulsoup4
# pip install selenium
# pip install beautifulsoup4 selenium

import requests
from bs4 import BeautifulSoup 

URL = 'https://naver.com/'

response = requests.get(URL)
# print(response.text)
# response 의 값에 대한 설명
# 100: 추가적 요청 기다림
# 200: 성공
# 300: 리소스 위치 바뀌었다
# 400: 요청자(클라이언트) (뭔가 잘못 입력했다) 오류
# 500: 서버(응답자) 오류
# https://developer.mozilla.org/ko/docs/Web/HTTP/Status 자세한 설명 주소 참조

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else:
    print(soup)