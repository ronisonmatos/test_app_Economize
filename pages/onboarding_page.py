from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.appiumby import AppiumBy

from core.logger import logger

import time

class OnboardingPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def aceitar_permissao(self):

        try:

            allow = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.ID,
                        "com.android.permissioncontroller:id/permission_allow_button"
                    )
                )
            )

            allow.click()

            logger.info("Permissão aceita")

        except:

            logger.info("Permissão não apareceu")

        time.sleep(2)

    def clicar_pular_configuracao(self):

        pular_config = self.wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    "Pular configuração"
                )
            )
        )

        pular_config.click()

        logger.info("Pular configuração clicado")

        time.sleep(2)

    def clicar_pular(self):

        pular = self.wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    "Pular"
                )
            )
        )

        pular.click()

        logger.info("Pular clicado")

        time.sleep(2)


    def clicar_entendi(self):

        entendi = self.wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    "Entendi"
                )
            )
        )

        entendi.click()

        logger.info("Clicou em Entendi")

        time.sleep(2)