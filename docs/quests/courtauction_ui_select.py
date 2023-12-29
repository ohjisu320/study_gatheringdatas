# 법원소재지에 따른 물건 내역 확인

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC




# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # refer official https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select
# Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)

def go_and_define_select() :
    browser.switch_to.frame('indexFrame')
    browser.find_element(by=By.CSS_SELECTOR, value="#menu > h1:nth-child(5)").click()
    # 셀렉트 지정
    selector_element = "#idJiwonNm"
    element_court = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
    list_court_name = browser.find_elements(by=By.CSS_SELECTOR, value="#idJiwonNm > option")
    list_court_name_sec =[]
    for x in range(len(list_court_name)) :
        list_court_name_sec.append(list_court_name[x].text)
    pass
    return element_court, list_court_name_sec


def selecting(x) :
    # 다시 셀렉트 클릭할 때, 오류발생
    Select(element_court).select_by_index(x)
    



def click_to_search():
    browser.find_element(by=By.CSS_SELECTOR, value="#contents > form > div.tbl_btn > a:nth-child(1)").click()

def finding_and_upload():
    list_numbers = []
    list_address = []
    table_rows = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form > table > tbody > tr")
    table_datas = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form:nth-child(1) > table > tbody > tr > td")
    for index in range(len(table_rows)) : # 20번 반복
        list_number_box = table_datas[(index*7)+1].text.split()[1:] # 어떻게 할지 결정하기
        number=""
        for e in range(len(list_number_box)) :
            if len(list_number_box) > 1 :
                number += list_number_box[e]+" "
            else :
                number += list_number_box[e]
        address = table_datas[(index*7)+3].text
        courtauctions.insert_one({"법원소재지": list_court_name_sec[x], "사건번호":number, "소재지및내역":address})
    return list_numbers, list_address

def paging(y):    
    time.sleep(1)
    # 다음 페이지 번호에 해당하는 <a> 태그를 찾습니다
    next_page = browser.find_element(By.XPATH, '//a/span[text()=" {} "]'.format(y + 1))
    next_page.click()
    time.sleep(1)
    return 

def back_program() :
    # 이전 버튼 : #contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5)
    browser.find_element(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5)").click()

def connect_mongo(col_name) : 
    # mongodb compass 띄우기
    from pymongo import MongoClient     # pymongo : module, Mongoclient : class      # client : mongoDB의 compass 같은 역할
    # mongodb에 접속(connection) -> 자원에 대한 class
    mongoClient = MongoClient("mongodb://localhost:27017")   # mongoClient : class를 담은 변수  # 내 주소
    # database 연결
    database = mongoClient["gatheringdatas"]
    # collection 작업
    collection = database[col_name]
    collection.delete_many({})
    return collection

if __name__ == "__main__" :
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

    element_court, list_court_name_sec = go_and_define_select()
    courtauctions=connect_mongo('courtauctions')
    for x in range(3) : 
        selecting(x)
        click_to_search()
        pass
        for y in range(1,10):
            finding_and_upload()
            paging(y)
        back_program()

    # 브라우저 종료
    browser.quit()