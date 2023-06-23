from selenium.webdriver.common.by import By

showtimes = (By.CSS_SELECTOR, "[data-qa='masthead:tickets-showtimes-link']")
news = (By.CSS_SELECTOR, "[data-qa='masthead:news-link']")
movie_trivia = (By.CSS_SELECTOR, "[data-qa='masthead:trivia-link']")
tv_shows = (By.CSS_SELECTOR, "[data-qa='masthead:tv-link']")
movies = (By.CSS_SELECTOR, "[data-qa='masthead:movies-dvds-link']")
search_input = (By.CSS_SELECTOR, "[data-qa='search-input']")
search_button = (By.CLASS_NAME, "search-submit")


class UpperMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def get_showtimes(self):
        return self.driver.find_element(showtimes[0], showtimes[1])

    def get_news(self):
        return self.driver.find_element(news[0], news[1])

    def get_movie_trivia(self):
        return self.driver.find_element(movie_trivia[0], movie_trivia[1])

    def get_tv_shows(self):
        return self.driver.find_element(tv_shows[0], tv_shows[1])

    def get_movies(self):
        return self.driver.find_element(movies[0], movies[1])

    def get_search_input(self):
        return self.driver.find_element(search_input[0], search_input[1])

    def get_search_button(self):
        return self.driver.find_element(search_button[0], search_button[1])

