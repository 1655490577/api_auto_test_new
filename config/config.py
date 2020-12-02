# 配置文件


def server_ip():
    """
    设置服务器ip地址
    server_ip_outside：str  外网地址
    server_ip_inside：str  内网地址
    :return:
    """
    server_ip_dev = 'http://manage.supervisor.dev.hfhksoft.com/api'   # 开发环境
    server_ip_test = 'http://manage.supervisor.test.hfhksoft.com/api'  # 测试环境
    return server_ip_test


def mysql_setting():
    """
    数据库连接配置
    host 服务器ip地址
    user 数据库登录名
    password 登录密码
    database 要使用的数据库
    autocommit 防止事物执行阻塞，默认为false
    """
    dev_sql = {
        "host": "192.168.30.21",
        "port": 3306,
        "user": "supervisor",
        "password": "Hfhk-supervisor-!@#-1230.",            # 开发环境数据库
        "database": "supervisor",
        "autocommit": True
    }

    test_sql = {
        "host": "192.168.30.21",
        "port": 3307,
        "user": "supervisor",
        "password": "Hfhk-supervisor-!@#-1230.",            # 测试环境数据库
        "database": "supervisor",
        "autocommit": True
    }

    return test_sql
