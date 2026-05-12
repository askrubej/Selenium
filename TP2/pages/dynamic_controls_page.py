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

class DynamicControlsPage:
    URL="https://the-internet.herokuapp.com/dynamic_controls"
    
    
    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains)
        logger.info("Page ouverte...")
    
    def verifier_page(self):
        titre = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h4")))
        assert titre.is_displayed(), "Page non chargée"
        logger.info("Page chargée")
    
    def verifier_case(self):
        case=self.driver.find_element(By.ID, 'checkbox')
        assert case.is_enabled()
        logger.info("Case disponible")
        
    def cliquer_remove(self):
        self.driver.find_element(By.XPATH, "//button[text()='Remove']").click()
        logger.info("Cliqué sur 'Remove'...")
        
    def verifier_remove(self):
        message_remove = self.wait.until(EC.presence_of_element_located((By.ID, "message"))).text
        assert "It's gone!" in message_remove, f"Mauvais message affiché : {message_remove}"
        logger.info("Le bon message s'affiche après avoir cliqué sur 'Remove' !")
        
    def cliquer_add(self):
        self.driver.find_element(By.XPATH, "//button[text()='Add']").click()
        logger.info("Cliqué sur 'Add'...")

    def verifier_add(self):
        message_add = self.wait.until(EC.presence_of_element_located((By.ID, "message"))).text
        assert "It's back!" in message_add, f"Mauvais message affiché : {message_add}"
        logger.info("Le bon message s'affiche après avoir cliqué sur 'Add' !")
        
    def verifier_champ_desactive(self):
        champ = self.driver.find_element(By.XPATH, "//input[@type='text']")
        assert not champ.is_enabled(), "Le champ devrait être désactivé"
        logger.info("Le champ est bien désactivé !")
        
    def cliquer_enable(self):
        self.driver.find_element(By.XPATH, "//button[text()='Enable']").click()
        logger.info("Cliqué sur le bouton 'Enable'...")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']" )))
        logger.info("Champ actif")
        
    def saisir_texte(self, texte):
        self.driver.find_element(By.XPATH, "//input[@type='text']" ).send_keys(texte)
        
