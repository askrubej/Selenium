from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from pages.dropdown_page import DropdownPage
from pages.add_remove_page import AddRemovePage

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


# try:
print("Demo POM dropdown")
login = LoginPage(driver)

print("Ouverture de la page")
login.open()
login.seconnecter()
login.verifier_connexion()
login.sedeconnecter()
login.verifier_deconnexion()

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

driver.quit()
