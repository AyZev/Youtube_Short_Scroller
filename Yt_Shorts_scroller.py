from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://youtube.com/shorts")
n = 10
actions.send_keys(Keys.SPACE).perform()
for i in range(n):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "player")))
    while True:
        if driver.find_elements(By.CLASS_NAME, "ad-created"):
            actions.send_keys(Keys.ARROW_DOWN).perform()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ytPlayerProgressBarDragContainer")))
        progress_bar = driver.find_element(By.CLASS_NAME, "ytPlayerProgressBarDragContainer")
        progress = int(progress_bar.get_attribute("aria-valuenow"))
        if progress >= 97:
            actions.send_keys(Keys.ARROW_DOWN).perform()
            break
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ytPlayerProgressBarDragContainer")))
        print(f"Finished short {i+1}.......")
    except Exception as e:
        print(f"Error while waiting for next video: {str(e)}")
    sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "player")))

driver.close()
