from selenium.webdriver.common.by import By


def fill_data(driver, id, value):
    driver.find_element(by=By.NAME, value=id).send_keys(value)
