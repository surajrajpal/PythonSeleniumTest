from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.btn-link')

class SearchResultsPageLocators(object):
    pass

class UsernameField(object):
    USERNAME_FIELD = (By.NAME,'email')

class PasswordField(object):
    PASSWORD_FIELD = (By.NAME,'password')

class LoginLocator(object):
    LOGIN = (By.CSS_SELECTOR,'button.login')

class pageTitle(object):
    PAGE_TITLE = (By.CSS_SELECTOR,'.pagetitle')

class errorMessage(object):
    ERROR_MESSAGE = (By.CLASS_NAME,'help-block')