import yaml
from configparser import ConfigParser
import os
import xlrd
import json


class MyConfigParser(ConfigParser):
    # 重写 Configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionStr):
        return optionStr


class ReadFileData(object):

    def __init__(self):
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 获取当前项目的绝对路径

    def load_yaml(self, yaml_file_name):
        file_path = os.path.join(self.BASE_PATH, 'data', yaml_file_name)
        with open(file_path, encoding='utf-8') as f:
            data_yaml = yaml.safe_load(f)
        return data_yaml

    def write_data(self, writeData, filename):
        file_path = os.path.join(self.BASE_PATH, 'data')
        with open(os.path.join(file_path, filename), 'w+', encoding='utf-8') as f:
            yaml.safe_dump(writeData, f, allow_unicode=True)

    def load_excel(self, fileName, module, interfaceName):
        data_all = []
        data_return = []
        file_path = os.path.join(self.BASE_PATH, 'data')
        data_xls = xlrd.open_workbook(os.path.join(file_path, fileName))
        sheet1 = data_xls.sheet_by_index(0)
        for i in range(3, sheet1.nrows):
            # print(sheet1.row_values(i)[2], sheet1.row_values(i)[3])
            if sheet1.row_values(i)[2] == module and sheet1.row_values(i)[3] == interfaceName:
                data_all.append(sheet1.row_values(i))
        for j in data_all:
            data_return.append([eval(j[6]), eval(j[7])])
        return data_return

    @staticmethod
    def load_json(file_path):
        with open(file_path, encoding='utf-8') as f:
            data_json = json.load(f)
        return data_json

    def load_ini(self, ini_file_name='config.ini'):
        file_path = os.path.join(self.BASE_PATH, 'config', ini_file_name)
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data_ini = config._sections
        # print("读到数据 ==>>  {} ".format(data))
        return data_ini


data = ReadFileData()


if __name__ == '__main__':
    print(data.load_excel('监理api接口自动化测试用例.xls', '组织架构', '新增平级'))

