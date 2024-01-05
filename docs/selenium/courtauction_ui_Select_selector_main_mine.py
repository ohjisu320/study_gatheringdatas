import docs.selenium.courtauction_ui_Select_selector_subfunction_mine as subfunction

# 기본 function 형식 - :을 통해 불릴 때만 기능함
def main(): 
    try :
        uri = "https://www.courtauction.go.kr/"
        browser = subfunction.get_browser(uri)
        court_count, list_court_name_sec = subfunction.go_and_define_select(browser=browser)
        print("court count :".format(court_count))



        # courtauctions=subfunction.connect_mongo('courtauctions')
        # for x in range(3) : 
        # court_count, list_court_name_sec = subfunction.go_and_define_select(browser=browser,"#idJiwonNm", x)
        # pass
        # for y in range(1,10):
        # subfunction.finding_and_upload()
        # subfunction.paging(y)
        # subfunction.back_program()

        def quitBrowser(browser) :
            browser.quit()

           # 업무 코드
    except :
        pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
    finally :
        quitBrowser(browser)    # try나 except가 끝난 후 무조건 실행되는 코드    
    return 0

if __name__=="__main__":
    # 기본 구문
    try :
        main()    # 업무 코드
    except :
        pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
    finally :
        pass    # try나 except가 끝난D 후 무조건 실행되는 코드