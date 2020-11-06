from API.api_get_data import getter
from common.logger import logger
import pytest
import allure


class TestOrganizationSave(object):
    """
    组织架构新增接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '组织架构', '公司新增'))
    def test_organization_save_equative(self, request_parameters, expected_response):
        """
        新增平级组织
        :param request_parameters: 请求参数列表
        :param expected_response:预期响应结果列表
        :return:
        """
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
            logger.info(f"当前获取到的token：{token},userId：{userId}")

        with allure.step("step2: 步骤2 ==>> 获取公司节点id"):
            rsp_tree = getter.organization_findOrganizationTree(cookies=cookies, code='01', token=token, userid=userId)
            company_id = rsp_tree.json()['data']['list'][0]['id']

        with allure.step("step3: 步骤3 ==>> 添加组织架构"):
            rsp_add = getter.organization_save(cookies=cookies, label=request_parameters['label'], pid=company_id,
                                               type=request_parameters['type'], token=token, userid=userId)
            logger.info(f"添加返回结果为：{rsp_add.json()}")

        with allure.step("step4: 步骤4 ==>> 查询当前组织架构，验证是否添加成功"):
            rsp_select = getter.organization_findDivision(cookies=cookies, token=token, userid=userId)
            logger.info(f"查询返回结果为：{rsp_select.json()}")

        assert rsp_add.status_code == 200
        assert rsp_add.json()['message'] == expected_response['message']
        assert rsp_add.json()['status'] == expected_response['status']
        assert request_parameters['label'] == rsp_select.json()['data']['list'][0]['label']

    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '组织架构', '部门新增'))
    def test_organization_save_subset(self, request_parameters, expected_response):
        """
        新增下级组织
        :param request_parameters:请求参数列表
        :param expected_response:预期响应结果列表
        :return:
        """
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
            logger.info(f"当前获取到的token：{token},userId：{userId}")

        with allure.step("step2: 步骤2 ==>> 获取部门节点id"):
            rsp_tree = getter.organization_findOrganizationTree(cookies=cookies, code='01', token=token, userid=userId)
            branch_id = rsp_tree.json()['data']['list'][0]['children'][0]['id']

        with allure.step("step3: 步骤3 ==>> 添加组织架构"):
            rsp_add = getter.organization_save(cookies=cookies, label=request_parameters['label'], pid=branch_id,
                                               type=request_parameters['type'], token=token, userid=userId)
            logger.info(f"添加返回结果为：{rsp_add.json()}")

        with allure.step("step4: 步骤4 ==>> 查询当前组织架构，验证是否添加成功"):
            rsp_select = getter.organization_findDivision(cookies=cookies, token=token, userid=userId)
            logger.info(f"查询返回结果为：{rsp_select.json()}")

        assert rsp_add.status_code == 200
        assert rsp_add.json()['message'] == expected_response['message']
        assert rsp_add.json()['status'] == expected_response['status']
        assert request_parameters['label'] == rsp_select.json()['data']['list'][0]['label']


if __name__ == '__main__':
    pytest.main(['-s', 'test_organization.py'])
