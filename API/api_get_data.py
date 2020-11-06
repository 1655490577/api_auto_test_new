from API.api_request import Requester
from common.read_data import ReadFileData


class get_data(Requester, ReadFileData):
    def __init__(self):
        super().__init__()
        self.BASE_PATH = ReadFileData().BASE_PATH
        self.id_list = []

    def get_login_token_cookies(self, phone, password, rememberMe=False):
        """
        获取用户登录成功后的token和cookies
        """
        r = self.user_login(phone=phone, password=password, rememberMe=rememberMe)
        token, userId, cookies = r.json()['data']['token'], r.json()['data']['tbAdmin']['id'], r.cookies.get_dict()
        return token, userId, cookies

    def get_dict_allIds(self, dict_a):
        """
            多维/嵌套字典数据无限遍历，获取json返回结果的所有id集合
            :param dict_a:
            :return: key_list
            """
        if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
            for x in range(len(dict_a)):
                temp_key = tuple(dict_a.keys())[x]
                temp_value = dict_a[temp_key]
                self.get_dict_allIds(temp_value)  # 自我调用实现无限遍历
        elif isinstance(dict_a, list):
            for k in dict_a:
                if isinstance(k, dict):
                    for x in range(len(k)):
                        temp_key = tuple(k.keys())[x]
                        temp_value = k[temp_key]
                        self.get_dict_allIds(temp_value)
                    self.id_list.append(k['id'])
        return self.id_list


getter = get_data()

if __name__ == '__main__':
    token1, userId1, cookies1 = getter.get_login_token_cookies('admin', 'admin')
    rsp = getter.organization_findOrganizationTree(cookies=cookies1, code='01', token=token1, userid=userId1)
    print(rsp.json()['data']['list'][0]['id'])
