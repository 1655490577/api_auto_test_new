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
        for i in range(3):
            getter.organization_save(cookies=cookies, label=f'测试部门{i+1}', pid=company_id, type='2', token=token, userid=userId)
        yield
        rsp_bm = getter.organization_findDivision(cookies=cookies, token=token, userid=userId)
        for i, item in enumerate(rsp_bm.json()['data']['list']):
            if item['label'] == f'测试部门{i+1}':
                branch_id = item['id']
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
        rsp_bm = getter.organization_findDivision(cookies=cookies, token=token, userid=userId)
        for i in rsp_bm.json()['data']['list']:
            if i['label'] == f'测试部门{i+1}':
                branch_id = i['id']
                getter.project_add(cookies=cookies, name=f'测试项目{i+1}', token=token, userid=userId, orgId=branch_id)
        yield
        for i in rsp_bm.json()['data']['list']:
            rsp_project = getter.user_findProject(cookies=cookies, divIds=[i['id']], pageNum=1,
                                                  pageSize=1000, token=token, userid=userId)
            for j in rsp_project.json()['data']['list']:
                getter.project_batchDelete(cookies=cookies, id=j['id'], token=token, userid=userId)
    except Exception as e:
        logger.error(f"添加项目前置执行失败，错误为{e}")


@pytest.fixture()
def add_station():
    """
    添加测试岗位数据
    """
    try:
        rsp_data = getter.get_allPerms(cookies=cookies, pageNum=1, pageSize=100, token=token, userid=userId)
        for i in range(3):
            rsp_add = getter.station_save(cookies=cookies, name=f'测试岗位{i+1}', perms=getter.get_dict_allIds(rsp_data.json()),
                                          token=token, userid=userId)
            logger.info(f"添加结果为{rsp_add.json()}")
        yield
        rsp_station = getter.user_findJob(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)
        station_id = []
        for i, items in enumerate(rsp_station.json()['data']['list']):
            if items['name'] == f'测试岗位{i+1}':
                station_id.append(items['id'])
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
        for i in range(3):
            getter.user_save(cookies=cookies, divisionId=branch_id, jobId=station_id[0], name=f'测试添加账号{i+1}',
                             password='123',phone='13100000002', status=1, token=token, userid=userId,
                             projectIds=[project_id])
        yield
        rsp_list = getter.user_list(cookies=cookies, pageNum=1, pageSize=1000, token=token, userid=userId)
        for i in rsp_list.json()['data']['list']:
            if i['name'] == f'测试添加账号{i+1}':
                delete_userId = i['id']
                getter.user_delete(cookies=cookies, id=[delete_userId], token=token, userid=userId)
    except Exception as e:
        logger.error(f"添加项目前置执行失败，错误为{e}")
