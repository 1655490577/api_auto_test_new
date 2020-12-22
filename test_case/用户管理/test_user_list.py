from API.api_get_data import getter
import pytest
import allure
import re


@pytest.mark.usefixtures('add_user')
@pytest.mark.usefixtures('add_station')
@pytest.mark.usefixtures('add_project')
@pytest.mark.usefixtures('add_organization')
class TestUserList(object):
    """
    用户列表接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '查询用户列表成功'))
    def test_user_list_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'], mobileType=2)
        with allure.step("step2: 步骤2 ==>> 查询用户列表"):
            rsp_list = getter.user_list(cookies=cookies, mobileType=2, pageNum=1, pageSize=1000, token=token, userid=userId)

        assert rsp_list.status_code == 200
        assert rsp_list.json()['data'] is not None
        assert rsp_list.json()['message'] == expected_response['message']
        assert rsp_list.json()['status'] == expected_response['status']
        for i in range(3):
            assert re.findall(f'测试添加账号{i+1}', rsp_list.json()) is not None

    def test_user_list_fail(self):
        pass
