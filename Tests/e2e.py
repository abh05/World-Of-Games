from selenium import webdriver
from sys import exit

def est_scores_service():
    driverCH = webdriver.Chrome(executable_path="chromedriver")
    driverCH.get("http://localhost:40000/score")
    driverCH.maximize_window()
    getnum = driverCH.find_element_by_xpath('/html/body/h3')
    a = getnum.text
    if 1 <= int(a) < 1000:
        return True
    else:
        return False


def main_function():
    test_result = est_scores_service()
    if test_result is True:
        print("test Passed")
        return exit(0)
    else:
        print("test Failed")
        return exit(1)


print(main_function())
