from pages.opcoesMenu_page import OpcoesMenuPage
from core.logger import logger

def test_opcoesMenu(driver):

    logger.info("Acessando Opções de Menu")

    opcoesMenuPage = OpcoesMenuPage(driver)

    opcoesMenuPage.menu()

    logger.info("Abriu o Menu")