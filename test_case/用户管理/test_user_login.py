from API.api_get_data import getter
from common.logger import logger
import pytest
import allure


class TestLogin(object):
    """
    登录接口测试
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '登录成功'))
    def test_login_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统"):
            rsp_login = getter.user_login(phone=request_parameters['phone'], password=request_parameters['password'],
                                          rememberMe=request_parameters['rememberMe'])
            logger.info(f"本次测试登录账号为{request_parameters['phone']}========>接口返回状态码为{rsp_login.status_code}，"
                        f"message为{rsp_login.json()['message']}，status为{rsp_login.json()['status']}")

        assert rsp_login.status_code == 200
        assert rsp_login.json()['data'] is not None
        assert rsp_login.json()['message'] == expected_response['message']
        assert rsp_login.json()['status'] == expected_response['status']

    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '登录失败'))
    def test_login_fail(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用错误用户名密码登录系统"):
            rsp_login = getter.user_login(phone=request_parameters['phone'], password=request_parameters['password'],
                                          rememberMe=request_parameters['rememberMe'])
            logger.info(f"本次测试登录账号为{request_parameters['phone']}========>接口返回状态码为{rsp_login.status_code}，"
                        f"message为{rsp_login.json()['message']}，status为{rsp_login.json()['status']}")

        assert rsp_login.status_code == 200
        assert rsp_login.json()['data'] is None
        assert rsp_login.json()['message'] in expected_response['message']
        assert rsp_login.json()['status'] == expected_response['status']


if __name__ == '__main__':
    pytest.main(['-s', 'test_user_login.py'])
