from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sys import exit

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')


def test_scores_service(driverCH):
    driverCH.get("http://localhost:8777/score")
    driverCH.maximize_window()
    getnum = driverCH.find_element_by_xpath('/html/body/h3')
    a = getnum.text
    if 1 <= int(a) < 1000:
        return True
    else:
        return False


def main_function():
    driverCH = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
    test_result = test_scores_service(driverCH)
    if test_result is True:
        print("test Passed")
        return exit(0)
    else:
        print("test Failed")
        return exit(1)


print(main_function())
