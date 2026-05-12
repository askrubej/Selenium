from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage
# import tests.test_tp2 

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
options.add_argument("--password-store=basic")
options.add_experimental_option("prefs", {
    "profile.password_manager_leak_detection": False
})

driver = webdriver.Chrome(options=options)

page = LoginPage(driver)
inven=InventoryPage(driver)
cart=CartPage(driver)
co=CheckoutPage(driver)
coc=CheckoutCompletePage(driver)
#SCENARIO 1
# page.open()
# page.seconnecter("standard_user", "secret_sauce")
# page.verifier_connexion()

#SCENARIO 2
# page.open()
# page.seconnecter("locked_out_user", "secret_sauce")
# page.verifier_non_connexion()

# #SCENARIO 3
# page.open()
# page.seconnecter("standard_user", "secret_sauce")
# inven.ajouter_produit("Sauce Labs Backpack")
# inven.verifier_ajout_produit()
# prix_produit=inven.recuperer_prix_produit("Sauce Labs Backpack")
# cart.open()
# cart.verifier_presence_produit("Sauce Labs Backpack")
# cart.verifier_prix(prix_produit)

#SCENARIO 4
page.open()
page.seconnecter("standard_user", "secret_sauce")
inven.ajouter_produit("Sauce Labs Backpack")
inven.verifier_ajout_produit()
prix_produit=inven.recuperer_prix_produit("Sauce Labs Backpack")
cart.open()
cart.verifier_presence_produit("Sauce Labs Backpack")
cart.verifier_prix(prix_produit)
co.open()
co.saisir_informations("John", "Doe", "59000")
coc.open()
coc.verifier_presence_produit("Sauce Labs Backpack")
coc.verifier_prix(prix_produit)
coc.verifier_prix_horstaxe(prix_produit)
coc.verifier_taxe()
coc.verifier_sous_total()
coc.cliquer_finish()
coc.verifier_message()