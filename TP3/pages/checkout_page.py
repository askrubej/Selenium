from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
import os
from utils.logger import get_logger

logger = get_logger(__name__)

class CheckoutPage:
    URL="https://www.saucedemo.com/checkout-step-one.html"
    
    FIRSTNAME=(By.ID, 'first-name')
    LASTNAME=(By.ID, 'last-name')
    CODEPOSTAL=(By.ID, 'postal-code')


    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains)
        logger.info("Page du checkout ouverte...")
        
    def saisir_informations(self, prenom, nom, codepostal):
        self.driver.find_element(*self.FIRSTNAME).send_keys(prenom)
        self.driver.find_element(*self.LASTNAME).send_keys(nom)
        self.driver.find_element(*self.CODEPOSTAL).send_keys(codepostal)
        logger.info("Informations saisies...")