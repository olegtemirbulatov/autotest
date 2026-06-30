from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class TopicsPage(BasePage):

    TOPICS_LOCATOR = (By.XPATH, "//a[contains(@href, '/topics/')]/p[1]")

    def get_popular_topics(self) -> list[str]:
        topics_elements_list = self.wait.until(
            ec.presence_of_all_elements_located(self.TOPICS_LOCATOR)
        )
        return [topic.text for topic in topics_elements_list]
