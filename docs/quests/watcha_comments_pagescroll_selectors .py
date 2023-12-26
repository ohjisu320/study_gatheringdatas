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

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/b9bzA3V/comments")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
# html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 한 페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")

previous_scrollHeight = 0
list_name =[]
list_contents = []
list_grade = []

while True : 
    element_body.send_keys(Keys.END)
    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
    if previous_scrollHeight >= current_scrollHeight :
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    list_count_comments = browser.find_elements(by=By.CSS_SELECTOR, value="ul > div.css-13j4ly.egj9y8a4")
for count_comments in range(len(list_count_comments)) : # comment 개수 만큼 for문 돌리기
    try : # 작성자 이름
        find_name = browser.find_element(by=By.CSS_SELECTOR, value=" div:nth-child({}) > div.css-jqudug.egj9y8a3 > div.css-drz8qh.egj9y8a2 > a > div.css-eldyae.e10cf2lr1".format(count_comments+1)).text
        list_name.append(find_name)
    except :
        list_name.append("")
    try : # 내용
        find_contents = browser.find_element(by=By.CSS_SELECTOR, value=" div:nth-child({}) > div.css-2occzs.egj9y8a1 > a > div > span".format(count_comments+1)).text
        list_contents.append(find_contents)
    except :
        list_contents.append("")
    try : # 별점
        find_grade = browser.find_element(by=By.CSS_SELECTOR, value=" div:nth-child({}) > div.css-jqudug.egj9y8a3 > div.css-31ods0.egj9y8a0 > span".format(count_comments+1)).text
        list_grade.append(find_grade)
    except :
        list_grade.append("")
    
pass

def connect_mongo(collection_name):
    from pymongo import MongoClient
    mongoClient=MongoClient("mongodb://localhost:27017")
    database=mongoClient["gatheringdatas"]
    collection=database[collection_name]
    return collection

col_watcha = connect_mongo("watcha_comments")
for x in range(len(list_count_comments)) :
    col_watcha.insert_one({"name":list_name[x], "grade" : list_grade[x], "contents":list_contents[x]})
    pass




# 브라우저 종료
browser.quit()