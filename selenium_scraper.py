# Target web page: https://www.olx.com.ec/
import constants as const
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def main():

    # Set up driver
    driver: WebDriver = setup_driver()

    # Request to the seed URL
    driver.get("https://www.olx.com.ec/")

    # Input search
    input_search(driver)

    # Click the button 4 times

    # Scrape results


def setup_driver():

    # Use this syntax of creating Service object to prevent deprecation warning.
    # Ref: https://github.com/SergeyPirogov/webdriver_manager/issues/281
    driver = webdriver.Chrome(service=Service(const.DRIVER_PATH))  # type:ignore
    driver.implicitly_wait(const.TIMEOUT)
    return driver


def input_search(driver: WebDriver):

    # Write search
    # search_input_box = driver.find_element_by_xpath(const.INPUT_XPATH)
    search_input_box = driver.find_element(By.XPATH, const.INPUT_XPATH)
    search_input_box.send_keys("guitarra")

    # Click button
    search_btn = driver.find_element(By.XPATH, const.SBTN_XPATH)
    search_btn.click()

    sleep(15)

    print("Done")


if __name__ == "__main__":
    main()
