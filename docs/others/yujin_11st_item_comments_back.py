# * quests
# - 11번 상품 상세정보와 댓글 크롤링
# - 상품은 최소 4개
# - db명 : gatheringdatas / collectioin명 : 상품 : 11st_item, 댓글 : 11st_comments
# - 상품 : 명칭, image(썸네일) link, 원가, 판매가, 상품정보

## * 웹 크롤링 동작      # 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver 생성
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 가능 여부에 대한 OK 받음
pass

# - 주소 입력
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb#pageNum%%6"
browser.get(url)

# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

def connect_mongo() : 
    # mongodb compass 띄우기
    from pymongo import MongoClient     # pymongo : module, Mongoclient : class      # client : mongoDB의 compass 같은 역할
    # mongodb에 접속(connection) -> 자원에 대한 class
    mongoClient = MongoClient("mongodb://192.168.10.184:27017/")   # mongoClient : class를 담은 변수  # 내 주소
    # database 연결
    database = mongoClient["yjgatheringdatas"]
    # collection 작업
    collection = database['11st_item']
    collection = database['11st_comments']
    return collection


# iframe으로 전환
# #footer > div.c_banner_bottom_wrap > iframe
# browser.switch_to.frame('iframe')


# 명칭, image(썸네일) link, 원가, 판매가, 상품정보
for index in range(4) :
    # 베스트 500에서의 (1번)썸네일 : #thisClick_3886981496 > div > a > div.img_plot
    element_bests = browser.find_elements(by=By.CSS_SELECTOR, value="div > a > div.img_plot")  # find_elements = list
    element_bests[index].click()
    time.sleep(2)   # 화면 완성 term
    # 상품명 : #layBodyWrap > div > div.s_product.s_product_detail > div.l_product_cont_wrap > div > div.l_product_view_wrap > div.l_product_summary > div.l_product_side_info > div.c_product_info_title.c_product_info_title_coupon > h1 
    element_item_name = browser.find_element(by=By.CSS_SELECTOR, value='h1.title').text
    # 대표 상품 썸네일 : #productImg > div > img
    element_item_thumnail = browser.find_element(by=By.CSS_SELECTOR, value='#productImg > div > img').get_attribute('src')  # src attribute 명령어 불러오기
    # 원가(old_price) : div.b_product_info_price.b_product_info_price_style2 > div > div > dl > div:nth-child(1) > dd
    try : 
        list_element_old_price = browser.find_element(by=By.CSS_SELECTOR, value='div > dl > div:nth-child(1) > dd').text.split()
        element_old_price = ""
        for x in range(len(list_element_old_price)) :
            element_old_price += list_element_old_price[x]
    except : 
        element_old_price = browser.find_element(by=By.CSS_SELECTOR, value='div > dl > div:nth-child(1) > dd').text
    # 판매가(price) : #finalDscPrcArea > dd.price
    element_price = browser.find_element(by=By.CSS_SELECTOR, value='#finalDscPrcArea > dd.price').text
    # 상품정보(infor) : #tabpanelDetail1 > table > tbody
    element_item_infor = browser.find_element(by=By.CSS_SELECTOR, value='#tabpanelDetail1 > table > tbody').text
    print("상품명 : {}, img : {}, old price : {}, price : {}, item_info : {}".format(element_item_name, element_item_thumnail, element_old_price, element_price, element_item_infor))
    browser.back()  # 제품 리스트로 이동(현재 브라우저 창에서 뒤로가기)
    time.sleep(1)   # 화면 완성 term
    pass
pass    




# while True :
#     try :
#         # browser.find_element(by=By.CSS_SELECTOR, value="menuLink84").click()   # 아래 2줄과 동일한 내용
#         element_click = browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button")  # 메뉴 더보기 버튼
#         click_button = element_click.click()
#         time.sleep(5)
#     except :
#         break



# ## 여러개(복수) elements 정보 가져오기  <-- 어떤 find를 했을 때 정보가 여러 개 라는 의미
# selector_value = "li.review_list_element"
# element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)   # value : 전체



# for count_comments in element_bundle : # comments 개수 만금 for문 돌리기
#     try :  # writer(작성자)
#         element_writer = count_comments.find_element(by=By.CSS_SELECTOR, value="dt.name")    # value : element 접근자
#         writer = element_writer.text
#         pass
#     except :
#         writer = ""
#         pass
#     finally :
#         pass

#     try :  # option(선택옵션)
#         element_option = count_comments.find_element(by=By.CSS_SELECTOR, value="div > dl > div")
#         option = element_option.text
#         pass    
#     except :
#         rate = ""
#         pass
#     finally :
#         pass

#     try :  # rate(별점)
#         element_rate = count_comments.find_element(by=By.CSS_SELECTOR, value="div > p.grade > span")
#         rate = element_rate.text
#         pass    
#     except :
#         rate = ""
#         pass
#     finally :
#         pass

#     try :  # contents(내용)
#         element_contents = count_comments.find_element(by=By.CSS_SELECTOR, value="div > div > div.cont_text_wrap > p")
#         contents = element_contents.text
#         pass    
#     except :
#         contents = ""
#         pass
#     finally :
#         pass

#     col_11st = connect_mongo()
#     col_11st.insert_one({"writer":writer, "option":option, "rate":rate, "contents":contents})
#     pass



# 브라우저 종료
browser.quit()