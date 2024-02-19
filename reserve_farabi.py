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
        url = 'https://r.irfarabi.com/exchange/'
        driver.get(url)

        while True:
            try:
                not_available_banner = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="divTimeSelector"]/h6'))
                )
                if not_available_banner.text != 'برای تاریخ انتخابی نوبتی یافت نشد.':
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
