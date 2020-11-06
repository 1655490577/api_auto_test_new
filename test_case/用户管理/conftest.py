from API.api_get_data import getter
from common.logger import logger
import pytest

token, userId, cookies = getter.get_login_token_cookies('admin', 'admin')


@pytest.fixture()
def add_organization():
    """
    添加测试部门数据
    :return:
    """
    try:
        rsp_tree = getter.organization_findOrganizationTree(cookies=cookies, code='01', token=token, userid=userId)
        company_id = rsp_tree.json()['data']['list'][0]['id']
        getter.organization_save(cookies=cookies, label='测试部门', pid=company_id, type='2', token=token, userid=userId)
        yield
        rsp_bm = getter.organization_findDivision(cookies=cookies, token=token, userid=userId)
        for i in rsp_bm.json()['data']['list']:
            if i['label'] == '测试部门':
                branch_id = i['id']
                getter.organization_delete(cookies=cookies, id=branch_id, token=token, userid=userId)
    except Exception as e:
        logger.error(f"添加组织前置执行失败，错误为{e}")


@pytest.fixture()
def add_project():
    """
    添加测试项目数据
    :return:
    """
    try:
        branch_id = ''
        rsp_bm = getter.organization_findDivision(cookies=cookies, token=token, userid=userId)
        for i in rsp_bm.json()['data']['list']:
            if i['label'] == '测试部门':
                branch_id = i['id']
        rsp_add = getter.project_add(cookies=cookies, name='测试项目测试项目', token=token, userid=userId, orgId=branch_id)
        yield
        getter.project_batchDelete(cookies=cookies, id=rsp_add.json()['data'], token=token, userid=userId)
    except Exception as e:
        logger.error(f"添加项目前置执行失败，错误为{e}")


@pytest.fixture()
def add_station():
    """
    添加测试岗位数据
    :return:
    """
    try:
        rsp_data = getter.get_allPerms(cookies=cookies, pageNum=1, pageSize=100, token=token, userid=userId)
        rsp_add = getter.station_save(cookies=cookies, name='测试添加岗位', perms=getter.get_dict_allIds(rsp_data.json()),
                                      token=token, userid=userId)
        logger.info(f"添加结果为{rsp_add.json()}")
        yield
        rsp_station = getter.user_findJob(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)
        station_id = []
        for i in rsp_station.json()['data']['list']:
            if i['name'] == '测试添加岗位':
                station_id.append(i['id'])
        getter.station_delete(cookies=cookies, id=station_id, token=token, userid=userId)
    except Exception as e:
        logger.error(f"添加项目前置执行失败，错误为{e}")


@pytest.fixture()
def add_user():
    """
    添加测试用户信息
    :return:
    """
    try:
        rsp_station = getter.user_findJob(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)
        station_id = []
        for i in rsp_station.json()['data']['list']:
            if i['name'] == '测试添加岗位':
                station_id.append(i['id'])
                break
        rsp_branch = getter.user_findDivision(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)
        branch_id = ''
        for i in rsp_branch.json()['data']['list']:
            if i['label'] == '测试部门':
                branch_id = i['id']
                break
        rsp_project = getter.user_findProject(cookies=cookies, divIds=[f"{branch_id}"], pageNum=1,
                                              pageSize=1000, token=token, userid=userId)
        project_id = ''
        for i in rsp_project.json()['data']['list']:
            if i['label'] == '测试项目测试项目':
                project_id = i['id']
                break
        getter.user_save(cookies=cookies, divisionId=branch_id, jobId=station_id[0], name='测试账号111', password='123',
                         phone='13100000002', status=1, token=token, userid=userId, projectIds=[project_id])
        yield
        rsp_list = getter.user_list(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)
        for i in rsp_list.json()['data']['list']:
            if i['name'] == '测试账号111':
                delete_userId = i['id']
                getter.user_delete(cookies=cookies, id=[delete_userId], token=token, userid=userId)
    except Exception as e:
        logger.error(f"添加项目前置执行失败，错误为{e}")
