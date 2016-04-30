from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from element import BasePageElement
from locators import MainPageLocators, LoginLocator


class fillEmailText(BasePageElement):
    locator = 'email'

class fillPasswordText(BasePageElement):
    locator = 'password'

class pageTitleText(BasePageElement):
    locator = 'pagetitle'

class errorMessage(BasePageElement):
    locator = 'help-block'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    search_text_element_username = fillEmailText()
    search_text_element_password = fillPasswordText()
    get_pageTitle_Text = pageTitleText()
    get_Error_Message = errorMessage()

    def is_title_matches(self, value):
        return value in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def click_login(self):
        element = self.driver.find_element(*LoginLocator.LOGIN)
        element.click()




