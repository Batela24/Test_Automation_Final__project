import allure
import page_objects.web_objects.results_page as result_page
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For, read_csv, get_data, get_random_place
from test_cases import conftest as conf


class WebRottentomatoesFlows:

    # Verify Menu Buttons Using smart-assertions
    @staticmethod
    @allure.step('Verify displayed menu buttons flow using smart_assertions')
    def verify_menu_buttons_flow_smart_assertions():
        elems = [page.web_upper_menu.get_showtimes(),
                 page.web_upper_menu.get_news(),
                 page.web_upper_menu.get_movie_trivia(),
                 page.web_upper_menu.get_tv_shows(),
                 page.web_upper_menu.get_movies(),
                 page.web_upper_menu.get_search_input()]
        Verifications.soft_assert(elems)

    # Verify Menu Buttons using My Implementation
    @staticmethod
    @allure.step('Verify displayed menu buttons flow using my implementation')
    def verify_menu_buttons_flow():
        elems = [page.web_upper_menu.get_showtimes(),
                 page.web_upper_menu.get_news(),
                 page.web_upper_menu.get_movie_trivia(),
                 page.web_upper_menu.get_tv_shows(),
                 page.web_upper_menu.get_movies(),
                 page.web_upper_menu.get_search_input()]
        Verifications.soft_displayed(elems)

    # Search Movie name and get the number of movies that contain this name (CSV data)
    @staticmethod
    @allure.step('Search movie from all the site flow')
    def search_movie(search_value):
        UiActions.clear(page.web_upper_menu.get_search_input())
        UiActions.update_text(page.web_upper_menu.get_search_input(), search_value)
        # select enter:
        UiActions.do_enter()
        # UiActions.update_text(page.web_upper_menu.get_search_input(), Keys.ENTER)
        # UiActions.click(page.web_upper_menu.get_search_button())

    @staticmethod
    @allure.step('Verify number of results for movie in movies category flow')
    def verify_number_of_movies_results(movie_name, number):
        # result_title = The 'Movies' option
        # wait for the total result be displayed on the results page
        wait(For.ELEMENT_DISPLAYED, result_page.movies_result_number)
        # compare between the site returned number and the csv value
        Verifications.verify_equals(get_movies_result_number_for_movie(movie_name), int(number))

    @staticmethod
    @allure.step('Verify social media options moving to the right url address')
    def verify_second_menu_social_media_links():
        social_media_names = ['youtube', 'pinterest', 'instagram', 'twitter', 'facebook']
        social_elems = [page.web_second_menu.get_youtube_social_link(),
                        page.web_second_menu.get_pinterest_social_link(),
                        page.web_second_menu.get_instagram_social_link(),
                        page.web_second_menu.get_twitter_social_link(),
                        page.web_second_menu.get_facebook_social_link()]
        source_names = []
        for i in range(len(social_elems)):
            social_elems[i].click()
            source_url = UiActions.move_to_new_tab_and_get_source_url()
            if social_media_names[3] in source_url:
                part_of_url = source_url.split('//')
                source_text_list = part_of_url[1].split('.')
                source_names.append(source_text_list[0])
            else:
                source_text_list = source_url.split('.')
                source_names.append(source_text_list[1])
        Verifications.soft_assert_for_second_menu(source_names, social_media_names)

    @staticmethod
    @allure.step('Open the movies page')
    def open_movies_page():
        UiActions.click(page.web_upper_menu.get_movies())  # Navigate to Movies

    @staticmethod
    @allure.step('Verify matching of random movie title between pages')
    def verify_movies_titles_between_pages():
        all_movies_titles = page.web_movies_page.get_all_movies_titles()
        random_place = get_random_place(len(all_movies_titles))
        selected_movie_title = all_movies_titles[random_place]
        selected_movie_title_text = UiActions.lower_letters(UiActions.text(selected_movie_title))
        # moving to the random movie page
        UiActions.click(selected_movie_title)
        expected_movie_title_text = UiActions.lower_letters(UiActions.text(page.web_movie_page.get_movie_title()))
        Verifications.verify_equals(selected_movie_title_text, expected_movie_title_text)

    @staticmethod
    @allure.step('Verify logo displaying')
    def logo_visual_testing():
        conf.eyes.open(conf.driver, 'Rottentomatoes', 'Rottentomatoes Testing Logo')
        conf.eyes.check_window('Home Page Logo')


# function for returning the result number of movies, for using in verify_number_of_movies_results method
def get_movies_result_number_for_movie(option):
    movies_amount = UiActions.text(page.web_results_page.get_movies_result())
    result_max_letter = len(movies_amount) - 1
    start_point = len(option) + 2
    result_number_only = movies_amount[start_point:result_max_letter]
    return int(result_number_only)


# variable for bringing the data from the csv file
csv_data = read_csv(get_data('CSV_Location'))

# Another option for a specific amount of data:
# test_data = [
#     (csv_data[0][0], csv_data[0][1]),
#     (csv_data[1][0], csv_data[1][1]),
#     (csv_data[2][0], csv_data[2][1]),
#     (csv_data[3][0], csv_data[3][1]),
#     (csv_data[4][0], csv_data[4][1]),
#     (csv_data[5][0], csv_data[5][1]),
# ]
