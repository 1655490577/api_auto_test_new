import pytest
import xlrd
import re
from API.api_get_data import getter
# from collections import Iterable
import requests

# class TestQer(object):
#
#     @pytest.mark.parametrize(('a', 'b'),
#                              getter.load_excel('监理api接口自动化测试用例.xls', '组织架构新增平级'))
#     def test1(self, a, b):
#         print(a, b)

# data_return = []
# data_xls = xlrd.open_workbook('监理api接口自动化测试用例.xls')
# sheet1 = data_xls.sheet_by_index(0)
# for i in range(3, sheet1.nrows):
#     if sheet1.row_values(i)[3] == '登录':
#         data_return.append(sheet1.row_values(i))
#
# print(data_return)

# a = [{"password": "123456", "phone": "13168775501", "rememberMe": True}]
# print(list(a))
token, userId, cookies = getter.get_login_token_cookies('13168775547', '1')
# # a = getter.organization_findDivision(cookies=cookies, token=token, userid=userId)
# # print(a.json())
# a = []
rsp_test = getter.user_findJob(cookies=cookies, token=token, userid=userId, pageNum=1, pageSize=100)
# print(rsp_test.json())
print(re.search("52", "sadfdsfadsfdasf'name': '测试系统管理权限'"))


# if isinstance(rsp_test['data']['children'], Iterable):


# class Test(object):
#
#     def __init__(self):
#         self.id_list = []
#
#     def get_dict_allkeys(self, dict_a):
#         """
#             多维/嵌套字典数据无限遍历，获取json返回结果的所有key值集合
#             :param dict_a:
#             :return: key_list
#             """
#         if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
#             for x in range(len(dict_a)):
#                 temp_key = tuple(dict_a.keys())[x]
#                 temp_value = dict_a[temp_key]
#                 self.get_dict_allkeys(temp_value)  # 自我调用实现无限遍历
#         elif isinstance(dict_a, list):
#             for k in dict_a:
#                 if isinstance(k, dict):
#                     for x in range(len(k)):
#                         temp_key = tuple(k.keys())[x]
#                         temp_value = k[temp_key]
#                         self.get_dict_allkeys(temp_value)
#                     self.id_list.append(k['id'])
#         return self.id_list
#
#
# a = Test()
# print(a.get_dict_allkeys(rsp_test.json()))
