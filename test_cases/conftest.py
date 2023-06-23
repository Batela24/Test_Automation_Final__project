import allure
import mysql.connector
import pytest
import selenium.webdriver
import appium.webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from applitools.selenium import Eyes
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages
from extensions.ui_actions import UiActions

driver = None
action = None

# for mobile actions:
action2 = None
m_action = None
mobile_size = None

# applitools
eyes = Eyes()

# DB integration:
db_connector = None


####################################################################################
# Function name: init_web_saucedemo
# Function Description: This fixture init the driver - in Saucedemo tests
# Function Parameters: Request
####################################################################################
@pytest.fixture(scope='class')
def init_web_saucedemo(request):
    init_web_driver(request, get_data("UrlSaucedemo"))
    ManagePages.init_web_saucedemo_pages()
    yield
    request.cls.driver.quit()
    close_applitools_connection()


####################################################################################
# Function name: init_web_rottentomatoes
# Function Description: This fixture init the driver - in Rottentomatoes tests
# Function Parameters: Request
####################################################################################
@pytest.fixture(scope='class')
def init_web_rottentomatoes(request):
    init_web_driver(request, get_data("UrlRottentomatoes"))
    ManagePages.init_web_rottentomatoes_pages()
    yield
    request.cls.driver.quit()
    close_applitools_connection()


####################################################################################
# Function name: init_web_driver
# Function Description: This function is general init for being used in the separated web init functions
# Function Parameters: Request, String - url
####################################################################################
def init_web_driver(request, url):
    if UiActions.lower_letters(get_data('Execute_Applitools')) == 'yes':
        globals()['driver'] = get_web_driver()
    else:
        edriver = get_web_driver()
        globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(url)
    request.cls.driver = driver
    # globals()['action'] = ActionChains(driver)
    if get_data('Execute_Applitools').lower() == 'yes':
        eyes.api_key = get_data('Applitools_Key')


####################################################################################
# Function name: close_applitools_connection
# Function Description: This function close the Applitools after the process finished
####################################################################################
def close_applitools_connection():
    if UiActions.lower_letters(get_data('Execute_Applitools')) == 'yes':
        eyes.close()  # applitools
        eyes.abort()  # applitools


####################################################################################
# Function name: init_mobile_driver
# Function Description: This fixture init the driver - in Mobile tests
# Function Parameters: Request
####################################################################################
@pytest.fixture(scope='class')
def init_mobile_driver(request):
    edriver = get_mobile_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = TouchAction(driver)
    request.cls.action = globals()['action']
    globals()['action2'] = TouchAction(driver)
    request.cls.action2 = globals()['action2']
    globals()['m_action'] = MultiAction(driver)
    request.cls.m_action = globals()['m_action']
    globals()['mobile_size'] = driver.get_window_size()
    request.cls.mobile_size = globals()['mobile_size']
    ManagePages.init_mobile_pages()
    yield
    driver.quit()


####################################################################################
# Function name: init_electron_driver
# Function Description: This fixture init the driver - in Electron tests
# Function Parameters: Request
####################################################################################
@pytest.fixture(scope='class')
def init_electron_driver(request):
    edriver = get_electron_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_electron_pages()
    yield
    driver.quit()


####################################################################################
# Function name: init_desktop_driver
# Function Description: This fixture init the driver - in Desktop tests
# Function Parameters: Request
####################################################################################
@pytest.fixture(scope='class')
def init_desktop_driver(request):
    edriver = get_desktop_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()
    yield
    driver.quit()


####################################################################################
# Function name: init_db_connection
# Function Description: This fixture defines db connection parameters  - in DB tests
# Function Parameters: Request
####################################################################################
# define db connection parameters
@pytest.fixture(scope='class')
def init_db_connection(request):
    db_connector = mysql.connector.connect(
        host=get_data('DB_Host'),
        database=get_data('DB_Name'),
        user=get_data('DB_User'),
        password=get_data('DB_Pass')
    )
    globals()['db_connector'] = db_connector
    request.cls.db_connector = db_connector
    yield
    db_connector.close()


