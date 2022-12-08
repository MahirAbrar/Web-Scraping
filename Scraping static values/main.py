# code runner is required
# install .venv
# at the bottom next to python, change python version to .venv
# pip install selenium

# allows us to access static items from webpages
from selenium import webdriver


def get_driver():
 # * code required
    options = webdriver.ChromeOptions()
    # wont display that memory is low and stuff
    options.add_argument("disable-infobars")
    # start with maximised version of the browser
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    # our program is going to have greater privedges as some browsers have protections
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    # configure to use chrome
    driver = webdriver.Chrome(options=options)
    # the link
    driver.get("http://automated.pythonanywhere.com")
    return driver


def main():
 # siteRef is a reference to the website
    siteRef = get_driver()
    # type: ignore
    element = siteRef.find_element(
        by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text


print(main())
