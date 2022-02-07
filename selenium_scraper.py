# Target web page: https://www.olx.com.ec/
import json
import random
import logging
import logging.config 
import constants as const
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


# Logs configuration
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/selenium_scraper.log", mode="w")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)



def main():

    # Set up driver
    driver: WebDriver = setup_driver()

    # Request to the seed URL
    driver.get("https://www.olx.com.ec/")

    # Input search
    input_search(driver)

    # Click the button 4 times
    press_button(driver)

    # Scrape results
    scrape_results(driver)

    print("\nYour scraping was successful!\n\nCheck the results folder!\n")




def setup_driver():

    # Use this syntax of creating Service object to prevent deprecation warning.
    # Ref: https://github.com/SergeyPirogov/webdriver_manager/issues/281
    driver = webdriver.Chrome(service=Service(const.DRIVER_PATH))  # type:ignore
    driver.implicitly_wait(const.TIMEOUT)

    logger.info("Driver configured successfully.")
    return driver


def input_search(driver: WebDriver):

    # Write search
    search_input_box = driver.find_element(By.XPATH, const.INPUT_XPATH)
    search_input_box.send_keys("guitarra") # Writes input

    # Click button
    search_btn = driver.find_element(By.XPATH, const.SBTN_XPATH)
    search_btn.click()

    logger.info("Search for guitarra successfull.")




def press_button(driver: WebDriver):

    sleep(random.uniform(4.0, 6.0)) # Button sometimes takes time to load

    for i in range(4):

        load_content_button = driver.find_element(By.XPATH, const.LOAD_CONTENT_BUTTON_XPATH)
        load_content_button.click()
        sleep(random.uniform(8.0, 12.0)) # Makes it more human-like

        logger.info(f"Loaded more content by pressing the button successfully ({i+1}).")



def scrape_results(driver: WebDriver):

    products = driver.find_elements(By.XPATH, const.ITEMS_XPATH)


    results = {}

    # Now we search with XPATH with product WebItem as our root (not the whole driver)
    for i, product in enumerate(products):

        # A few items don't have this elements
        try:
            # The .text is to take the text string out of the WebElement
            price = product.find_element(By.XPATH, './/span[@data-aut-id="itemPrice"]').text.replace(" ", "") # Now we use .// in out XPATH
            description = product.find_element(By.XPATH, './/span[@data-aut-id="itemTitle"]').text # Now we use .// in out XPATH

            # Load fields in final data structure
            results[i] = {"price": price, "description": description}
        except:
            logger.debug(f"Couldn't find elements for product {i}, moving to the next one.")
            continue # Pass on to the next


    # Store results in a json file
    with open('results/scraped_results.json', 'w') as fp:
        json.dump(results, fp, indent=4)
        logger.info("Stored results successfully.")
        pass





if __name__ == "__main__":
    main()

