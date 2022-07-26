import selenium
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time
from config import config


def open_login(login_button, max_try=300):
    try:
        login_button.click()
    except ElementClickInterceptedException:
        print("Error")

        if max_try == 0:
            return

        max_try -= 1

        open_login(login_button, max_try)


def login(driver):
    nif_input = driver.find_elements(by=By.ID, value="nif")

    nif_input = nif_input[0]

    nif_input.send_keys(config.dni)

    password_input = driver.find_elements(by=By.ID, value="password")

    password_input = password_input[0]

    password_input.send_keys(config.password)

    checkbox = driver.find_elements(by=By.TAG_NAME, value="md-checkbox")

    checkbox = checkbox[0]

    checkbox.click()

    dialog = driver.find_element(by=By.XPATH, value="//div[@class = 'md-actions']/button")

    dialog.click()

    time.sleep(1)

    submit = driver.find_element(by=By.XPATH, value="//button[@ng-click = 'vm.submitLoginChave()']")

    submit.click()

    time.sleep(1)

    driver.get("https://esaude.sergas.gal/EPACI_epaciente/#/dynamic-view?idView=60f534f9c6fc339762662291")

    time.sleep(1)

    dispensation_plan = driver.find_element(by=By.XPATH, value="//div[@class = 'col-12 mb-4 ng-star-inserted']")

    dispensation_plan.click()

    time.sleep(1)

    # download_button = driver.find_element(by=By.ID, value="//button[@id = 'download']")
    #
    # download_button.click()

    driver.switch_to.window(driver.window_handles[1])

    print(driver.current_url)


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

    login(driver)

    #driver.close()


