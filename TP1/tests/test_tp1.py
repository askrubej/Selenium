from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from pages.dropdown_page import DropdownPage
from pages.add_remove_page import AddRemovePage

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(options=options)


# try:
print("Demo POM dropdown")
login = LoginPage(driver)

print("Ouverture de la page")
login.open()
login.seconnecter()
login.verifier_connexion()
# login.sedeconnecter()
# login.verifier_deconnexion()

dd = DropdownPage(driver)
dd.open()
dd.choisir_option1("Option 1")
dd.verifier_option("Option 1")
dd.choisir_option1("Option 2")
dd.verifier_option("Option 2")

ar = AddRemovePage(driver)
ar.open()
ar.cliquer_add_element(3)
ar.verifier_boutons_delete(3)
ar.supprimer_element(1)
ar.verifier_boutons_delete(2)
ar.supprimer_tous_elements()
ar.verifier_boutons_delete(0)

