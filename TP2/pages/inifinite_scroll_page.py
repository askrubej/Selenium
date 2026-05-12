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

class InfiniteScrollPage:
    URL="https://the-internet.herokuapp.com/infinite_scroll"
        
    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains)
        logger.info("Page ouverte...")
        
    def verifier_premier_bloc(self):
        bloc = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "jscroll-inner"))
        )
        assert bloc.is_displayed(), "Premier bloc non visible"
        logger.info("Premier bloc présent")
        
    def scroller_vers_le_bas(self, fois=3):
        for i in range(fois):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)  # nécessaire : le scroll déclenche un chargement asynchrone
            logger.info(f"Scroll {i+1}/{fois} effectué")
            
    def compter_blocs(self):
        blocs = self.driver.find_elements(By.CLASS_NAME, "jscroll-added")
        total = len(blocs)
        logger.info(f"Blocs visibles : {total}")
        return total

    def verifier_augmentation(self, blocs_avant):
        blocs_apres=self.compter_blocs()
        assert blocs_apres > blocs_avant, "Aucun nouveau contenu ! "
        logger.info(f"Apparition de {blocs_apres} blocs en supplément des {blocs_avant} blocs initiaux")