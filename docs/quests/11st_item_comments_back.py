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
browser.get("https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb")


from selenium.webdriver.common.by import By

def click_item(i) : # click best item - preprocess
    # click item
    item_list = browser.find_elements(by=By.CSS_SELECTOR, value="div.box_pd.ranking_pd >a")
    item_list[i].click()
    time.sleep(1)
    return item_list

def click_review() :    # click reviews - preprocess
    # click review
    browser.find_element(by=By.CSS_SELECTOR, value="#tabMenuDetail2").click()
    # - switch
    browser.switch_to.frame("ifrmReview")
    time.sleep(1)

def item_finding() :    # finding item's info
    pass
    item_name = browser.find_element(by=By.CSS_SELECTOR, value="h1.title").text
    try : 
        item_reqular_price = browser.find_element(by=By.CSS_SELECTOR, value="div.price_info > dd > del").text
    except :
        item_reqular_price=""    
    try : 
        item_now_price =browser.find_element(by=By.CSS_SELECTOR, value="strong > span.value").text
    except :
        item_now_price =browser.find_element(by=By.CSS_SELECTOR, value=" #finalDscPrcArea > dd > strong > span.value").text
    item_image = browser.find_element(by=By.CSS_SELECTOR, value="div.img_full > img").get_attribute('src')
    item_contents = browser.find_element(by=By.CSS_SELECTOR, value="#tabpanelDetail1 > table > tbody").text
    col_11st_items.insert_one({"명칭":item_name, "원가" : item_reqular_price, "판매가":item_now_price, "image link" : item_image, "상품상세": item_contents})
  
def comments_listing() :    # finding reviews' info
    list_reviews=browser.find_elements(by=By.CSS_SELECTOR, value="div.cont_text_wrap")
    try : # 작성자 리스팅
        list_name = browser.find_elements(by=By.CSS_SELECTOR, value=" ul.area_list > li.review_list_element >dl.c_product_reviewer >dt.name")
    except :
        list_name=[]
        for x in range(len(list_reviews)):
            list_name.append("")
    list_option = [] # 옵션 리스팅
    for x in range(len(list_reviews)) :
        try : 
            option = browser.find_element(by=By.CSS_SELECTOR, value="ul.area_list > li.review_list_element > div > dl > div > dd")
            list_option.append(option.text)
        except :
            list_option.append("")
    try : # 별점 리스팅
        list_rate = browser.find_elements(by=By.CSS_SELECTOR, value="ul.area_list > li.review_list_element > div > p.grade > span > em")
    except :
        list_rate = []
        for x in range(len(list_reviews)):
            list_rate.append("")

    # 내용 리스팅(2) with for문 - click 후 div.cont_text_wrap 스크래핑
    list_contents = [] # list 생성
    for x in range(len(list_reviews)) : # 리뷰 수 만큼 반복
        try : 
            browser.find_element(by=By.CSS_SELECTOR, value="ul.area_list > li.review_list_element > div > div > div.cont_text_wrap > p.cont_btn > button").click() # 클릭
            elements_contents = browser.find_elements(by=By.CSS_SELECTOR, value="ul.area_list > li.review_list_element > div > div > div.cont_text_wrap") # elements 찾기
            list_contents.append(elements_contents[x].text) # text만 뽑아서 list에 append
        except :
            elements_contents = browser.find_elements(by=By.CSS_SELECTOR, value="ul.area_list > li.review_list_element > div > div > div.cont_text_wrap") # elements 찾기
            list_contents.append(elements_contents[x].text) # text만 뽑아서 list에 append
    col_11st_items.find({},{"_id":1})
    item_id = col_11st_items.find({},{"_id":1})[i]["_id"]
    for x in range(len(list_reviews)) : # 리뷰 수 만큼 반복해서 한 행씩 db에 upload
        col_11st_comments.insert_one({"item_id":item_id,"name":list_name[x].text, "option" : list_option[x], "rate" : list_rate[x].text, "comments":list_contents[x]})        
   
def connect_mongo(database_name, collection_name): # mongodb connect
    from pymongo import MongoClient
    mongoClient=MongoClient("mongodb://localhost:27017")
    database=mongoClient[database_name]
    collection=database[collection_name]
    return collection

def before() :  # dbconnect - preprocess
    col_11st_items = connect_mongo("gatheringdatas", "11st_item")
    col_11st_items.delete_many({})
    col_11st_comments = connect_mongo("gatheringdatas", "11st_item_comments") # db connect
    col_11st_comments.delete_many({})
    return col_11st_items,col_11st_comments

# 브라우저 종료

loop_sign = int(input("select items(num) : "))    # 몇 개의 item을 스크래핑 할 지 input 받기

col_11st_items,col_11st_comments = before() # dbconnect - preprocess

for i in range(loop_sign) :
    click_item(i)   # click best item - preprocess
    item_finding()  # finding item's info 
    click_review()  # click reviews - preprocess
    comments_listing()  # finding reviews' info
    browser.back()  # back
    time.sleep(1)   # stop for 1s 

browser.quit()