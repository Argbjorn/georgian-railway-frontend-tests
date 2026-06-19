import pytest
from config import DESKTOP_VIEWPORT, MOBILE_DEVICE

DEVICES = ["mobile", "desktop"]

@pytest.fixture(scope="session", params=DEVICES, ids=DEVICES)
def device_type(request):
    return request.param

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright, device_type):
    if device_type == "mobile":
        return {
            **browser_context_args,
            **playwright.devices[MOBILE_DEVICE],
        }
    return {
        **browser_context_args,
        "viewport": DESKTOP_VIEWPORT,
    }
