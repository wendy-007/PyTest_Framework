'''
a=[1,2,3,4]
for x in a:
    print(x)
'''
a=[1,2,3,4]
it = iter(a)
print(next(it))

from data import excel_path
import data
import os
if os.path.exists(excel_path.excel_path):
    print('True')
