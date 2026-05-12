from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.notification_page import NotificationPage
from pages.inifinite_scroll_page import InfiniteScrollPage
import tests.test_tp2 

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

dc = DynamicControlsPage(driver)
dl = DynamicLoadingPage(driver)
notification=NotificationPage(driver)
isc=InfiniteScrollPage(driver)

try:
    dc.open()
    dc.verifier_page()
    dc.verifier_case()
    dc.cliquer_remove()
    dc.verifier_remove()
    dc.cliquer_add()
    dc.verifier_add()
    dc.verifier_champ_desactive()
    dc.cliquer_enable()
    dc.saisir_texte("yolo")

    dl.open()
    dl.aller_sur_exemple("2")
    dl.verifier_bouton_start()
    dl.cliquer_start()
    dl.verifier_texte("Hello World")

    notification.open()
    notification.lire_message()

    isc.open()
    isc.verifier_premier_bloc()
    blocs_avant=isc.compter_blocs()
    isc.scroller_vers_le_bas(5)
    isc.verifier_augmentation(blocs_avant)

except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

finally:
    driver.quit()