from pages.base_page import BasePage


class TopicsPage(BasePage):

    def get_popular_topics(self):
        return self.page.locator("//a[contains(@href, '/topics/')]/p[1]").all_inner_texts()
