from API.api_get_data import getter
import pytest
import allure


class TestUserSave(object):
    """
    用户管理-新增接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '新增用户成功'))
    def test_user_save_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
        with allure.step("step2: 步骤2 ==>> 获取所有部门id列表"):
            branch_id = []
            rsp_data1 = getter.user_findDivision(cookies=cookies, pageNum=1, pageSize=10000, token=token, userid=userId)
            for i in rsp_data1.json()['data']['list']:
                branch_id.append(i['id'])

        with allure.step("step3: 步骤3 ==>> 根据部门id获取部门下所有项目id"):
            rsp_data2 = getter.user_findProject(cookies=cookies, id=branch_id[0], pageNum=1, pageSize=10000,
                                                token=token, userid=userId)
            project_ids = []
            for i in rsp_data2.json()['data']['list']:
                project_ids.append(i['id'])

        with allure.step("step4: 步骤4 ==>> 获取岗位id"):
            rsp_data3 = getter.user_findJob(cookies=cookies, pageNum=1, pageSize=10000, token=token, userid=userId)
            jobId = rsp_data3.json()['data']['list'][0]['id']

        with allure.step("step4: 步骤4 ==>> 新增用户"):
            rsp_branch = getter.user_save(cookies=cookies, divisionId=branch_id[0], jobId=jobId, name='测试用户001',
                                          password='123', phone='13200000001', projectIds=project_ids, status=1,
                                          token=token, userid=userId)

        assert rsp_branch.status_code == 200
        assert rsp_branch.json()['data'] is None
        assert rsp_branch.json()['message'] == expected_response['message']
        assert rsp_branch.json()['status'] == expected_response['status']

    def test_user_save_fail(self):
        pass
