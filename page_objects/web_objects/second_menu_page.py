from selenium.webdriver.common.by import By

youtube = (By.ID, "header-youtube-social-link")
pinterest = (By.ID, "header-pinterest-social-link")
instagram = (By.ID, "header-instagram-social-link")
twitter = (By.ID, "header-twitter-social-link")
facebook = (By.ID, "header-facebook-social-link")


class SecondMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def get_youtube_social_link(self):
        return self.driver.find_element(youtube[0], youtube[1])

    def get_pinterest_social_link(self):
        return self.driver.find_element(pinterest[0], pinterest[1])

    def get_instagram_social_link(self):
        return self.driver.find_element(instagram[0], instagram[1])

    def get_twitter_social_link(self):
        return self.driver.find_element(twitter[0], twitter[1])

    def get_facebook_social_link(self):
        return self.driver.find_element(facebook[0], facebook[1])


