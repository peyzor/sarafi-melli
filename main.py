import datetime
import logging
import random
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger()
logger.setLevel(logging.INFO)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)

logger.addHandler(stdout_handler)


def main():
    url = 'https://nobat.mex.co.ir/'
    browser = webdriver.Chrome()

    browser.get(url)

    start_time = datetime.time(16, 0, 0)
    while True:
        time.sleep(0.1)

        if datetime.datetime.now().time() >= start_time:
            break

    wait = WebDriverWait(browser, 300)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div[2]/div/span/button')
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/span[1]/button')
    )).click()

    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-2 my-5"]')
    ))

    appointments = browser.find_elements(
        By.XPATH, '//div[@class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-2 my-5"]//button[not(@disabled)]'
    )

    if not appointments:
        raise Exception('no appointments found')

    appointment = random.choice(appointments)
    appointment.click()

    complete_button = browser.find_element(
        By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/span[2]/button'
    )
    complete_button.click()

    time.sleep(600)

    browser.quit()


if __name__ == '__main__':
    main()
