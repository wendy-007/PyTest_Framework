'''进行数据分离，进行参数化'''
import xlrd
from data import excel_path
import os
def read_excel():
    # 加一个文件判断
    if os.path.exists(excel_path.excel_path):
        print('True')
        # 打开excel文件获取数据
        data = xlrd.open_workbook(excel_path.excel_path)
    else:
        raise FileNotFoundError

    # 获取一个工作表
    table = data.sheet_by_index(0)  # 第一张Sheet表
    col = table.col_values(0)       # 读取第一列
    print(col)

    all_tel = []
    a = len(col) - 1
    i = 1
    while i <= a:
        tel = int(col[i])
        #print(tel)
        all_tel.append(tel)
        i = i + 1
    print(all_tel)
    return all_tel

read_excel()

