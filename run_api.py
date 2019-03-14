# -*- coding:utf-8 -*-
from common.log import logger
from function.func import ApiTest
import common.excel as excel
import config as conf

logger().info('♣♣☆☆☆☆☆☆♣♣♣☆☆☆☆☆☆☆☆☆♣ 开始测试 ♣☆☆☆☆☆☆☆☆♣♣♣☆☆☆☆☆☆☆☆☆')
"""打开Excel"""
workbook = excel.open_excel(conf.FILE_PATH)
sheet = excel.get_sheet('Case')

"""执行测试用例"""
res = ApiTest().run_case(sheet)
logger().info(res)
logger().info('♣♣☆☆☆☆☆☆♣♣♣☆☆☆☆☆☆☆☆☆♣ 测试结束 ♣☆☆☆☆☆☆☆☆♣♣♣☆☆☆☆☆☆☆☆☆')
