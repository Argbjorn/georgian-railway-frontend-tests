import pytest

def test_main_page_opens_and_has_correct_title(page, base_url):
    page.goto(base_url)
    page.wait_for_load_state("networkidle")
    assert page.title() == "Georgian Railway Map"