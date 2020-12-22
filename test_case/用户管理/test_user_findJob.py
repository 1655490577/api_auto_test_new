from API.api_get_data import getter
import pytest
import allure
import re


@pytest.mark.usefixtures('add_station')
class TestUserFindJob(object):
    """
    查询所有岗位
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '查询岗位成功'))
    def test_user_findJob_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'], mobileType=2,)
        with allure.step("step2: 步骤2 ==>> 查询所有岗位"):
            rsp_data = getter.user_findJob(cookies=cookies, mobileType=2, pageNum=1, pageSize=1000, token=token, userid=userId)

            assert rsp_data.status_code == 200
            assert rsp_data.json()['data'] is not None
            assert rsp_data.json()['message'] == expected_response['message']
            assert rsp_data.json()['status'] == expected_response['status']
            for i in range(3):
                assert re.findall(f'测试岗位{i+1}', rsp_data.json()) is not None

    def test_user_findJob_fail(self):
        pass
