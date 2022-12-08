from selenium import webdriver
# is able to press keys
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def main():
 # driver is a reference to the website
    driver = get_driver()
    # type: ignore
    # finding element by ID is more robust compared to by xpath
    # putting it in a variable is not needed.
    # *typing values in an input
    driver.find_element(
        by="id", value="id_username").send_keys("automated")
    # *typing and pressing a key
    driver.find_element(
        by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    print(driver.current_url)
    # * clicking a link
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
    name = f"{datetime.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    f = open(name, "w")  # type: ignore
    while True:
        time.sleep(4)
        element = driver.find_element(
            by="xpath", value="/html/body/div[1]/div/h1[2]")
        text = element.text.split(": ")[1]
        f.write(text + " ")


print(main())
