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

class NotificationPage:
    URL="https://the-internet.herokuapp.com/notification_message_rendered"
        
    def __init__(self,driver,timeout=10):
        self.driver =  driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains)
        logger.info("Page ouverte...")
        
    def lire_message(self):
        message = self.wait.until(
            EC.presence_of_element_located((By.ID, "flash-messages"))
        )
        logger.info(f"Message lu : {message.text.strip()}")
        return message.text.strip()
    
    def cliquer_clickhere(self):
        self.find.element(By.XPATH, '//a[text()="Click here"]').click()
        