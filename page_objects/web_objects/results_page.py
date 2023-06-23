from selenium.webdriver.common.by import By

movies_result_number = (By.CSS_SELECTOR, "[data-filter='movie']>span")


class ResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def get_movies_result(self):
        return self.driver.find_element(movies_result_number[0], movies_result_number[1])

