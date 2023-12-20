from selenium import webdriver
from selenium.webdriver.common.by import By

from apps import db
from apps.authentication.models import Users
from run import app
from tests.utils import fill_data


def test_login():
    with app.app_context():
        db.create_all()
        db.session.add(Users(username="Viktor", password="12345678", email="viksuper555@gmail.com"))
        db.session.commit()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get('http://127.0.0.1:5000/login')
    fill_data(driver, "username", "Viktor")
    fill_data(driver, "password", "12345678")
    driver.find_element(by=By.NAME, value="login").click()
    assert bool(driver.current_url.endswith('/index'))
    driver.quit()
