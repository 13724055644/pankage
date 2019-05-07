#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 8:54
# @Author  : wuhy


import openpyxl

wb = openpyxl.load_workbook('news.xlsx')
sheet = wb.worksheets[0]

#读取第一行第一列单元格值
sheet_value = sheet.cell(1,1).value
print('第一行第一列单元格的值为:{}'.format(sheet_value))