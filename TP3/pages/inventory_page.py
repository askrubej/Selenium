from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import os
from utils.logger import get_logger

logger = get_logger(__name__)

class InventoryPage:
    URL="https://www.saucedemo.com"
    

    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        

    def ajouter_produit(self, nom_produit):
        xpath = f"//div[text()='{nom_produit}']/ancestor::div[@class='inventory_item']//button"
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn.click()
        logger.info(f"Produit ajouté : {nom_produit}")
        screenshot_name = f"screenshots/ajout_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        self.driver.save_screenshot(screenshot_name)
    
    def verifier_ajout_produit(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack")))
        logger.info("Le produit a été ajouté au panier")
        nombre_panier=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").text 
        assert nombre_panier=="1", f"Nombre de produits dans le panier incorrect : {nombre_panier}"
        logger.info(f"Il y a bien {nombre_panier} produit(s) dans le panier !")
    
    def recuperer_prix_produit(self, nom_produit):
        xpath = f"//div[text()='{nom_produit}']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']"
        prix = self.driver.find_element(By.XPATH, xpath).text
        logger.info(f"Prix récupéré pour {nom_produit} : {prix}")
        return prix