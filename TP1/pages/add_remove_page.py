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

class AddRemovePage:
    URL="https://the-internet.herokuapp.com/add_remove_elements/"
    
    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
        time.sleep(5)
        logger.info("Page ouverte...")
        
    def cliquer_add_element(self, nombre):
        for _ in range(nombre):
            self.driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
        #     time.sleep(2)
        # time.sleep(5)
        logger.info(f"Le bouton 'Add Element' a été cliqué {nombre} fois")
    
    def verifier_boutons_delete(self,nombre):
        nb=self.driver.find_elements(By.XPATH,"//button[text()='Delete']")
        logger.info(f"On a bien {len(nb)} boutons 'Delete'")
    
    def supprimer_element(self,nombre):
        self.driver.find_elements(By.XPATH, "//button[text()='Delete']")[0].click()
        logger.info(f"{nombre} élément supprimé")
        
    def supprimer_tous_elements(self):
        boutons = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
        for btn in boutons:
            btn.click()
        logger.info("Tous les éléments supprimés")