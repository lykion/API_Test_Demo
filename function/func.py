# -*- coding:utf-8 -*-
import time
import datetime
import json
import common.excel as excel
import config as conf
import common.res as res
import function.write as w
from common.log import logger


class ApiTest:
    """ """

    def __init__(self):
        pass

    def run_case(self, sheet):
        """
        读取Excel中的测试用例，并执行测
        :param sheet: sheet
        :return: result -- 接口返回的结果
        """
        row = excel.get_row(sheet)      # 获取Excel测试用例的行
        for i in range(1, row):         # 通过for循环的方式，遍历取出Excel所有的用例
            id = int(excel.get_cell_content(sheet, i, conf.CASE_ID-1))
            host = conf.host
            url = excel.get_cell_content(sheet, i, conf.CASE_URL-1)
            data = excel.get_cell_content(sheet, i, conf.CASE_DATA-1)
            method = excel.get_cell_content(sheet, i, conf.CASE_METHOD-1)
            header = conf.headers
            is_header = excel.get_cell_content(sheet, i, conf.CASE_HEADER-1)
            # testTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            StartTime = datetime.datetime.now()
            logger().info('Start Time is: {}'.format(StartTime))
            result = res.test_api(method, host + url, data, header, is_header)  # 执行请求,返回的结果是json格式
            actual_msg = result.get('msg')      # 接口实际返回的 msg
            # Excel中的msg；此方法是用xlrd操作Excel，所以索引要用实际值-1
            expect_msg = excel.get_cell_content(sheet, i, conf.CASE_CHECK_POINT-1)      # 期望结果
            if expect_msg == actual_msg:      # 检查通过，将结果写入Excel
                w.write_to_excel(conf.FILE_PATH, conf.SHEET_NAME, i + 1, conf.CASE_TEST_RESULT, conf.PASS)
                # 将返回的结果转换成str写入Excel
                w.write_to_excel(conf.FILE_PATH, conf.SHEET_NAME, i + 1, conf.CASE_RESPONSE, str(result))
                w.write_to_excel(conf.FILE_PATH, conf.SHEET_NAME, i + 1, conf.CASE_TEST_TIME, StartTime)
                logger().info('第{}条用例测试成功'.format(id))
                logger().info(result)
                logger().info('--------------------------------------------------------------------------'
                              '-----------------------------------------')
            else:   # 检查不通过，将结果写入Excel
                w.write_to_excel(conf.FILE_PATH, conf.SHEET_NAME, i + 1, conf.CASE_TEST_RESULT, conf.FAIL)
                w.write_to_excel(conf.FILE_PATH, conf.SHEET_NAME, i + 1, conf.CASE_TEST_TIME, StartTime)
                logger().info('请求失败')
                logger().info('第{}条用例测试失败'.format(id))


"""测试类"""
if __name__ == '__main__':
    wb = excel.open_excel(conf.FILE_PATH)
    sheet = excel.get_sheet('Case')
    ApiTest().run_case(sheet)
