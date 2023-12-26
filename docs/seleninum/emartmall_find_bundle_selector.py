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
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)

pass


# - 정보 획득
pass
from selenium.webdriver.common.by import By
selector_value = "div.mnemitem_unit"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for element_item in element_bundle:
    # print(element_item.text)        # 상품 정보들
    # 상품 제목
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value="span.mnemitem_goods_tit")
    title = element_title.text
    # 상품 판매 원가 (try~except 포함)
    try :
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value="div > del > em")
        old_price = element_old_price.text
        pass
    except :
        old_price = ""
        pass
    finally :
        pass
    print("title : {}, old price : {}".format(title, old_price))
    pass
pass
# 브라우저 종료
browser.quit()