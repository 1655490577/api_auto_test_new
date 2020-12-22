from API.api_get_data import getter
import pytest
import allure
import jsonpath


class TestUserSave(object):
    """
    用户管理-新增接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '新增用户成功'))
    def test_user_save_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'], mobileType=2)
        with allure.step("step2: 步骤2 ==>> 获取所有部门id列表"):
            rsp_data1 = getter.user_findDivision(cookies=cookies, mobileType=2, pageNum=1, pageSize=10000, token=token, userid=userId)
            branch_id = jsonpath.jsonpath(rsp_data1.json(), '$..id')

        with allure.step("step3: 步骤3 ==>> 根据部门id获取部门下所有项目id"):
            rsp_data2 = getter.user_findProject(cookies=cookies, divIds=branch_id[0], mobileType=2, pageNum=1, pageSize=10000,
                                                token=token, userid=userId)
            project_ids = jsonpath.jsonpath(rsp_data2.json(), '$..id')

        with allure.step("step4: 步骤4 ==>> 获取岗位id"):
            rsp_data3 = getter.user_findJob(cookies=cookies, mobileType=2, pageNum=1, pageSize=10000, token=token, userid=userId)
            jobId = rsp_data3.json()['data']['list'][0]['id']

        with allure.step("step5: 步骤5 ==>> 新增用户"):
            rsp_branch = getter.user_save(cookies=cookies, divisionId=branch_id[0], jobId=jobId, name='测试用户001',
                                          password='123', phone='13200000001', projectIds=project_ids, status=1,
                                          token=token, userid=userId, mobileType=2)

        assert rsp_branch.status_code == 200
        assert rsp_branch.json()['data'] is None
        assert rsp_branch.json()['message'] == expected_response['message']
        assert rsp_branch.json()['status'] == expected_response['status']

    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '新增用户失败'))
    def test_user_save_fail(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'], mobileType=2)
        with allure.step("step2: 步骤2 ==>> 获取所有部门id列表"):
            if request_parameters['addInfo'] == '事业部未传':
                branch_id = []
            else:
                rsp_data1 = getter.user_findDivision(cookies=cookies, mobileType=2, pageNum=1, pageSize=10000, token=token,
                                                     userid=userId)
                branch_id = jsonpath.jsonpath(rsp_data1.json(), '$..id')

        with allure.step("step3: 步骤3 ==>> 根据部门id获取部门下所有项目id"):
            if request_parameters['addInfo'] == '项目权限未传':
                project_ids = []
            elif request_parameters['addInfo'] == '事业部与所选项目不符合':
                rsp_data2 = getter.user_findProject(cookies=cookies, divIds=branch_id[1], mobileType=2, pageNum=1,
                                                    pageSize=10000, token=token, userid=userId)
                project_ids = jsonpath.jsonpath(rsp_data2.json(), '$..id')
            else:
                rsp_data2 = getter.user_findProject(cookies=cookies, divIds=branch_id[0], mobileType=2, pageNum=1,
                                                    pageSize=10000, token=token, userid=userId)
                project_ids = jsonpath.jsonpath(rsp_data2.json(), '$..id')

        with allure.step("step4: 步骤4 ==>> 获取岗位id"):
            if request_parameters['addInfo'] == '岗位id系统中不存在':
                jobId = '123123123123432'
            elif request_parameters['addInfo'] == '岗位未传':
                jobId = ''
            else:
                rsp_data3 = getter.user_findJob(cookies=cookies, mobileType=2, pageNum=1, pageSize=10000, token=token,
                                                userid=userId)
                jobId = rsp_data3.json()['data']['list'][0]['id']

        with allure.step("step5: 步骤5 ==>> 新增用户"):
            if request_parameters['addInfo'] == '用户名未传':
                rsp_branch = getter.user_save(cookies=cookies, divisionId=branch_id[0], jobId=jobId, name='',
                                              password='123', phone='13200000001', projectIds=project_ids, status=1,
                                              token=token, userid=userId, mobileType=2)
            elif request_parameters['addInfo'] == '手机号未传':
                rsp_branch = getter.user_save(cookies=cookies, divisionId=branch_id[0], jobId=jobId, name='测试用户001',
                                              password='123', phone='', projectIds=project_ids, status=1,
                                              token=token, userid=userId, mobileType=2)
            elif request_parameters['addInfo'] == '手机号格式不是手机号':
                rsp_branch = getter.user_save(cookies=cookies, divisionId=branch_id[0], jobId=jobId, name='测试用户001',
                                              password='123', phone='19864800001', projectIds=project_ids, status=1,
                                              token=token, userid=userId, mobileType=2)
            elif request_parameters['addInfo'] == '手机号重复':
                rsp_branch = getter.user_save(cookies=cookies, divisionId=branch_id[0], jobId=jobId, name='测试用户001',
                                              password='123', phone='13168775547', projectIds=project_ids, status=1,
                                              token=token, userid=userId, mobileType=2)
            elif request_parameters['addInfo'] == '密码未传':
                rsp_branch = getter.user_save(cookies=cookies, divisionId=branch_id[0], jobId=jobId, name='测试用户001',
                                              password='', phone='13200000001', projectIds=project_ids, status=1,
                                              token=token, userid=userId, mobileType=2)
            elif request_parameters['addInfo'] == '在职状态未传':
                rsp_branch = getter.user_save(cookies=cookies, divisionId=branch_id[0], jobId=jobId, name='测试用户001',
                                              password='123', phone='13200000001', projectIds=project_ids, status='',
                                              token=token, userid=userId, mobileType=2)
            else:
                rsp_branch = getter.user_save(cookies=cookies, divisionId=branch_id[0], jobId=jobId, name='测试用户001',
                                              password='123', phone='13200000001', projectIds=project_ids, status=1,
                                              token=token, userid=userId, mobileType=2)

        assert rsp_branch.status_code == 200
        assert rsp_branch.json()['data'] is None
        assert rsp_branch.json()['message'] == expected_response['message']
        assert rsp_branch.json()['status'] == expected_response['status']
