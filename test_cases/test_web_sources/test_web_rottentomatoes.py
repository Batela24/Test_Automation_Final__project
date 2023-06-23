import pytest
import allure
from utilities.common_ops import get_data
from workflows.web_flows import web_rottentomatoes_flows
from workflows.web_flows.web_rottentomatoes_flows import WebRottentomatoesFlows
from extensions.ui_actions import UiActions


@pytest.mark.usefixtures('init_web_rottentomatoes')
class Test_Web_Rottentomatoes:

    @allure.title('Test01: Verify Upper Menu Buttons')
    @allure.description('This test verifies upper menu buttons are displayed')
    def test_verify_upper_menu(self):
        # smart-assertions:
        WebRottentomatoesFlows.verify_menu_buttons_flow_smart_assertions()
        # My Implementation:
        # WebFlows.verify_menu_buttons_flow()

    @allure.title('Test02: Search Movies')
    @allure.description('This test verifies for each searched movie, the right movie number of results')
    @pytest.mark.parametrize('search_value,expected_movies', web_rottentomatoes_flows.csv_data)
    def test_csv(self, search_value, expected_movies):
        WebRottentomatoesFlows.search_movie(search_value)
        WebRottentomatoesFlows.verify_number_of_movies_results(get_data('ResultTitle'), int(expected_movies))

    @allure.title('Test03: Verify Second Menu Buttons')
    @allure.description('This test verifies second menu buttons are moving the user to the right source url')
    def test_verify_second_menu_functionality(self):
        WebRottentomatoesFlows.verify_second_menu_social_media_links()

    @allure.title('Test04: Verify Random movie name between pages')
    @allure.description('This test verifies that random movie has the same name between list and details pages')
    def test_verify_random_movies_titles_between_pages(self):
        WebRottentomatoesFlows.open_movies_page()
        WebRottentomatoesFlows.verify_movies_titles_between_pages()

    @allure.title('Test05: Visual Logo Testing')
    @allure.description('This test verifies visually of the site logo')
    @pytest.mark.skipif(UiActions.lower_letters(get_data('Execute_Applitools')) == 'no', reason='run this test only on'
                                                                                                ' selenium 3.141.0 & '
                                                                                                'appium 1.3.0')
    def test_verify_logo_visibility(self):
        WebRottentomatoesFlows.logo_visual_testing()





