# 법원소재지에 따른 물건 내역 확인

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
browser.get("https://www.courtauction.go.kr/")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)


# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # refer official https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select
# Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)
time.sleep(2)
browser.switch_to.frame('indexFrame')
browser.find_element(by=By.CSS_SELECTOR, value="#menu > h1:nth-child(5)").click()

# 셀렉트 지정
selector_element = "#idJiwonNm"
element_court = browser.find_elements(by=By.CSS_SELECTOR, value="#idJiwonNm")
list_elements_court = element_court[0].text.split()
for x in range(len(list_elements_court)) : # 61개 반복 (법원 개수)
    time.sleep(2)
    element_court = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
    Select(element_court).select_by_index(x)
    browser.find_element(by=By.CSS_SELECTOR, value="#contents > form > div.tbl_btn > a:nth-child(1)").click()
    list_pages_num = browser.find_element(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form > div > div.page2 > a").text.split() #10
    list_info = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form > table > tbody > tr ") # 20개
    list_info_details = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form > table > tbody > tr > td") 
    list_unique_num =[]
    list_local = []
    # 법원 소재지, 사건번호/소재지 및 내역 으로 컬렉션 나누기
    for z in range(len(list_pages_num)) : # 10번 반복
        list_pages = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form > div > div.page2 > a") #10
        list_pages[z+1].click()
        # tr을 list화 > 2번째 td
        for y in range(len(list_info)) : # 20번 반복
            # list_info_details = list_info[y].find_elements(by=By.CSS_SELECTOR, value="tr > td")  # td를 리스트화 
            list_info_details = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form > table > tbody > tr > td")
            list_unique_num.append(list_info_details[6*y+1].text)
            locals =list_info_details[6*y+3]
            list_local.append(locals.text) 
            # db에 업로드 자리
            print(list_unique_num, list_local)
            pass



# 검색 클릭 후 정보 저장



# 브라우저 종료
browser.quit()