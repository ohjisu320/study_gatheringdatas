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

# - 주소 입력
browser.get("https://getbootstrap.com/docs/5.3/examples/checkout/")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)


# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # refer official https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select
# Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)

# 국가 selector 선택
selector_element = "#country"
element_country = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
Select(element_country).select_by_index(1)

# 주 selector 선택
selector_element = "#state"
element_state = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
Select(element_state).select_by_index(1)
pass

# 브라우저 종료
browser.quit()