import logging
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from email_service import send_email

logger = logging.getLogger()
logger.setLevel(logging.INFO)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)

logger.addHandler(stdout_handler)


def check_reservation_availability():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        url = 'http://reserve.ex-sa.ir/'
        driver.get(url)

        while True:
            try:
                exchange = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="branchesList"]/div[1]/button'))
                )
                exchange.click()

                not_available_banner = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="branchTurnsList"]/div[5]/h5'))
                )
                if not_available_banner.text != 'نوبت خالی وجود ندارد':
                    logger.info(f'sending email')
                    send_email("Available Reserve", f"{url=}")
                    break

                driver.refresh()
                time.sleep(1)

            except Exception as e:
                # driver.refresh()
                # time.sleep(1)
                logger.info(f'err: {e}')
                break

    finally:
        driver.quit()


if __name__ == "__main__":
    check_reservation_availability()
