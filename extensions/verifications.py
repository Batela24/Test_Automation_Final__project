import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:

    @staticmethod
    @allure.step('verify equals')
    def verify_equals(actual, expected):
        assert actual == expected, "Verify Equals Failed, Actual: " + str(actual) + " is not Equals to Expected: "\
                                   + str(expected)

    @staticmethod
    @allure.step('verify element is displayed')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), "Verify is Displayed Failed, Element:  " + elem.text + "is not Displayed"

    # Verify Menu Buttons using smart-assertions
    @staticmethod
    @allure.step('soft verification (assert) of elements using smart-assertions')
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    # Verify Menu Buttons using My Implementation
    @staticmethod
    @allure.step('soft verification (assert) of elements using my implementation')
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].get_attribute('data-qa'))
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print("Soft Displayed Failed, Element which have failed: " + str(failed_elem))
            raise AssertionError("Soft Displayed Failed")

    # Verify Second Menu Buttons using smart-assertions
    @staticmethod
    @allure.step('soft verification (assert) of social media elements using smart-assertions')
    def soft_assert_for_second_menu(source_names, social_names):
        for i in range(len(source_names)):
            soft_assert(source_names[i] == social_names[i])
        verify_expectations()



