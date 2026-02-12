import pytest
from config import LANGUAGES
from pages.header import switch_language
from tests.helpers import assert_url_equals, open_routes_page

page_titles = {"en": "Routes", "ru": "Поезда", "ka": "მატარებლები"}

@pytest.mark.parametrize("language", LANGUAGES)
def test_routes_page_has_correct_h1(page, site_base_url, language):
    open_routes_page(page, site_base_url, language)
    assert page.locator("h1").inner_text() == page_titles[language]

def test_routes_page_has_routes_links(page, site_base_url):
    open_routes_page(page, site_base_url, "en")
    assert page.locator(".hextra-card").count() > 0

def test_routes_page_has_correct_routes_links(page, site_base_url):
    open_routes_page(page, site_base_url, "en")
    page.get_by_role("link", name="801: Batumi → Tbilisi", exact=True).click()
    assert_url_equals(page, site_base_url["en"] + "routes/801/")