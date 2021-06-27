import time
import pytest
from selenium.webdriver.common.keys import Keys
from Pages.Locators import Locus
from Drivers.browser import driver
from pytest_bdd import when, given, then, scenario, parsers
from Source.conftest import wait_and_send, wait_and_click, wait_till_element_present, names

task_id = names()


@pytest.mark.invalid_login()
@scenario('../Features/SDET_Assignment.feature', 'Login with invalid credentials')
def test_invalid_login():
    pass


@pytest.mark.login()
@scenario('../Features/SDET_Assignment.feature', 'Login with valid credentials')
def test_valid_login():
    pass


@pytest.mark.profile()
@scenario('../Features/SDET_Assignment.feature', 'User verified/Check personnel profile')
def test_profile():
    pass


@pytest.mark.search()
@scenario('../Features/SDET_Assignment.feature', 'User searches for a task with task id')
def test_search():
    pass


@pytest.mark.create()
@scenario('../Features/SDET_Assignment.feature', 'User creates a new task and searches for the created task')
def test_create_task():
    pass


@given("User navigates to Locus hiring dashboard")
def initialize_test():
    pass                                            #Since we are already using a pre-test function in conftest.py file


@when(parsers.parse("User enter {types} user id and click continue"))
def user_id(types):
    if types == "invalid":
        wait_and_send("xpath", Locus.txt_user_id, "candidate")
    else:
        wait_and_send("xpath", Locus.txt_user_id, "test-hiring/personnel/web-test")
    wait_and_click("xpath", Locus.btn_continue)


@then(parsers.parse("User enters {types} password and try to login"))
def password(types):
    if types == "invalid":
        wait_and_send("xpath", Locus.txt_password, "1234")
    else:
        wait_and_send("xpath", Locus.txt_password, "9HQ?#$B2-jQdP+B&")
    wait_and_click("xpath", Locus.btn_Login)


@then("User is in Home page")
def home_page():
    wait_till_element_present("css", Locus.left_side_bar)


@then("Alert message is displayed for invalid password")
def login_alert_message():
    wait_till_element_present("xpath", Locus.alert_message)


@then("User hovers over profile icon and verify personal details")
def verify_personal_details():
    wait_and_click("xpath", Locus.icn_profile)
    assert driver.find_element_by_xpath(Locus.title_user).text == "web-test"


@then(parsers.parse("User searches for a {types} task and verify the search result"))
def search_and_verify(types):
    wait_and_click("xpath", Locus.icn_search)
    if types == "existing":
        wait_and_send("xpath", Locus.txt_search_area, "2020-10-10-test-1")
    else:
        wait_and_send("xpath", Locus.txt_search_area, task_id)
    wait_till_element_present("xpath", Locus.search_result)
    assert len(driver.find_elements_by_xpath(Locus.search_result)) > 1
    driver.find_element_by_xpath(Locus.txt_search_area).send_keys(Keys.ESCAPE)


@then("User clicks on add task button and enter id, team")
def create_task():
    wait_and_click("xpath", Locus.btn_add_task)
    wait_and_send("xpath", Locus.txt_task_id, task_id)
    wait_and_click("xpath", Locus.drp_team)
    wait_and_click("xpath", Locus.drp_option)
    wait_and_click("xpath", Locus.btn_proceed)


@then("User enters address, slot and change visit type to Service")
def task_details():
    i = 1
    wait_and_click("xpath", Locus.btn_slot)
    wait_and_send("xpath", Locus.txt_slot, "120")
    wait_and_click("xpath", Locus.btn_save)
    type_drop_down = driver.find_elements_by_xpath(Locus.drp_type)
    while i < 3:
        type_drop_down[i].click()
        time.sleep(1)
        wait_and_click("xpath", Locus.drp_type_option)
        i = i+1
    wait_and_send("id", Locus.txt_address, "sony signal, koramangala, bangalore")
    time.sleep(3)
    driver.find_element_by_id(Locus.txt_address).send_keys(Keys.ENTER)
    time.sleep(2)


@then("User clicks on create task and verifies ticket is created")
def task_created():
    wait_and_click("xpath", Locus.btn_create_task)
    wait_till_element_present("xpath", Locus.task_header)
    wait_and_click("xpath", Locus.icn_close)





