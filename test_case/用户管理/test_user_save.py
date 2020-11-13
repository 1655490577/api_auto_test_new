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
        pass

    def test_user_save_fail(self):
        pass
