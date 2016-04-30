import unittest

import time
from selenium import webdriver
import page

class IndeeLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://preproduction.indee.tv")

    def test_login(self):

        # Login with invalid email and validating the browser title hasnt changed
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches("indee."), "indee. title doesn't match."
        main_page.click_login_button()
        main_page.search_text_element_username = "qaengineer@indee"
        main_page.search_text_element_password = "onboarding2016"
        main_page.click_login()
        assert main_page.is_title_matches("Login | Indee"), "Login | Indee title doesnt match"
        text = main_page.get_Error_Message
        assert text == "Enter a valid email."

     # Login with incorrect password and validating the browser title hasnt changed
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches("Login | Indee"), "Login | Indee title doesn't match."
        main_page.search_text_element_username = "qaengineer@indee.tv"
        main_page.search_text_element_password = "onboarding2016"
        main_page.click_login()
        assert main_page.is_title_matches("Login | Indee"), "Login | Indee title doesnt match"

    # Login with correct credentials and validating the projects page is displayed
        main_page.search_text_element_username = "QAengineer@indee.tv"
        main_page.search_text_element_password = "Onboarding2016"
        main_page.click_login()
        time.sleep(5)
        assert main_page.is_title_matches("Projects | Indee"), "Projects | Indee title doesnt match"
        text = main_page.get_pageTitle_Text
        assert text == "Projects"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
