import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


def get_text_content():
    # Get ChromeDriver path from environment variable
    chromedriver_path = os.getenv('CHROMEDRIVER_PATH', '/usr/bin/chromedriver')

    # Setup Chrome WebDriver
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open the URL
        driver.get("https://atcoder.jp/contests/abc392/tasks/abc392_a")

        # Wait for the page to load completely
        WebDriverWait(driver, 30).until(lambda d: d.execute_script(
            'return document.readyState') == 'complete')

        element = driver.find_element(By.ID, "pre-sample0")

        # Print the text content
        print(element.get_property("textContent"))

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    get_text_content()
