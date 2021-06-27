import pytest
from Drivers.browser import driver
from datetime import datetime
from Pages.Locators import Locus
from pytest_bdd import when,then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 30)


@pytest.fixture(scope="function", autouse=True)
def pretest(request):                                                      #Pre-test which will run before every test function
    Locus_login_page()
    yield driver
    sign_out(request)


@pytest.fixture(scope="session", autouse=True)
def posttest():
    yield driver                                                    #teardown at the end of every session
    driver.quit()


def Locus_login_page():
    driver.get("https://test-hiring.locus-dashboard.com/#/login")
    wait_and_click("xpath", Locus.btn_Login)


@when("User is login page")
def home_assert():
    wait_till_element_present("xpath", Locus.txt_user_id)


def sign_out(request):
    if "invalid_login" in request.keywords:
        pass
    elif "profile" in request.keywords:
        wait_and_click("xpath", Locus.signout)
    else:
        wait_and_click("xpath", Locus.icn_profile)
        wait_and_click("xpath", Locus.signout)


def wait_and_click(locator_type, element):
    if locator_type == "id":
        wait.until(EC.element_to_be_clickable((By.ID, element))).click()
    elif locator_type == "xpath":
        wait.until(EC.element_to_be_clickable((By.XPATH, element))).click()
    elif locator_type == "css":
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element))).click()


def wait_and_send(locator_type, element, text):
    if locator_type == "id":
        wait.until(EC.element_to_be_clickable((By.ID, element))).send_keys(text)
    elif locator_type == "xpath":
        wait.until(EC.element_to_be_clickable((By.XPATH, element))).send_keys(text)


def wait_till_element_present(locator_type, element):
    if locator_type == "id":
        wait.until(EC.presence_of_element_located((By.ID, element)))
    elif locator_type == "xpath":
        wait.until(EC.presence_of_element_located((By.XPATH, element)))


def names():
    date = str(datetime.now().date())
    now = datetime.now()
    temp = ('%02d%02d%d' % (now.minute, now.second, now.microsecond))[:-4]
    name = str(date+temp)
    return name
