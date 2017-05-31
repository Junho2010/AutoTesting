# coding=utf-8
import ConfigParser
import unittest
from selenium import webdriver



# 重写配置读取类，避免大小写变更问题
class MyConfig(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self, defaults=defaults)
    def optionxform(self, optionstr):
        return optionstr


# 重写TestCase类，在初始化中读入配置信息
class MyTest(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(MyTest, self).__init__(methodName)

        # 设置默认的浏览器为火狐
        self.test = webdriver.Chrome()
        self.other = webdriver.Firefox()

        # 读取基本配置
        self.baseConfig = MyConfig()
        self.baseConfig.read('base.ini')

        # 读取控件配置
        self.controlsConfig = MyConfig()
        self.controlsConfig.read('Controls.ini')
        self.element = dict(self.controlsConfig.items('element'))
        self.elements = dict(self.controlsConfig.items('elements'))

        # 读取用例变量配置
        self.caseConfig = MyConfig()
        self.caseConfig.read('TestCase.ini')

        # 根据控件名称获取单个控件
        def getControl(self, name, conf=self.element):
            lst = conf[name].split('|')
            return self.test.find_element(lst[0],lst[1])

        # 根据控件名称获取一组控件
        def getControls(self, name, conf=self.elements):
            lst = conf[name].split('|')
            return self.test.find_elements(lst[0],lst[1])

        # 根据用例名称和参数名称获取参数
        def getCaseParameter(self, caseName, parameterName, conf=self.caseConfig):
            return conf.get(caseName, parameterName)
