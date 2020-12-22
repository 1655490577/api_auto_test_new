from API.api_get_data import getter
import pytest


@pytest.fixture(scope='function')
def addOrganization():
    """
    新增测试使用组织架构数据
    :return:
    """
    token, userId, cookies = getter.get_login_token_cookies('admin', 'admin')
    rsp_tree = getter.organization_findOrganizationTree(cookies=cookies, mobileType=2, code='01', token=token, userid=userId)
    branch_id = rsp_tree.json()['data']['list'][0]['children'][0]['id']
    getter.organization_save(cookies=cookies, label='test事业部', pid=branch_id,
                             type=1,  mobileType=2, token=token, userid=userId)
    yield
    rsp_tree = getter.organization_findOrganizationTree(cookies=cookies, mobileType=2, code='01', token=token, userid=userId)
    delete_branch_id = rsp_tree.json()['data']['list'][0]['children'][0]['id']
    getter.organization_delete(cookies=cookies, mobileType=2, id=delete_branch_id, token=token, userid=userId)
