# -*- coding:utf-8 -*-
""" 接口相关配置 """
host = 'http://127.0.0.1:5025'

"""Excel"""
# FILE_PATH = "F:\PyCharmProject\LYKION\new\API_Case.xlsx"      # 因为文件夹的名字中有'n'，而在Python中'n'表示空格，所以要在前面加'\'进行转义
FILE_PATH = "F:\PyCharmProject\LYKION\self_learn\API_Case.xlsx"
SHEET_NAME = 'Case'

"""Excel中单元格列的配置"""
''' 
1、下面数值与Excel的序号一一对应
2、若使用xlrd，则需要-1，因为索引是从0开始
3、若使用openpyxl，则不需要-1，因为索引是从1开始
'''
CASE_ID = 1
CASE_URL = 4
CASE_METHOD = 5
CASE_HEADER = 6
CASE_DATA = 8
CASE_CHECK_POINT = 9
CASE_TEST_RESULT = 10
CASE_TEST_TIME = 11
CASE_RESPONSE = 12

"""向Excel中写入内容配置"""
PASS = 'Pass'
FAIL = 'Fail'

"""其他(测试类会用到)"""
url = 'http://127.0.0.1:5025/do/extra'
method = 'post'
data = {
    'OrderCode': '1002',
    'ShipperCode': 'SF',
    'LogisticCode': '118652124588863'
        }

headers = {
    'Content-Type': 'application/json'
}
data_type = 'Json'
is_header = 'yes'
