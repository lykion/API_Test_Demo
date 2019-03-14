# -*- coding:utf-8 -*-
import xlrd
import config as conf

workbook = None


def open_excel(path):
    """
    打开Excel
    :param path: Excel路径
    :return:
    """
    global workbook
    if workbook == None:
        workbook = xlrd.open_workbook(path)
    return workbook


def get_sheet(sheetName):
    """
    通过sheet打开工作簿
    :param sheetName:
    :return:
    """
    global workbook
    return workbook.sheet_by_name(sheetName)


def get_row(sheet):
    """
    获取行数
    :param sheet:
    :return:
    """
    return sheet.nrows


def get_col(sheet):
    """
    获取列数
    :param sheet:
    :return:
    """
    return sheet.ncols


def get_cell_content(sheet, row, col):
    """
    获取单元格内容
    :param sheet: sheet名
    :param row: 行
    :param col: 列
    :return:
    """
    return sheet.cell_value(row, col)


"""测试类"""
if __name__ == '__main__':
    wb = open_excel(conf.FILE_PATH)
    ws = get_sheet('Test_Case')
    row = get_row(ws)
    col = get_col(ws)
    cell_content = get_cell_content(ws, 1, 3)
    print(ws.name, row, col, cell_content)
