from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.appiumby import AppiumBy

from core.logger import logger

import time

class OpcoesMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)


    def menu(self):

        try: 

            menu = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        '//*[contains(@content-desc, "Menu")]'
                    )
                )
            )

            menu.click()

            logger.info("Apertou o botão Menu")

        except:
            logger.info("Não clicou no Menu")

        time.sleep(2)