import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import base64

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='android',
    appPackage='com.jrustonapps.myearthquakealerts',
    appActivity='com.jrustonapps.myearthquakealerts.controllers.MainActivity',
    language='pt',
    locale='br'
)

appium_server_url = 'http://127.0.0.1:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_maps(self) -> None:
        self.driver.start_recording_screen()
        Wait = WebDriverWait(self.driver,5)
        
        #CT1
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Durante o uso do app"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Durante o uso do app"]')
        el.click()
        
        Sleep = WebDriverWait(self.driver,5)
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="CANCEL"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="CANCEL"]')
        el.click()
        Sleep = WebDriverWait(self.driver,5)
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-1.png'
        self.driver.save_screenshot(directory + file_name)
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Mais opções"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Mais opções"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Settings"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Settings"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="My Region"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="My Region"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Your Country"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Your Country"]')
        el.click()
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-2.png'
        self.driver.save_screenshot(directory + file_name)
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Brasil"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Brasil"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Unit of Measurement"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Unit of Measurement"]')
        el.click()
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-3.png'
        self.driver.save_screenshot(directory + file_name)
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Km"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Km"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Settings"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Settings"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]')
        el.click()
        
        #CT2
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Search"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Search"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateFromText"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateFromText"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="07 maio 2023"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="07 maio 2023"]')
        el.click()
        
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-4.png'
        self.driver.save_screenshot(directory + file_name)
        
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="OK"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateToText"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateToText"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="10 maio 2023"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="10 maio 2023"]')
        el.click()
        
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-5.png'
        self.driver.save_screenshot(directory + file_name)
        
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="OK"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Interstitial close button"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Interstitial close button"]')
        el.click()
        
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-6.png'
        self.driver.save_screenshot(directory + file_name)
        
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Adana, Türkiye"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Adana, Türkiye"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Adana, Türkiye. Adana."]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Adana, Türkiye. Adana."]')
        el.click()
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-7.png'
        self.driver.save_screenshot(directory + file_name)
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Navegar para cima"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Navegar para cima"]')
        el.click()
        
        #CT3
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="All Magnitudes"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="All Magnitudes"]')
        el.click()
        
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-8.png'
        self.driver.save_screenshot(directory + file_name)
        
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="5.0+ Magnitude"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="5.0+ Magnitude"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Tonga"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Tonga"]')
        el.click()
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-9.png'
        self.driver.save_screenshot(directory + file_name)
                
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Navegar para cima"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Navegar para cima"]')
        el.click()
        
        #CT5
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Mais opções"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Mais opções"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Settings"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Settings"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="My Region"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="My Region"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Your Region"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Your Region"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Europe"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Europe"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Your Country"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Your Country"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Camarões"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Camarões"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Unit of Measurement"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Unit of Measurement"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Miles"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Miles"]')
        el.click()
        
        
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-my earth-10.png'
        self.driver.save_screenshot(directory + file_name)
        
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Settings"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Settings"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="mai. 7, 2023"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="mai. 7, 2023"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="07 maio 2023"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="07 maio 2023"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="OK"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="mai. 10, 2023"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="mai. 10, 2023"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="10 maio 2023"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="10 maio 2023"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="OK"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()
                
        
        filepath = os.path.join(directory, "screen_recording_Earth.mp4")
        payload = self.driver.stop_recording_screen()
        with open(filepath, "wb") as fd:
            fd.write(base64.b64decode(payload))

if __name__ == '__main__':
    unittest.main()