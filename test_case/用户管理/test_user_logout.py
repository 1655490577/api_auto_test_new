from API.api_get_data import getter
from common.logger import logger
import pytest
import allure


class TestLogout(object):
    """
    退出登录接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '注销成功'))
    def test_logout(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
            logger.info(f"当前获取到的token：{token},userId：{userId}")
        with allure.step("step2: 步骤2 ==>> 使用当前获取到的信息退出登录"):
            rsp_logout = getter.user_logout(cookies=cookies, token=token, userid=userId)
            print(rsp_logout.json())
            logger.info(f"本次测试登录账号为{request_parameters['phone']}========>接口返回状态码为{rsp_logout.status_code}，"
                        f"message为{rsp_logout.json()['message']}，status为{rsp_logout.json()['status']}")

        assert rsp_logout.status_code == 200
        assert rsp_logout.json()['data'] is None
        assert rsp_logout.json()['message'] == expected_response['message']
        assert rsp_logout.json()['status'] == expected_response['status']


if __name__ == '__main__':
    pytest.main(['-s', 'test_user_logout.py'])
