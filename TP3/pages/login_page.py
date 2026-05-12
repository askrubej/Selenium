from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
import os
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage:
    URL="https://www.saucedemo.com"
    
    USERNAME=(By.ID, "user-name")
    PWD=(By.ID, "password")
    LOGIN=(By.ID, "login-button")
    
    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains)
        logger.info("Page ouverte...")
    
    def seconnecter(self, user, pwrd):
        logger.info("Remplissage du formulaire de login...")
        
        # Username
        self.driver.find_element(*self.USERNAME).send_keys(user)
        logger.info("Username saisi...")
                
        # Password
        self.driver.find_element(*self.PWD).send_keys(pwrd)
        logger.info("Password saisi...")

        # Login
        self.driver.find_element(*self.LOGIN).click()
        logger.info("Login effectué...")


    def verifier_connexion(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Products']")))
        titre=self.driver.find_element(By.XPATH, '//div[text()="Swag Labs"]')
        assert "Swag Labs" in titre.text, "Titre incorrect ou absent"
        logger.info("Connexion réussie !")
    
    def verifier_non_connexion(self):
        message=self.wait.until(EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Epic sadface')]")))
        assert message.is_displayed(), "Message d'erreur absent !"
        assert "inventory" not in self.driver.current_url, "Erreur : L'utilisateur n'est plus sur la page d'accueil !"
        logger.info(f"Connexion refusée !")