from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
import os
from utils.logger import get_logger

logger = get_logger(__name__)

class CartPage:
    URL="https://www.saucedemo.com/cart.html"
    

    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains)
        logger.info("Page du panier ouverte...")
        
    def verifier_presence_produit(self, produit):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
        noms_panier=self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        noms_texte=[n.text for n in noms_panier]
        assert produit in noms_texte, f"Produit {produit} absent du panier"
        logger.info(f"Le produit {produit} est bel et bien dans le panier !")
        
    def verifier_prix(self,prix_produit):
        prix_affiche=self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
        assert prix_affiche==prix_produit, "Le prix du panier ne correspond pas au prix du produit"
        logger.info("Le prix dans le panier est correct !")

