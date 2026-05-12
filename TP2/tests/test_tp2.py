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

def verifier_page():
    titre = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h4")))
    assert titre.is_displayed(), "Page non chargée"
    logger.info("Page chargée")
    
    
def verifier_case():
    case=self.driver.find_element(By.ID, 'checkbox')
    assert case.is_enabled()