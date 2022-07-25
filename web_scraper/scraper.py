import selenium
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import ElementClickInterceptedException


def open_login(login_button, max_try=300):
    try:
        login_button.click()
    except ElementClickInterceptedException:
        print("Error")

        if max_try == 0:
            return

        max_try -= 1

        open_login(login_button, max_try)


def innit():

    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    # options = ChromeOptions()
    # driver = webdriver.Chrome(options=ChromeOptions())

    driver.get("https://esaude.sergas.gal/EPACI_epaciente/#/home")

    access_button = driver.find_elements(by=By.ID, value="epaci-header-access-button")

    while len(access_button) == 0:
        access_button = driver.find_elements(by=By.ID, value="epaci-header-access-button")

    access_button = access_button[0]

    open_login(access_button)

    #driver.close()


