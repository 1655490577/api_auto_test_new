from API.api_get_data import getter
from common.logger import logger
from collections import Iterable
import pytest
import allure


class TestOrganizationDelete(object):
    """
    组织架构删除接口测试
    """
    @pytest.mark.usefixtures('addOrganization')
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '组织架构', '删除成功'))
    def test_organization_delete_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
            logger.info(f"当前获取到的token：{token},userId：{userId}")

        with allure.step("step2: 步骤2 ==>> 获取需要删除的部门id"):
            rsp_tree = getter.organization_findOrganizationTree(cookies=cookies, code='01', token=token, userid=userId)
            branch_id = rsp_tree.json()['data']['list'][0]['children'][0]['id']
            logger.info(f"本次删除的部门名称为{rsp_tree.json()['data']['list'][0]['children'][0]['label']},"
                        f"该部门id为：{branch_id}")

        with allure.step("step3: 步骤3 ==>> 删除指定部门"):
            rsp_delete = getter.organization_delete(cookies=cookies, id=branch_id, token=token, userid=userId)
            logger.info(f"本次删除结果为{rsp_delete.json()['message']}")

        with allure.step("step4: 步骤4 ==>> 查询所有部门，验证删除部门是否成功"):
            rsp_select = getter.organization_findDivision(cookies=cookies, token=token, userid=userId)
            branchIdList = []
            for i in rsp_select.json()['data']['list']:
                branchIdList.append(i['id'])
            logger.info(f"当前所有事业部id为：{branchIdList}")

        assert rsp_delete.status_code == 200
        assert rsp_delete.json()['data'] is None
        assert rsp_delete.json()['message'] == expected_response['message']
        assert rsp_delete.json()['status'] == expected_response['status']
        assert branch_id not in branchIdList

    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '组织架构', '删除失败'))
    def test_organization_delete_fail(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
            logger.info(f"当前获取到的token：{token},userId：{userId}")

        with allure.step("step2: 步骤2 ==>> 获取需要删除的公司id"):
            rsp_tree = getter.organization_findOrganizationTree(cookies=cookies, code='01', token=token, userid=userId)
            if request_parameters['deleteInfo'] == '公司':
                company_id = rsp_tree.json()['data']['list'][0]['id']
                logger.info(f"本次删除的公司名称为{rsp_tree.json()['data']['list'][0]['label']},"
                            f"该公司id为：{company_id}")
            elif request_parameters['deleteInfo'] == '项目':
                project_id = rsp_tree.json()['data']['list'][0]['children'][0]['id']
                logger.info(f"本次删除项目名称为{rsp_tree.json()['data']['list'][0]['children'][0]['label']},"
                            f"该项目id为：{project_id}")
            elif request_parameters['deleteInfo'] == '有项目的部门':
                branchList = []
                for i in rsp_tree.json()['data']['list'][0]['children']:
                    if isinstance(i['children'], Iterable):
                        branchList.append(i['id'])
                logger.info(f"所有有项目的部门id为：{branchList}")

        with allure.step("step3: 步骤3 ==>> 删除指定部门"):
            if request_parameters['deleteInfo'] == '公司':
                rsp_delete = getter.organization_delete(cookies=cookies, id=company_id, token=token, userid=userId)
            elif request_parameters['deleteInfo'] == '项目':
                rsp_delete = getter.organization_delete(cookies=cookies, id=project_id, token=token, userid=userId)
            elif request_parameters['deleteInfo'] == '有项目的部门':
                rsp_delete = getter.organization_delete(cookies=cookies, id=branchList[0], token=token, userid=userId)
            logger.info(f"本次删除结果为{rsp_delete.json()['message']}")

        assert rsp_delete.status_code == 200
        assert rsp_delete.json()['data'] is None
        assert rsp_delete.json()['message'] == expected_response['message']
        assert rsp_delete.json()['status'] == expected_response['status']


if __name__ == '__main__':
    pytest.main(['-s', 'test_organization_delete.py'])
