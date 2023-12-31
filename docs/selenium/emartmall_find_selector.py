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
html = browser.page_source
print(html)
pass
# - 정보 획득
from selenium.webdriver.common.by import By
# selector_value = browser.find_element(by=By.CSS_SELECTOR, value="#ty_thmb_view > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit")
# browser.find_element(By.CSS_SELECTOR,"#swiper-wrapper-08c189565af93cfd > li.mnemitem_grid_item.swiper-slide.swiper-slide-next > div > a > div.mnemitem_tit > span.mnemitem_goods_tit")

# 하나의 element 가져오기
selector_value = "#ty_thmb_view > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit"
element_path = browser.find_element(by=By.CSS_SELECTOR, value=selector_value) # Class를 리턴한 것.
# browser.find_element(by=By.CSS_SELECTOR, value=selector_value)
# get text in tag
element_path.text
pass
type(element_path)
# <class 'selenium.webdriver.remote.webelement.WebElement'>
element_path.text
# '반려견패드(중)40*50cm*100매'
element_path.get_attribute('class')
# 'mnemitem_goods_tit'

## 여러 개의 elements 정보 가져오기
selector_value = "span.mnemitem_goods_tit"
elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value) # Class를 리턴한 것.
pass
elements_path
# [<selenium.webdriver....ent_102")>]
type(elements_path)
# <class 'list'>
type(elements_path[0])
# <class 'selenium.webdriver.remote.webelement.WebElement'>
elements_path[0].text
# '반려견패드(중)40*50cm*100매'
# looping
for webelement in elements_path :
    title = webelement.text
    print("{}".format(title))

# 브라우저 종료
browser.quit()