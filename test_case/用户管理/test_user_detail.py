from API.api_get_data import getter
from common.logger import logger
import pytest
import allure


@pytest.mark.usefixtures('add_user')
@pytest.mark.usefixtures('add_station')
@pytest.mark.usefixtures('add_project')
@pytest.mark.usefixtures('add_organization')
class TestUserDetail(object):
    """
    用户详情接口
    """
    @pytest.mark.parametrize(('request_parameters', 'expected_response'),
                             getter.load_excel('监理api接口自动化测试用例.xls', '用户管理', '获取用户详情成功'))
    def test_userDetail_success(self, request_parameters, expected_response):
        with allure.step("step1: 步骤1 ==>> 使用正确用户名密码登录系统获取对应token与userId"):
            token, userId, cookies = getter.get_login_token_cookies(request_parameters['phone'],
                                                                    request_parameters['password'])
        with allure.step("step2: 步骤2 ==>> 获取需要查询用户id"):
            select_info = []
            rsp_list = getter.user_list(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)
            for i, item in enumerate(rsp_list.json()['data']['list']):
                if item['name'] == '测试添加账号1':
                    select_info.append(item)
                    break
            select_id = select_info[0]['id']
            logger.info(f"select_info为{select_info},select_id为{select_id}")

        with allure.step("step3: 步骤3 ==>>查询用户详情"):
            rsp_detail = getter.user_detail(cookies=cookies, id=select_id, token=token, userid=userId)

        assert rsp_detail.status_code == 200
        assert rsp_detail.json()['data'] is not None
        assert rsp_detail.json()['message'] == expected_response['message']
        assert rsp_detail.json()['status'] == expected_response['status']
        assert select_info[0] == rsp_detail.json()['data']

    def test_userDetail_fail(self):
        pass
