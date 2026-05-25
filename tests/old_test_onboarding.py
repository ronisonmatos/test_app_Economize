from pages.onboarding_page import OnboardingPage

from core.logger import logger

def test_onboarding(driver):

    logger.info("Iniciando teste onboarding")

    onboarding = OnboardingPage(driver)

    onboarding.aceitar_permissao()

    onboarding.clicar_pular_configuracao()

    onboarding.clicar_pular()

    logger.info("Teste onboarding finalizado")