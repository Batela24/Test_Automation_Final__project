import allure
from workflows.web_flows.web_saucedemo_flows import WebSaucedemoFlows
from extensions.db_actions import DBActions


class DBFlows:

    @staticmethod
    @allure.step('Login to Saucedemo via Database Flow')
    def login_saucedemo_via_db():
        columns = ['name', 'password']
        result = DBActions.get_query_result(columns, 'users', 'status', 'standard')
        WebSaucedemoFlows.login_flow(result[0][0], result[0][1])
