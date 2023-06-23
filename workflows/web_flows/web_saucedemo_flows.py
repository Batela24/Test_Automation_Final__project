import allure
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For
import page_objects.web_objects.main_page as main


class WebSaucedemoFlows:

    @staticmethod
    @allure.step('Login to saucedemo flow')
    def login_flow(user: str, password: str):
        UiActions.update_text(page.web_login.get_user_name(), user)
        UiActions.update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_submit())

    @staticmethod
    @allure.step('Verify saucedemo title flow')
    def verify_saucedemo_title(expected: str):
        wait(For.ELEMENT_EXISTS, main.main_title)
        actual = UiActions.text(page.web_main.get_main_title())
        Verifications.verify_equals(actual, expected)

