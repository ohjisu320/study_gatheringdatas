# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

webdriver_manager_directory = ChromeDriverManager().install()

# browser(Chrome) 열기
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://cafe.naver.com/peopledisc")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
# 병원진료후기 메뉴 클릭  : #menuLink84
# browser.find_element(by=By.CSS_SELECTOR, value="#menuLink84").click() --앞의 것이 완료된 경우
element_click = browser.find_element(by=By.CSS_SELECTOR, value="#menuLink84")
element_click.click()

# iframe으로 전환
browser.switch_to.frame("cafe_main")

# 해당 리스트 : #main-area > div:nth-child(4) > table > tbody > tr
cafe_list = browser.find_elements(by=By.CSS_SELECTOR, value="#main-area > div:nth-child(4) > table > tbody > tr")
pass

# 브라우저 종료
browser.quit()