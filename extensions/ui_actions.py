import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf


class UiActions:

    @staticmethod
    @allure.step('click on element')
    def click(elem):
        elem.click()

    @staticmethod
    @allure.step('updating text')
    def update_text(elem: WebElement, value: str):
        elem.send_keys(value)

    @staticmethod
    @allure.step('mouse hover tooltip')
    def mouse_hover_tooltip(elem: WebElement):
        ActionChains(conf.driver).move_to_element(elem).click().perform()

    @staticmethod
    @allure.step('mouse hover two elements')
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        ActionChains(conf.driver).move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('right click')
    def right_click(elem: WebElement):
        ActionChains(conf.driver).context_click(elem).perform()

    @staticmethod
    @allure.step('drag and drop')
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        ActionChains(conf.driver).drag_and_drop(elem1, elem2).perform()

    @staticmethod
    @allure.step('clear text field in element')
    def clear(elem: WebElement):
        elem.clear()

    @staticmethod
    @allure.step('click enter')
    def do_enter():
        ActionChains(conf.driver).send_keys(Keys.ENTER).perform()

    @staticmethod
    @allure.step('return the text from element')
    def text(elem: WebElement):
        if elem.tag_name == "input":
            return elem.get_attribute("value")
        else:
            return elem.text

    @staticmethod
    @allure.step('return a string in lower letters')
    def lower_letters(word: str):
        return word.lower()

    @staticmethod
    @allure.step('return the source url for new tab')
    def move_to_new_tab_and_get_source_url():
        # return the current tab
        current_tab = conf.driver.current_window_handle
        # select to move into the new tab
        tabs = conf.driver.window_handles
        conf.driver.switch_to.window(tabs[1])
        page_source_url = conf.driver.current_url
        # close the new tab and return to the first page
        conf.driver.close()
        conf.driver.switch_to.window(current_tab)
        return page_source_url
