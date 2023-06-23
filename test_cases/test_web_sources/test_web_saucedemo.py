import pytest
import allure
from utilities.common_ops import get_data
from workflows.web_flows.web_saucedemo_flows import WebSaucedemoFlows


@pytest.mark.usefixtures('init_web_saucedemo')
class Test_Web_Saucedemo:

    @allure.title('Test01: Verify Login to Saucedemo')
    @allure.description('This test verifies a successful login to Saucedemo')
    def test_verify_login(self):
        WebSaucedemoFlows.login_flow(get_data('UserName'), get_data('Password'))
        WebSaucedemoFlows.verify_saucedemo_title('Products')


