from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MyTestClass:
    def test_invalid_example(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, "#user-name"))
        elem = driver.find_element(By.CSS_SELECTOR, "#user-name")
        elem.clear()
        elem.send_keys("standard_user")
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, "#password"))
        elem = driver.find_element(By.CSS_SELECTOR, "#password")
        elem.clear()
        elem.send_keys("secret_sauce\n")
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, "#inventory_container"))
        elem = driver.find_element(By.CSS_SELECTOR, "#inventory_container")
        assert elem
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, "span.title"))
        elem = driver.find_element(By.CSS_SELECTOR, "span.title")
        elem = elem.text
        assert elem == "PRODUCTS"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, 'button[name*="backpack"]'))
        elem = driver.find_element(By.CSS_SELECTOR, 'button[name*="backpack"]')
        elem.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, "#shopping_cart_container a"))
        elem = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container a')
        elem.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, "span.title"))
        elem = driver.find_element(By.CSS_SELECTOR, "span.title")
        elem = elem.text
        assert elem == "YOUR CART"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, "div.cart_item"))
        elem = driver.find_element(By.CSS_SELECTOR, "div.cart_item")
        elem = elem.text
        assert elem == "Backpack"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, 'button:contains("Remove")'))
        elem = driver.find_element(By.CSS_SELECTOR, 'button:contains("Remove")')
        elem.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.CSS_SELECTOR, "a#logout_sidebar_link"))
        elem = driver.find_element(By.CSS_SELECTOR, 'a#logout_sidebar_link')
        elem.click()
        driver.close()
