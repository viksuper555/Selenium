import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.utils import fill_data


def test_register():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('http://127.0.0.1:5000/register')
    fill_data(driver, "username", "Georgi")
    fill_data(driver, "email", "jorosuper555@gmail.com")
    fill_data(driver, "password", "12345678")
    driver.find_element(by=By.NAME, value="register").click()
    message = driver.find_element(by=By.CLASS_NAME, value="login-box-msg")
    assert message.text == 'User created please login'
    driver.quit()


def test_register_short_name():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('http://127.0.0.1:5000/register')
    username = driver.find_element(by=By.NAME, value="username")
    email = driver.find_element(by=By.NAME, value="email")
    password = driver.find_element(by=By.NAME, value="password")
    submit_button = driver.find_element(by=By.NAME, value="register")
    username.send_keys("S")  # Short name
    email.send_keys("viksuper555@gmail.com")
    password.send_keys("12345678")
    submit_button.click()
    validation_message = username.get_attribute("validationMessage")
    assert validation_message == 'Please lengthen this text to 3 characters or more (you are currently using 1 character).'
    driver.quit()


def test_register_bad_email():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('http://127.0.0.1:5000/register')
    username = driver.find_element(by=By.NAME, value="username")
    email = driver.find_element(by=By.NAME, value="email")
    password = driver.find_element(by=By.NAME, value="password")
    submit_button = driver.find_element(by=By.NAME, value="register")
    username.send_keys("Viktor")
    email.send_keys("123") # Bad email
    password.send_keys("12345678")
    submit_button.click()
    validation_message = email.get_attribute("validationMessage")
    assert validation_message == "Please include an '@' in the email address. '123' is missing an '@'."
    driver.quit()



if __name__ == '__main__':
    test_register()
