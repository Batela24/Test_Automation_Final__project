from selenium.webdriver.common.by import By

movie_section = (By.CLASS_NAME, "js-tile-link ")
movie_title = (By.CSS_SELECTOR, "[data-qa='discovery-media-list-item-title']")


class MoviesPage:

    def __init__(self, driver):
        self.driver = driver

    def get_all_movies_sections(self):
        return self.driver.find_elements(movie_section[0], movie_section[1])

    def get_all_movies_titles(self):
        return self.driver.find_elements(movie_title[0], movie_title[1])


