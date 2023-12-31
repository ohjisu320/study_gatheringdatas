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
browser.get("https://play.google.com/store/apps/details?id=com.nhlife.customer.healthcare&hl=ko-KR&pli=1")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# 댓글 모달화면 띄우기 및 클릭 : 평가 및 리뷰 클릭
selector_element = "#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > header > div > div:nth-child(2) > button"
browser.find_element(by=By.CSS_SELECTOR,value=selector_element).click()
# - 정보 획득
# 댓글 모달확인 : (css overflow:scroll or auto) div.fysCi
selector_element = "div.fysCi"
element_scrollableDiv = browser.find_element(by=By.CSS_SELECTOR,value=selector_element)
# 스크롤 전 댓글 개수 확인 : div.RHo1pe
selector_element = "div.RHo1pe"
elements_comment = browser.find_elements(by=By.CSS_SELECTOR,value=selector_element)
print("count comment before done scroll : {}".format(len(elements_comment)))
# 댓글 마지막까지 스크롤 : scrollHeight 확인
# - scrollableDiv.scrollHeight
# - scrollableDiv.scrollTo(0, scrollableDiv.scrollHeight);
previous_scrollHeight = 0
while True:
    # python 방식 변수 매칭
    # print("{0}.scrollTo({1}, {0}.scrollHeight);".format(element_scrollableDiv,previous_scrollHeight))
    # javascript와 python 결합 방식 변수 매칭
    browser.execute_script("arguments[0].scrollTo(arguments[1], arguments[0].scrollHeight);",element_scrollableDiv,previous_scrollHeight)
    current_scrollHeight = browser.execute_script("return arguments[0].scrollHeight",element_scrollableDiv)
    if previous_scrollHeight >= current_scrollHeight:
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass
time.sleep(1)
# 스크롤 후 댓글 개수 확인 : div.RHo1pe
selector_element = "div.RHo1pe"
elements_comment = browser.find_elements(by=By.CSS_SELECTOR,value=selector_element)
print("count comment after done scroll : {}".format(len(elements_comment)))
time.sleep(1)
# 브라우저 종료
browser.quit()