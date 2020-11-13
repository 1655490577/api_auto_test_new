from API.api_get_data import getter
import pytest
import allure


@pytest.mark.skip(reason='目前该接口未使用')
class TestUserListByIds(object):
    """
    用户登录_项目信息listByIds(不知道干嘛用的)
    """
    def test_user_listByIds_success(self):
        pass

    def test_user_listByIds_fail(self):
        pass
