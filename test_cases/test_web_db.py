import allure
import pytest
from workflows.db_flows import DBFlows
from workflows.web_flows.web_saucedemo_flows import WebSaucedemoFlows


@pytest.mark.usefixtures('init_web_saucedemo')
@pytest.mark.usefixtures('init_db_connection')
class Test_Wed_DB:
    @allure.title('Test01: Login to saucedemo via DB')
    @allure.description('This test verify login using elements taken from database')
    def test_verify_login_db(self):
        DBFlows.login_saucedemo_via_db()
        WebSaucedemoFlows.verify_saucedemo_title('Products')
