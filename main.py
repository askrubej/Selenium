from selenium import webdriver
from books_page import BooksPage

driver=webdriver.Chrome()

try :
    page=BooksPage(driver)
    
    page.open()

    # Test phase 2
    livres = page.extraire_livres()
    print(f"{len(livres)} livres extraits")
    for i, l in enumerate(livres[:3], start=1):
        print(f"  {i}. {l['Titre']} - {l['Prix']}")


except AssertionError as e:
    print(f"Erreur d'assertion : {e}")
    
except Exception as e:
    print(f"Erreur : {e}")
    
finally:
    driver.quit()
    print("Navigateur fermé")
 