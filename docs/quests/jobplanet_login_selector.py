# longin 후에 검색(검색어-데이터분석) 진행

 # * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

# browser(Chrome) 열기
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")

# - 가능 여부에 대한 OK 받음
pass

# 정보 획득
pass
from selenium.webdriver.common.by import By
try :
    email = browser.find_element(by=By.CSS_SELECTOR, value="#user_email")
    email.send_keys("dhwltn320@naver.com")
    pass
except :
    email = browser.find_element(by=By.CSS_SELECTOR, value="#user_email")
    email.send_keys("dhwltn320@naver.com")
    pass
try :
    password = browser.find_element(by=By.CSS_SELECTOR, value="#user_password")
    password.send_keys("********")
    pass
except :
    password = browser.find_element(by=By.CSS_SELECTOR, value="#user_password")
    password.send_keys("")
    pass
try :
    button = browser.find_element(by=By.CSS_SELECTOR, value="fieldset > button")
    button.click()
    pass
except :
    pass
pass
# 브라우저 종료
browser.quit()
