import pytest

from config import BASE_URL

@pytest.fixture(scope="session", autouse=True)
def site_base_url():
    return BASE_URL

@pytest.fixture(autouse=True)
def _log_browser_diagnostics(page):
    # Surfaces real browser-side errors in the pytest failure output,
    # so CI failures show the actual cause instead of just the assertion.
    page.on("console", lambda msg: print(f"[console:{msg.type}] {msg.text}"))
    page.on("pageerror", lambda exc: print(f"[pageerror] {exc}"))
    yield