import pytest
from selene import browser
from selene.support.shared import config


@pytest.fixture(autouse=True)
def setup_teardown():
    browser.open(config.base_url)
    yield
    browser.quit()


@pytest.fixture(autouse=True)
def setup_browser():
    config.timeout = 1
    config.window_width = 1920
    config.window_height = 1080
    config.base_url = 'https://www.google.com/'