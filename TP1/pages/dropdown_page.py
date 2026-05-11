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

class DropdownPage:
    URL="https://the-internet.herokuapp.com/dropdown"
    
    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
        logger.info("Page ouverte...")
        
        dropdown=self.wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
        assert dropdown.is_displayed(), "Dropdown non disponible"
        logger.info("Dropdown présent...")
        
    def choisir_option1(self, option):
        # On localise la balise <select>.
        dropdown_element = self.driver.find_element(By.ID, "dropdown")
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(option)
        logger.info(f"Sélection de {option} ")
    
    def verifier_option(self, option):
        dropdown_element = self.driver.find_element(By.ID, "dropdown")
        dropdown = Select(dropdown_element)
        selected_option = dropdown.first_selected_option
        selected_text = selected_option.text
        assert selected_text == option, f"Texte sélectionné incorrect : {selected_text}"
        logger.info(f"{option} est séléctionnée !")

