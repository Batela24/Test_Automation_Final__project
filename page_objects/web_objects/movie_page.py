from selenium.webdriver.common.by import By

movie_title = (By.XPATH, "//h1[@class='title']")


class MoviePage:

    def __init__(self, driver):
        self.driver = driver

    def get_movie_title(self):
        return self.driver.find_element(movie_title[0], movie_title[1])

