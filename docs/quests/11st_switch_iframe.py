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


from selenium.webdriver.common.by import By
def before() : # 전처리과정
    # click review
    click_revies = browser.find_element(by=By.CSS_SELECTOR, value="#tabMenuDetail2").click()
    # - switch
    browser.switch_to.frame("ifrmReview")
    time.sleep(3)
before()

time.sleep(3)

# click_reviewmore = browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button").click()
# time.sleep(3)
# - 정보 획득
def listing() :
    list_reviews=browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element")

    try : # 작성자 리스팅
        list_name = browser.find_elements(by=By.CSS_SELECTOR, value=" ul.area_list > li.review_list_element >dl.c_product_reviewer >dt.name")
    except :
        list_name=[]
        for x in range(len(list_reviews)):
            list_name.append("")
    try : # 옵션 리스팅
        list_option = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element > div > dl > div > dd")
    except :
        list_option = []
        for x in range(len(list_reviews)):
            list_option.append("")
    try : # 별점 리스팅
        list_rate = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element > div > p.grade > span > em")
    except :
        list_rate = []
        for x in range(len(list_reviews)):
            list_rate.append("")

    # 내용 리스팅(1) without for문 - p.cont_review_hide.text-expanded 스크래핑
    try : 
        list_contents = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element > div > div > div.cont_text_wrap > p.cont_review_hide.text-expanded")
    except :
        list_contents = []
        for x in range(len(list_reviews)):
            list_contents.append("")

    # 내용 리스팅(2) with for문 - click 후 div.cont_text_wrap 스크래핑
    list_contents_sec = []
    for x in range(len(list_name)) :
        try :
            browser.find_element(by=By.CSS_SELECTOR, value="li.review_list_element > div > div > div.cont_text_wrap > p.cont_btn > button").click()
            elements_contents = browser.find_elements(by=By.CSS_SELECTOR, value="div.cont_text_wrap")
            list_contents_sec.append(elements_contents[x].text)
        except :
            elements_contents_sec = browser.find_elements(by=By.CSS_SELECTOR, value="div.cont_text_wrap")
            list_contents_sec.append(elements_contents_sec[x].text)
            
    return list_name,list_option,list_rate,list_contents,list_contents_sec
list_name,list_option,list_rate,list_contents,list_contents_sec = listing()

def connect_mongo(database_name, collection_name):
    from pymongo import MongoClient
    mongoClient=MongoClient("mongodb://localhost:27017")
    database=mongoClient[database_name]
    collection=database[collection_name]
    collection.delete_many({})
    return collection

def db_upload() :
    # db업로드 - 내용 리스팅(1)
    col_11st_comments = connect_mongo("gatheringdatas", "11st_comments_first")
    for x in range(len(list_name)) :
        col_11st_comments.insert_one({"name":list_name[x].text, "option" : list_option[x].text, "rate" : list_rate[x].text, "comments":list_contents[x].text})
    # db업로드 - 내용 리스팅(2)
    col_11st_comments = connect_mongo("gatheringdatas", "11st_comments_second")
    for x in range(len(list_name)) :
        col_11st_comments.insert_one({"name":list_name[x].text, "option" : list_option[x].text, "rate" : list_rate[x].text, "comments":list_contents_sec[x]})
db_upload()
# 브라우저 종료
browser.quit()