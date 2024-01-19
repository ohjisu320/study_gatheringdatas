# longin 후에 검색(검색어-데이터분석) 진행

 # * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

webdriver_manager_directory = ChromeDriverManager().install()

# browser(Chrome) 열기
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("http://192.168.10.235:8000/")

# - 가능 여부에 대한 OK 받음
pass

# 정보 획득
pass
from selenium.webdriver.common.by import By
time.sleep(2)
go_contactus = browser.find_element(by=By.CSS_SELECTOR, value="body > main > div > div > form:nth-child(2) > button").click()
time.sleep(2)
browser.back()
time.sleep(2)
go_clicktech = browser.find_element(by=By.CSS_SELECTOR, value="body > main > div > div > form:nth-child(1) > button").click()
time.sleep(2)
go_allad = browser.find_element(by=By.CSS_SELECTOR, value="body > div > ul > li:nth-child(1) > a").click()
time.sleep(2)
go_allad_by_chip = browser.find_element(by=By.CSS_SELECTOR, value="body > main > div.d-flex.gap-2.justify-content-start.py-5 > a:nth-child(2)").click()
time.sleep(2)
go_detailad = browser.find_element(by=By.CSS_SELECTOR, value="body > main > div.container > div > div:nth-child(1) > a").click()
time.sleep(2)
browser.back()
go_coupon = browser.find_element(by=By.CSS_SELECTOR, value="body > div > ul > li:nth-child(2) > a").click()
# 상세클릭 추가
time.sleep(2)
go_notice = browser.find_element(by=By.CSS_SELECTOR, value="body > div > ul > li:nth-child(3) > a").click()
# 상세클릭 추가
browser.back()
time.sleep(2)
go_faq = browser.find_element(by=By.CSS_SELECTOR, value="body > div > ul > li:nth-child(4) > a").click()

# 상세클릭 추가
browser.back()
time.sleep(2)
browser.get("http://192.168.10.235:8000/manager")
pass
# 브라우저 종료
browser.quit()
