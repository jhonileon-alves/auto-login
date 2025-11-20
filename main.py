from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def login_banco(usuario, senha):
    try:
        options = Options()
        options.add_experimental_option('detach', True)
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        driver.get('http://exemplo.com/login')

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, 'user')))
        wait.until(EC.presence_of_element_located((By.NAME, 'password')))

        driver.find_element(By.NAME, 'user').send_keys(usuario)
        driver.find_element(By.NAME, 'password').send_keys(senha + Keys.ENTER)
        return driver
    except Exception as e:
        print(f"[ERRO] Falha ao tentar realizar login: {e}")

usuario = os.environ.get("TEST_USER", "usuario_teste")
senha = os.environ.get("TEST_PASS", "senha_teste")

driver = login_banco(usuario, senha)
