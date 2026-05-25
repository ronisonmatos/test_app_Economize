from pages.opcoesMenu_page import OpcoesMenuPage
from pages.onboarding_page import OnboardingPage
from core.logger import logger

def test_completo(driver):

    logger.info("Iniciando Testes")

    logger.info("Iniciando teste onboarding")

    onboarding = OnboardingPage(driver)

    onboarding.aceitar_permissao()

    onboarding.clicar_pular_configuracao()

    onboarding.clicar_pular()

    onboarding.clicar_entendi()

    onboarding.clicar_entendi()

    logger.info("Teste onboarding finalizado")

    opcoesMenuPage = OpcoesMenuPage(driver)

    opcoesMenuPage.menu()

    logger.info("Abriu o Menu")