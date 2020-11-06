from API.api_get_data import getter
import pytest


@pytest.fixture()
def preposition_login():
    token, userId, cookies = getter.get_login_token_cookies('13100000001', '1')
    return [token, userId, cookies]


@pytest.fixture()
def addOrganization():
    token, userId, cookies = getter.get_login_token_cookies('admin', 'admin')
    parentId = getter.organization_findOrganizationTree(cookies=cookies, code='01', token=token,
                                                        userid=userId).json()['data']['list'][0]['id']

    getter.organization_save(cookies=cookies, label='测试部门1', pid=parentId, remarks='测试专用', token=token,
                             userid=userId, type=2)

