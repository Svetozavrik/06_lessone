from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(( By.CSS_SELECTOR,"button.start"))
        )
    start_button.click()

    wait = WebDriverWait(driver, 20)
    hello_world_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#finish h4"))
        )
    driver.save_screenshot("result.png")
    assert hello_world_element.text == "Hello World!"

    print(hello_world_element.text)

    driver.quit()

  
       
