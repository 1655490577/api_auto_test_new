from API.api_get_data import getter
import jsonpath


token, userId, cookies = getter.get_login_token_cookies('13168775547', '123', 2)
# print(token, userId)
rsp_data1 = getter.user_findDivision(cookies=cookies, pageNum=1, pageSize=10000, mobileType=2, token=token, userid=userId)
# print(rsp_data1.json())
branch_id = jsonpath.jsonpath(rsp_data1.json(), '$..id')
print(branch_id)
rsp_data2 = getter.user_findProject(cookies=cookies, divIds=branch_id[0], pageNum=1, mobileType=2, pageSize=10000,
                                    token=token, userid=userId)
project_ids = jsonpath.jsonpath(rsp_data2.json(), '$..id')
print(project_ids)

