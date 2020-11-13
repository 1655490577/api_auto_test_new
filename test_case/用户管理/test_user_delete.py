from API.api_get_data import getter
from common.logger import logger
import pytest
import allure
import re


@pytest.mark.usefixtures('add_user')
@pytest.mark.usefixtures('add_station')
@pytest.mark.usefixtures('add_project')
@pytest.mark.usefixtures('add_organization')
class TestUserDelete(object):
    """
    删除用户接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '删除用户成功'))
    def test_user_delete_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
            logger.info(f"当前获取到的token：{token},userId：{userId}")

        with allure.step("step2: 步骤2 ==>> 获取被删除用户id"):
            delete_id = []
            rsp_list1 = getter.user_list(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)
            for i, item in enumerate(rsp_list1.json()['data']['list']):
                if item['name'] == f'测试添加账号{i+1}':
                    if request_parameters['deleteInfo'] == '删除单个用户':
                        delete_id.append(item['id'])
                        break
                    elif request_parameters['deleteInfo'] == '批量删除用户':
                        delete_id.append(item['id'])
            logger.info(f"被删除用户id为{delete_id}")

        with allure.step("step3: 步骤3 ==>>删除用户"):
            rsp_delete = getter.user_delete(cookies=cookies, id=delete_id, userid=userId, token=token)
            logger.info(f"删除结果为{rsp_delete.json()['message']}")

        with allure.step("step4: 步骤4 ==>>查询所有用户列表"):
            rsp_list2 = getter.user_list(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)

        assert rsp_delete.status_code == 200
        assert rsp_delete.json()['data'] is None
        assert rsp_delete.json()['message'] == expected_response['message']
        assert rsp_delete.json()['status'] == expected_response['status']
        assert rsp_list2.json()['data'] is not None
        for i in delete_id:
            assert re.search(i, str(rsp_list2.json()['data'])) is None

    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '删除用户失败'))
    def test_user_delete_fail(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
            logger.info(f"当前获取到的token：{token},userId：{userId}")

        with allure.step("step2: 步骤2 ==>> 根据用例获取对应用户id/cookies"):
            rsp_list1 = getter.user_list(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)
            delete_id = []
            if request_parameters['deleteInfo'] == 'id不存在':
                delete_id = '123213123213'
            if request_parameters['deleteInfo'] == 'id为空':
                delete_id = ''
            if request_parameters['deleteInfo'] == '批量删除用户':
                for i, item in enumerate(rsp_list1.json()['data']['list']):
                    if item['name'] == f'测试添加账号{i + 1}':
                        delete_id.append(item['id'])
                delete_id.append('12312312343241')
            if request_parameters['deleteInfo'] == '未登录删除用户':
                for i, item in enumerate(rsp_list1.json()['data']['list']):
                    if item['name'] == f'测试添加账号{i+1}':
                        delete_id.append(item['id'])
                        break

        with allure.step("step3: 步骤3 ==>> 根据对应信息删除用户"):
            if request_parameters['deleteInfo'] == '未登录删除用户':
                rsp_delete = getter.user_delete(id=delete_id, token=token, userid=userId)
            else:
                rsp_delete = getter.user_list(cookies=cookies, id=delete_id, token=token, userid=userId)

            assert rsp_delete.status_code == 200
            assert rsp_delete.json()['data'] is None
            assert rsp_delete.json()['message'] == expected_response['message']
            assert rsp_delete.json()['status'] == expected_response['status']
