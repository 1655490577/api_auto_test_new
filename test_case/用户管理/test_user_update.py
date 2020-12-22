from API.api_get_data import getter
import pytest
import allure
import jsonpath


class TestUserUpdate(object):
    """
    修改用户信息接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '修改用户信息成功'))
    def test_user_update_success(self, request_parameters, expected_response):
        pass

    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '修改用户信息失败'))
    def test_user_update_fail(self, request_parameters, expected_response):
        pass
