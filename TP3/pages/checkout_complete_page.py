from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
import os
from utils.logger import get_logger

logger = get_logger(__name__)

class CheckoutCompletePage:
    URL="https://www.saucedemo.com/checkout-step-two.html"
    
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
        
    def verifier_presence_produit(self, produit):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
        noms_panier=self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        noms_texte=[n.text for n in noms_panier]
        assert produit in noms_texte, f"Produit {produit} absent du panier"
        logger.info(f"Le produit {produit} est bel et bien dans le panier final !")
        
    def verifier_prix(self,prix_produit):
        prix_affiche=self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
        assert prix_affiche==prix_produit, "Le prix du panier ne correspond pas au prix du produit"
        logger.info(f"Le prix dans le panier final est correct : {prix_produit} !")
        
    def verifier_prix_horstaxe(self, prix_produit) :
        prix_ht=self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        assert prix_produit in prix_ht, "Le prix hors-taxe ne correspond pas au prix du produit"
        logger.info(f"Le prix hors-taxe dans le panier final est correct : {prix_produit} !")    
        
    def verifier_taxe(self):
        taxe=self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        assert taxe, "Taxe non affichée"
        logger.info(f"La taxe s'affiche correctement : {taxe}")
    
    def verifier_sous_total(self):
        sous_total_texte = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        taxe_texte = self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        total_texte = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text

    # Extraire les valeurs numériques
        sous_total = float(sous_total_texte.split("$")[1])
        taxe = float(taxe_texte.split("$")[1])
        total = float(total_texte.split("$")[1])

        assert round(sous_total + taxe, 2) == total, f"Total incohérent : {sous_total} + {taxe} ≠ {total}"
        logger.info(f"Total cohérent : {sous_total} + {taxe} = {total}")

    def cliquer_finish(self):
        bouton_finish=self.driver.find_element(By.ID, "finish")
        bouton_finish.click()
    
    def verifier_message(self):
        message=self.driver.find_element(By.CLASS_NAME, "complete-header").text 
        assert "Thank you for your order!" in message, f"Message faux"
        logger.info("Message correct")
        