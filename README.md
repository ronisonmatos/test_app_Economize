# QA Mobile - Economize App

Projeto de automação mobile utilizando:

- Appium
- Python
- Pytest
- Selenium
- Android Emulator
- Relatórios HTML/XML
- Logs

---

# Estrutura do Projeto

```bash
qa_mobile_economize/
│
├── tests/
│   └── test_onboarding.py
│
├── pages/
│   └── onboarding_page.py
│
├── core/
│   ├── config.py
│   ├── driver_factory.py
│   └── logger.py
│
├── reports/
│
├── logs/
│
├── screenshots/
│
├── conftest.py
│
├── pytest.ini
│
├── requirements.txt
│
└── README.md


Requisitos

Instalar:

Python 3.10+
Node.js
Java JDK
Android Studio
Appium
1. Instalar Python

Download:

https://www.python.org/downloads/

Durante instalação marcar:

Add Python to PATH

Verificar:

python --version
2. Instalar Node.js

Download:

https://nodejs.org/

Verificar:

node -v
npm -v
3. Instalar Appium
npm install -g appium

Verificar:

appium -v
4. Instalar Java JDK

Download:

https://adoptium.net/

Verificar:

java -version
5. Instalar Android Studio

Download:

https://developer.android.com/studio

Instalar:

Android SDK
Platform Tools
Emulator
6. Configurar Variáveis de Ambiente
ANDROID_HOME

Exemplo:

C:\Users\SEU_USUARIO\AppData\Local\Android\Sdk

Adicionar no PATH:

platform-tools
emulator
cmdline-tools\latest\bin
7. Verificar ADB
adb devices
8. Criar e iniciar Emulador

Android Studio:

Device Manager
→ Create Device
→ Pixel 4
→ Android 11

Iniciar emulador.

9. Instalar Dependências Python

Na raiz do projeto:

pip install -r requirements.txt
10. Iniciar Appium

Novo terminal:

appium

Deixar rodando.

11. Executar Testes
python -m pytest
12. Executar com Relatório HTML
python -m pytest --html=reports/report.html

Relatório será criado em:

reports/report.html
13. Executar com Relatório XML
python -m pytest --junitxml=reports/result.xml

Arquivo XML:

reports/result.xml
Logs

Os logs ficam em:

logs/test_execution.log
Estrutura da Automação
tests/

Contém os cenários de teste.

pages/

Contém os Page Objects.

Responsável por:

elementos
ações
navegação
core/

Infraestrutura do projeto:

driver
configuração
logs
Tecnologias Utilizadas
Python
Appium
Selenium
Pytest
Android Emulator
Melhorias Futuras
Screenshots automáticas
CI/CD
Allure Report
Execução paralela
BrowserStack
Device Farm