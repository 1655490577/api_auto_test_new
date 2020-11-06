import requests
from API.api_base import baseApi


class Requester(baseApi):

    def __init__(self):
        super().__init__()

    def user_login(self, **kwargs):  # 登录
        return requests.post(url=self.ip + '/admin/login', json=kwargs, headers=self.headers)

    def user_logout(self, cookies, **kwargs):  # 注销退出
        return requests.post(url=self.ip + '/admin/logout', json=kwargs, headers=self.headers, cookies=cookies)

    def user_delete(self, cookies, **kwargs):  # 删除用户
        return requests.post(url=self.ip + '/admin/delete', json=kwargs, headers=self.headers, cookies=cookies)

    def user_detail(self, cookies, **kwargs):  # 注销退出
        return requests.post(url=self.ip + '/admin/detail', json=kwargs, headers=self.headers, cookies=cookies)

    def user_list(self, cookies, **kwargs):  # 用户列表
        return requests.post(url=self.ip + '/admin/list', json=kwargs, headers=self.headers, cookies=cookies)

    def user_list_nothing(self, cookies, **kwargs):  # 用户列表（无权限）
        return requests.post(url=self.ip + '/admin/list/nothing', json=kwargs, headers=self.headers, cookies=cookies)

    def user_listByIds(self, cookies, **kwargs):  # 获取登录后可选择项目
        return requests.post(url=self.ip + '/admin/listByIds', json=kwargs, headers=self.headers, cookies=cookies)

    def user_save(self, cookies, **kwargs):  # 新增用户
        return requests.post(url=self.ip + '/admin/save', json=kwargs, headers=self.headers, cookies=cookies)

    def user_update(self, cookies, **kwargs):  # 修改用户
        return requests.post(url=self.ip + '/admin/update', json=kwargs, headers=self.headers, cookies=cookies)

    def user_updatePsw(self, cookies, **kwargs):  # 修改密码
        return requests.post(url=self.ip + '/admin/updatePsw', json=kwargs, headers=self.headers, cookies=cookies)

    def user_findDivision(self, cookies, **kwargs):  # 查询事业部
        return requests.post(url=self.ip + '/admin/findDivision', json=kwargs, headers=self.headers, cookies=cookies)

    def user_findJob(self, cookies, **kwargs):  # 查询岗位
        return requests.post(url=self.ip + '/admin/findJob', json=kwargs, headers=self.headers, cookies=cookies)

    def user_findProject(self, cookies, **kwargs):  # 查询项目
        return requests.post(url=self.ip + '/admin/findProject', json=kwargs, headers=self.headers, cookies=cookies)

    def organization_save(self, cookies, **kwargs):  #
        return requests.post(url=self.ip + '/organization/save', json=kwargs, headers=self.headers, cookies=cookies)

    def organization_update(self, cookies, **kwargs):  #
        return requests.post(url=self.ip + '/organization/update', json=kwargs, headers=self.headers, cookies=cookies)

    def organization_detail(self, cookies, **kwargs):  #
        return requests.post(url=self.ip + '/organization/detail', json=kwargs, headers=self.headers, cookies=cookies)

    def organization_delete(self, cookies, **kwargs):  #
        return requests.post(url=self.ip + '/organization/delete', json=kwargs, headers=self.headers, cookies=cookies)

    def organization_list(self, cookies, **kwargs):  #
        return requests.post(url=self.ip + '/organization/list', json=kwargs, headers=self.headers, cookies=cookies)

    def organization_list_nothing(self, cookies, **kwargs):  #
        return requests.post(url=self.ip + '/organization/list/noting', json=kwargs, headers=self.headers, cookies=cookies)

    def organization_findDivision(self, cookies, **kwargs):  #
        return requests.post(url=self.ip + '/organization/findDivision', json=kwargs, headers=self.headers, cookies=cookies)

    def organization_findOrganizationTree(self, cookies, **kwargs):  #
        return requests.post(url=self.ip + '/organization/findOrganizationTree', json=kwargs, headers=self.headers, cookies=cookies)

    def organization_findProjectByDivids(self, cookies, **kwargs):  #
        return requests.post(url=self.ip + '/organization/findProjectByDivids', json=kwargs, headers=self.headers, cookies=cookies)

    def project_add(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfo/add', json=kwargs, headers=self.headers, cookies=cookies)

    def project_batchDelete(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfo/batchDelete', json=kwargs, headers=self.headers, cookies=cookies)

    def project_detail(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfo/detail', json=kwargs, headers=self.headers, cookies=cookies)

    def project_list(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfo/list', json=kwargs, headers=self.headers, cookies=cookies)

    def project_listByIds(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfo/listByIds', json=kwargs, headers=self.headers, cookies=cookies)

    def project_update(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfo/update', json=kwargs, headers=self.headers, cookies=cookies)

    def build_add(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/buildInfo/add', json=kwargs, headers=self.headers, cookies=cookies)

    def build_batchDelete(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/buildInfo/batchDelete', json=kwargs, headers=self.headers, cookies=cookies)

    def build_detail(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/buildInfo/detail', json=kwargs, headers=self.headers, cookies=cookies)

    def build_list(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/buildInfo/list', json=kwargs, headers=self.headers, cookies=cookies)

    def build_update(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/buildInfo/update', json=kwargs, headers=self.headers, cookies=cookies)

    def projectBid_add(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/add', json=kwargs, headers=self.headers, cookies=cookies)

    def projectBid_batchDelete(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/batchDelete', json=kwargs, headers=self.headers, cookies=cookies)

    def projectBid_detail(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/detail', json=kwargs, headers=self.headers, cookies=cookies)

    def projectBid_list(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/list', json=kwargs, headers=self.headers, cookies=cookies)

    def projectBid_update(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/update', json=kwargs, headers=self.headers, cookies=cookies)

    def basement_add(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/add', json=kwargs, headers=self.headers, cookies=cookies)

    def basement_batchDelete(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/batchDelete', json=kwargs, headers=self.headers, cookies=cookies)

    def basement_detail(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/detail', json=kwargs, headers=self.headers, cookies=cookies)

    def basement_list(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/list', json=kwargs, headers=self.headers, cookies=cookies)

    def basement_update(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/projectInfoBid/update', json=kwargs, headers=self.headers, cookies=cookies)

    def station_delete(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/role/delete', json=kwargs, headers=self.headers, cookies=cookies)

    def station_find(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/role/find', json=kwargs, headers=self.headers, cookies=cookies)

    def station_list(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/role/list', json=kwargs, headers=self.headers, cookies=cookies)

    def station_list_nothing(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/role/list/nothing', json=kwargs, headers=self.headers, cookies=cookies)

    def station_save(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/role/save', json=kwargs, headers=self.headers, cookies=cookies)

    def station_update(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/role/update', json=kwargs, headers=self.headers, cookies=cookies)

    def get_allPerms(self, cookies, **kwargs):
        return requests.post(url=self.ip + '/admin/sysmenu/tree/nothing', json=kwargs, headers=self.headers, cookies=cookies)
