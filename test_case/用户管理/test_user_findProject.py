from API.api_get_data import getter
import pytest
import allure


@pytest.mark.usefixtures('add_station')
@pytest.mark.usefixtures('add_organization')
class TestUserFindProject(object):
    """
    查询所有项目
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '查询项目成功'))
    def test_user_findProject_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'], mobileType=2)
        with allure.step("step2: 步骤2 ==>> 获取事业部id"):
            rsp_ids = getter.user_findDivision(cookies=cookies, mobileType=2, pageNum=1, pageSize=1000, token=token, userid=userId)
            branch_id = rsp_ids.json()['data']['list'][0]['id']

        with allure.step("step3: 步骤3 ==>> 查询所有事业部下项目"):
            rsp_data = getter.user_findProject(cookies=cookies, divIds=[branch_id], pageNum=1,
                                               pageSize=1000, mobileType=2, token=token, userid=userId)

        assert rsp_data.status_code == 200
        assert rsp_data.json()['data'] is not None
        assert rsp_data.json()['message'] == expected_response['message']
        assert rsp_data.json()['status'] == expected_response['status']

    def test_user_findProject_fail(self):
        pass
