import constants as const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def main():

    # Set up driver
    driver:WebDriver = setup_driver()

    # Request to the seed URL
    driver.get("https://www.olx.com.ec/")

    # Input search

    # Click the button 4 times

    # Scrape results


def setup_driver():

    # Use this syntax of creating Service object to prevent deprecation warning.
    # Ref: https://github.com/SergeyPirogov/webdriver_manager/issues/281
    driver = webdriver.Chrome(service=Service(const.DRIVER_PATH))  # type:ignore
    driver.implicitly_wait(const.TIMEOUT)
    return driver


# def input_search(driver:WebDriver):





if __name__ == "__main__":
    main()
    # print(setup_driver().__class__)
