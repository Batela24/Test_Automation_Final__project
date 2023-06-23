import pytest
import test_cases.conftest as conf
from page_objects.desktop_objects.standard_page import StandardPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_objects.calculator_page import CalculatorPage
from page_objects.mobile_objects.saved_page import SavedPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects.movie_page import MoviePage
from page_objects.web_objects.movies_page import MoviesPage
from page_objects.web_objects.results_page import ResultsPage
from page_objects.web_objects.upper_menu_page import UpperMenuPage
from page_objects.web_objects.second_menu_page import SecondMenuPage
from utilities.common_ops import get_data

# Web Objects
web_login = None
web_main = None
web_upper_menu = None
web_results_page = None
web_second_menu = None
web_movies_page = None
web_movie_page = None

# Mobile Objects
mobile_calculator = None
mobile_saved = None

# Electron Objects
electron_task = None

# Desktop Objects
standard_calc = None


class ManagePages:

    @staticmethod
    def init_web_saucedemo_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)

    @staticmethod
    def init_web_rottentomatoes_pages():
        globals()['web_upper_menu'] = UpperMenuPage(conf.driver)
        globals()['web_results_page'] = ResultsPage(conf.driver)
        globals()['web_second_menu'] = SecondMenuPage(conf.driver)
        globals()['web_movies_page'] = MoviesPage(conf.driver)
        globals()['web_movie_page'] = MoviePage(conf.driver)

    @staticmethod
    def init_mobile_pages():
        globals()['mobile_calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_saved'] = SavedPage(conf.driver)

    @staticmethod
    def init_electron_pages():
        globals()['electron_task'] = TaskPage(conf.driver)

    @staticmethod
    def init_desktop_pages():
        globals()['standard_calc'] = StandardPage(conf.driver)
