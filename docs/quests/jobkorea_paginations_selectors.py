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
browser.get("https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1")


# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By
# 서울, 경기, 인천 선택
for local_num in range(1,4) :
    click_local = browser.find_element(by = By.CSS_SELECTOR, value="#devSearchForm > div.detailArea > div > div:nth-child(1) > dl.loc.circleType.dev-tab.dev-local.on > dd.ly_sub > div.ly_sub_cnt.colm2-ty2.clear > dl.detail_sec.barType > dd > div.nano-content.dev-main > ul > li:nth-child({}) > label".format(local_num))
    click_local.click()

click_button = browser.find_element(by=By.CSS_SELECTOR, value="#dev-btn-search")
click_button.click()

time.sleep(5)

# page_list= browser.find_element(by=By.CSS_SELECTOR, value="#MajorAGI > p:nth-child(3)").text.split()
# for page_num in range(len(page_list)) : 
#     page_list[page_num+1].click()
#     time.sleep(3)

for page_num in [] :
    next = browser.find_element(by=By.CSS_SELECTOR, value="#dvGIPaging > div > p:nth-child(3) > a")
    click_next=next.click()
    



for x in [] :
    url = "https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1#anchorGICnt_{}".format(x)
    browser.get(url)

pass

# 브라우저 종료
browser.quit()