from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class LoginPage:
    URL="https://the-internet.herokuapp.com/login"
    
    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        

    def open(self):
        self.driver.get(self.URL)
        logger.info("Page ouverte...")
        assert "login" in self.driver.current_url, "URL incorrecte"



    def seconnecter(self,user="tomsmith",pwrd="SuperSecretPassword!" ):
        logger.info("Remplissage du formulaire de login")

        # Username
        self.driver.find_element(By.ID, "username").send_keys(user)
        logger.info("       Username saisi")

        # Password
        self.driver.find_element(By.ID, "password").send_keys(pwrd)
        logger.info("       Password saisi")

        # Login
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        logger.info("    Login effectué")

        # Vérification        
    def verifier_connexion(self):
        flash = self.driver.find_element(By.ID, "flash").text
        assert "secure area" in flash, f"Utilisateur non connecté"
        logger.info("Utilisateur connecté !")

        
    def sedeconnecter(self):
        button_sedeco= self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'logout')]")))
        button_sedeco.click()
        
    def verifier_deconnexion(self):
        self.wait.until(EC.url_contains('login'))
        assert "login" in self.driver.current_url, "Déconnexion ratée"
        logger.info("Déconnexion réussie !")