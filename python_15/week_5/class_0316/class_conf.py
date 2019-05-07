# -*- coding:utf-8 -*-
# @time:2019/3/18 17:05
# @Author:MOQIN
# @File:class_conf.py
# @Software:python_15
# 封装类
from configparser import ConfigParser


class myConfig:
    # 初始化
    def __init__(self, conf_filePath, enconding="utf-8"):
        # 打开配置文件
        self.cf = ConfigParser()
        self.cf.read(conf_filePath, enconding)

    # 获取整数
    def get_intValue(self, section, option):
        return self.cf.getint(section, option)

    # 获取字符串
    def get_strValue(self, section, option):
        return self.cf.get(section, option)

    # 获取布尔值
    def get_boolValue(self, section, option):
        return self.cf.getboolean(section, option)

    # 获取浮点数
    def get_floatValue(self, section, option):
        return self.cf.getfloat(section, option)

    # 读取文件
    def get_sections(self):
        return self.cf.sections()

    def get_options(self):
        return self.cf.options()


# 例如
my = myConfig("demo.cfg")
db_name = my.get_strValue("db", "db_name")
print(db_name)

print(my.get_sections())
print(my.get_options())
