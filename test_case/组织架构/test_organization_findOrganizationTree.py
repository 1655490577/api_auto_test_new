from API.api_get_data import getter
from common.logger import logger
import pytest
import allure


class TestOrganizationFindOrganizationTree(object):
    """
    组织架构-树查询接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '组织架构', '查询树结构成功'))
    def test_organization_findOrganizationTree_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
            logger.info(f"当前获取到的token：{token},userId：{userId}")

        with allure.step("step2: 步骤2 ==>> 请求获取组织架构树信息"):
            rsp_tree = getter.organization_findOrganizationTree(cookies=cookies, code=request_parameters['code'],
                                                                label=request_parameters['label'],
                                                                token=token, userid=userId)
            assert rsp_tree.status_code == 200
            assert rsp_tree.json()['data'] is not None
            assert rsp_tree.json()['message'] == expected_response['message']
            assert rsp_tree.json()['status'] == expected_response['status']

    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '组织架构', '查询失败'))
    def test_organization_findOrganizationTree_fail(self, request_parameters, expected_response):
        pass
