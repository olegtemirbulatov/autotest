from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from pages.topics_page import TopicsPage
from pages.login_page import LoginPage


class HomePage(BasePage):

    SIGN_IN_LINK_LOCATOR = (By.CSS_SELECTOR, "a.HeaderMenu-link--sign-in")
    OPEN_SOURCE_MENU_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Open Source']")
    TOPICS_BUTTON_LOCATOR = (By.XPATH, "//span[normalize-space()='Topics']")

    def go_to_topics(self):
        open_source_menu_button = self.wait.until(
            ec.presence_of_element_located(self.OPEN_SOURCE_MENU_BUTTON_LOCATOR)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(open_source_menu_button).perform()
        topics_button = self.wait.until(
            ec.element_to_be_clickable(self.TOPICS_BUTTON_LOCATOR)
        )
        topics_button.click()
        self.wait.until(lambda d: "/topics" in d.current_url)
        return TopicsPage(self.driver, self.driver.current_url)
    
    def go_to_login(self):
        sign_in_link = self.wait.until(
            ec.element_to_be_clickable(self.SIGN_IN_LINK_LOCATOR)
        )
        sign_in_link.click()
        self.wait.until(lambda d: "/login" in d.current_url)
        return LoginPage(self.driver, self.driver.current_url)