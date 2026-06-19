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

# pytest hook to deselect unsupported test cases for mobile Firefox
def pytest_collection_modifyitems(config, items):
    selected, deselected = [], []
    for item in items:
        callspec = getattr(item, "callspec", None)
        is_unsupported = (
            callspec
            and callspec.params.get("device_type") == "mobile"
            and callspec.params.get("browser_name") == "firefox"
        )
        (deselected if is_unsupported else selected).append(item)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected
