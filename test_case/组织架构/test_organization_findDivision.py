from API.api_get_data import getter
from common.logger import logger
import pytest
import allure


class TestOrganizationFindDivision(object):
    """
    组织架构-查询所有事业部接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '组织架构', '查询事业部成功'))
    def test_organization_findDivision_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
            logger.info(f"当前获取到的token：{token},userId：{userId}")

        with allure.step("step2: 步骤2 ==>> 请求获取所有事业部信息"):
            rsp_branch = getter.organization_findDivision(cookies=cookies, mobileType=2, token=token, userid=userId)

        assert rsp_branch.status_code == 200
        assert rsp_branch.json()['data'] is not None
        assert rsp_branch.json()['message'] == expected_response['message']
        assert rsp_branch.json()['status'] == expected_response['status']

    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '组织架构', '查询事业部失败'))
    def test_organization_findDivision_fail(self, request_parameters, expected_response):
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'test_organization_findDivision.py'])
