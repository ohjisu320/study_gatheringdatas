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
browser.get("https://www.11st.co.kr/products/pa/4940434685?inpu=&trTypeCd=22&trCtgrNo=895019")

# - 가능 여부에 대한 OK 받음
pass

# click review
from selenium.webdriver.common.by import By
click_revies = browser.find_element(by=By.CSS_SELECTOR, value="#tabMenuDetail2").click()

# - switch
browser.switch_to.frame("ifrmReview")

list_reviews = browser.find_elements(by=By.CSS_SELECTOR, value="dt.name")

time.sleep(3)

# click_reviewmore = browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button").click()
# time.sleep(3)
# - 정보 획득


try : 
    list_name = browser.find_elements(by=By.CSS_SELECTOR, value="dt.name")
except :
    list_name = []

try : 
    list_option = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element > div > dl > div > dd")
except :
    list_option = []
try : 
    list_rate = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element > div > p.grade > span > em")
except :
    list_rate = []
try : 
    click_more = browser.find_element(by=By.CSS_SELECTOR, value="li.review_list_element > div > div > div.cont_text_wrap > p.cont_btn.review-expand > button.c_product_btn.c_product_btn_more6.review-expand-open-text").click()
    list_contents = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element > div > div > div.cont_text_wrap > p")
except :
    list_contents = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element > div > div > div.cont_text_wrap > p")
pass

def connect_mongo(database_name, collection_name):
    from pymongo import MongoClient
    mongoClient=MongoClient("mongodb://localhost:27017")
    database=mongoClient[database_name]
    collection=database[collection_name]
    return collection
col_11st_comments = connect_mongo("gatheringdatas", "11st_comments")
for x in range(len(list_name)) :
    col_11st_comments.insert_one({"name":list_name[x].text, "option" : list_option[x].text, "rate" : list_rate[x].text, "comments":list_contents[x].text})
# 브라우저 종료
browser.quit()