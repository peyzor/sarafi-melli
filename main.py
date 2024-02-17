import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def main():
    url = 'https://nobat.mex.co.ir/'
    browser = webdriver.Chrome()
    browser.get(url)

    wait = WebDriverWait(browser, 10)

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

    if appointments:
        appointment = random.choice(appointments)
        appointment.click()


if __name__ == '__main__':
    main()
