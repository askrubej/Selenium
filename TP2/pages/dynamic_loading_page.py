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

class DynamicLoadingPage:
    URL="https://the-internet.herokuapp.com/dynamic_loading"
        
    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains)
        logger.info("Page ouverte...")
        
    def aller_sur_exemple(self,numero):
        self.driver.find_element(By.XPATH, f'//a[contains(text(),"Example {numero}")]').click()
        logger.info(f"Cliqué sur exemple {numero}...")
    
    def verifier_bouton_start(self): ######################
        btn=self.wait.until(EC.presence_of_element_located((By.XPATH,'//button[text()="Start"]')))
        assert btn.is_displayed(), "Bouton Start non visible"
        logger.info("Bouton Start présent !")
    
    def cliquer_start(self):
        self.driver.find_element(By.XPATH,'//button[text()="Start"]').click()
        logger.info(f"Cliqué sur le bouton Start...")
        
    def verifier_texte(self, texte_suppose): ################################
        texte=self.wait.until(EC.presence_of_element_located((By.ID, "finish"))).text
        assert texte_suppose in texte, f"Texte non correct"
        logger.info("Texte correct affiché !")