import pytest

from pages.duckduckgo.search_page import SearchPage


class TestSearch:

    @pytest.mark.parametrize("query", ["qa", "aqa", "python"])
    @pytest.mark.ui
    def test_search(self, ddg_search_page: SearchPage, query: str) -> None:
        search_page = ddg_search_page.open().search(query).expect_search_results()
        assert search_page.get_search_results_count() > 5
