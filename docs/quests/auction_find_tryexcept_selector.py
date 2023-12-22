#  상품 제목, 원래가격, 현재가격, 배송방법(list방식) 크롤링하기
# 각각 사용했던 태그 공유
# git url / file: 사용한 각각 tag(element) ex) div title

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

capabilities = browser.capabilities

browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")

# - 가능 여부에 대한 OK 받음
pass

# 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div.info" # 전체
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for element_item in element_bundle :
    try : 
        element_title = element_item.find_element(by=By.CSS_SELECTOR, value="em > a") # 상품 제목
        title = element_title.text
    except :
        title = ""
        pass
    try : 
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value="ul > li.c_price > span > strike > span")
        old_price = element_old_price.text # 원래가격
        pass
    except :
        old_price = ""
        pass

    try : 
        element_new_price = element_item.find_element(by=By.CSS_SELECTOR, value="ul > li.d_price > span.sale > span")
        new_price = element_new_price.text # 현재가격
    except :
        new_price = ""
        pass
    try : 
        element_delivery = element_item.find_element(by=By.CSS_SELECTOR, value="div.icon > div")
        delivery = element_delivery.text.split() # 배송방법  
        pass
    except :
        delivery = ""
        pass

    print("title : {}, old price : {}, new price : {}, delivery : {}".format(title, old_price, new_price, delivery))
    pass