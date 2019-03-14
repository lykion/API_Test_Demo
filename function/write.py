# -*- coding:utf-8 -*-
import openpyxl
import config as conf
from common.log import logger


def write_to_excel(path, sheetName, row, col, string):
    """
    1、向Excel中写入内容
    2、openpyxl操作Excel时，索引是与Excel本身的序号对应，而不是从0开始，而是从1开始
    3、在执行写入操作时，Excel文件必须是关闭的，否则报错
    :param path: Excel路径
    :param sheetName: sheetName
    :param row: 行
    :param col: 列
    :param string: 写入单元格的内容
    :return:
    """
    try:
        workbook = openpyxl.load_workbook(path)
        sheet = workbook[sheetName]
        sheet.cell(row=row, column=col).value = string
        workbook.save(path)
        # logger().info('操作成功')
    except Exception as e:
        logger().info('操作失败：{}'.format(e))


if __name__ == '__main__':
    write_to_excel(conf.FILE_PATH, conf.SHEET_NAME, 2, 11, 'This is a test string.')