####################################################################################
# Function name: get_web_driver
# Function Description: This function defines the driver options - on Web
# Function Return: driver
####################################################################################
def get_web_driver():
    # if we want to get the browser parameter from jenkins, need to use:
    # web_driver = os.getenv('Browser')
    web_driver = get_data('Browser')
    if UiActions.lower_letters(web_driver) == 'chrome':
        driver = get_chrome()
    elif UiActions.lower_letters(web_driver) == 'firefox':
        driver = get_firefox()
    elif UiActions.lower_letters(web_driver) == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception("Wrong Input, Unrecognized Browser")
    return driver


####################################################################################
# Function name: get_mobile_driver
# Function Description: This function defines the driver options - on Mobile
# Function Return: String - driver
####################################################################################
def get_mobile_driver():
    if UiActions.lower_letters(get_data('Mobile_Device')) == 'android':
        driver = get_android(get_data('Udid'))
    elif UiActions.lower_letters(get_data('Mobile_Device')) == 'ios':
        driver = get_ios(get_data('Udid'))
    else:
        driver = None
        raise Exception("Wrong input, unrecognized mobile OS")
    return driver


####################################################################################
# Function name: get_electron_driver
# Function Description: This function defines the driver option - on Electron
# Function Return: driver
####################################################################################
def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data('Electron_App')
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data('Electron_Driver'))
    return driver


####################################################################################
# Function name: get_desktop_driver
# Function Description: This function defines Desktop connection driver
# Function Return: driver
####################################################################################
def get_desktop_driver():
    dc = {}
    dc['app'] = get_data('Application_Name')
    dc['platformName'] = 'Windows'
    dc['deviceName'] = 'WindowsPC'
    driver = appium.webdriver.Remote(get_data('WinAppDriver_Service'), dc)
    return driver


####################################################################################
# Function name: get_chrome
# Function Description: This function defines Chrome driver connection
# Function Return: chrome_driver
####################################################################################
def get_chrome():
    # for selenium 4.x:
    # srv = Service(ChromeDriverManager().install())
    # chrome_driver = selenium.webdriver.Chrome(service=srv)
    # for selenium 3.X:
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver


####################################################################################
# Function name: get_firefox
# Function Description: This function defines Firefox driver connection
# Function Return: ff_driver
####################################################################################
def get_firefox():
    # for selenium 4.x:
    # srv = Service(executable_path=GeckoDriverManager().install())
    # ff_driver = selenium.webdriver.Firefox(service=srv)
    # for selenium 3.X:
    ff_driver = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return ff_driver


####################################################################################
# Function name: get_edge
# Function Description: This function defines Edge driver connection
# Function Return: edge_driver
####################################################################################
def get_edge():
    # for selenium 4.x:
    # srv = Service(EdgeChromiumDriverManager(log_level=20).install())
    # edge_driver = selenium.webdriver.Edge(service=srv)
    # for selenium 3.X:
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
    return edge_driver


####################################################################################
# Function name: get_android
# Function Description: This function defines the Android Mobile connection parameters and driver connection
# Function Parameters: String - udid
# Function Return: android_driver
####################################################################################
def get_android(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data('App_Package')
    dc['appActivity'] = get_data('App_Activity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data('Appium_Server'), dc)
    return android_driver


####################################################################################
# Function name: get_ios
# Function Description: This function defines the IOS Mobile connection parameters and driver connection
# Function Parameters: String - udid
# Function Return: ios_driver
####################################################################################
def get_ios(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_data('Bundle_ID')
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_data('Appium_Server'), dc)
    return ios_driver


####################################################################################
# Function name: pytest_exception_interact
# Function Description: This function catch exceptions and errors and save an image
# Function Parameters: node, cell, report
####################################################################################
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:  # if it is None -> this is exception from API test
            image = get_data('ScreenshotPath') + 'screen_' + str(get_time_stamp()) + '.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
