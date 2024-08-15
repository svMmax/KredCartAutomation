import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# to customise the command line
# added --browser parameter to command line
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


# we need to add command liner --browser
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test Run - Browser Chrome")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()
    else:
        # driver = webdriver.Chrome()
        print("Test Run - Browser Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://automation.credence.in/shop")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(params=[
    ("2may2024@gmail.com", "Test@123", "Login_Pass"),
    ("2may2024@gmail.com1", "Test@123", "Login_Fail"),
    ("2may2024@gmail.com", "Test@1231", "Login_Fail"),
    ("2may2024@gmail.com1", "Test@1231", "Login_Fail")
])
def getDataForLogin(request):
    return request.param
