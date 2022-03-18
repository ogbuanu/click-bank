import requests
import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from constants import *

class ClickBank(webdriver.Chrome):

    def __init__(self,driver_path=r"C:\selenium_drivers",teardown=False) -> None:
        self.teardown = teardown
        self.driver_path = os.environ.get("CHROMEDRIVER_PATH") or driver_path
        os.environ['PATH'] += driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        options.add_experimental_option("detach", True)
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        super(ClickBank,self).__init__(options=options,executable_path=os.environ.get("CHROMEDRIVER_PATH"))
        # super(ClickBank,self).__init__(options=options,)
        # self.implicitly_wait(15)


    def __call__(self):

        self.get_page()
        time.sleep(5)
        body_element = self.get_body_element()
        # print(self)
        body_element.click()
        time.sleep(5)
        self.quit()
        
        
    def __exit__(self, *args):
        if self.teardown:
            self.quit()
        # return super().__exit__(*args)
    def get_page(self):
        self.get(BASE_URL)
    
    def get_body_element(self):
        # -1 0 11 12
        # 0 0 12 12
        WebDriverWait(self,30).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        body_element = self.find_element(By.TAG_NAME, 'body')
        return body_element
    
        
        