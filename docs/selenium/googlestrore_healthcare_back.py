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
browser.get("https://play.google.com/store/search?q=%ED%97%AC%EC%8A%A4%EC%BC%80%EC%96%B4%EC%95%B1&c=apps&hl=ko-KR&pli=1")


# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By
# 앱 제조 회사 리스트 : div > a.Si6A0c.Gy4nib
elements_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a.Si6A0c.Gy4nib")
for company in elements_companies :
    company.click()
    time.sleep(1)   # 화면 완성 term
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="div > h1")
    print("app company name : {}".format(element_title.text))
    browser.back()  # 제품 리스트로 이동
    time.sleep(1)   # 화면 완성 term
    pass

pass

# 브라우저 종료
browser.quit()