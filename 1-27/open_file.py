import os, sys

# f = open(r'D:\GitHub\Django\1-27\file_test\demo1.txt', 'a')
# f.write('zhangchenfang')
# f.close()
#
# f = open(r'D:\GitHub\Django\1-27\file_test\demo1.txt', 'r')
# print("读取的字符串是 : ", f.read())
# f.close()

# f = open(r'D:\GitHub\Django\1-27\file_test\demo1.txt', 'r+')
# print("读取的字符串是 : ", f.read(5))  # 读5个字节
#
# position = f.tell()
# print('当前位置：', position)  # 指针位置在第position个字节之后
#
# f.seek(1, 0)  # 重新定位
# """
# seek（offset [,from]）
# Offset变量表示要移动的字节数
# From 移动模式：0 从头  1  从当前  2从尾
# 在使用模式时要注意文件的打开方式是否允许指针从中间移动
# """
# print("读取的字符串是 : ", f.read(5))
#
# f.close()

# os.rename(old_name, new_name)
# os.remove(file_name)
# os.mkdir("newdir")
# 改变当前目录 使py定位到相应的目录，以便于输入相对路径
# os.chdir("newdir")
# 当前目录
# os.getcwd()
# 删除当前目录 必须保证目录内没有文件
# os.rmdir('dirname')
# 递归删除目录。
# os.removedirs(path)
# 目录重命名
# os.rename(old, new)
# 列出当前目录下的所有文件(夹)
# os.listdir(os.getcwd())

# os.chdir('./file_test/')
# v = os.getcwd()
# print(v)
# print('目录：', os.listdir(os.getcwd()))
# os.rename('ee', 'e12')
# print('目录：', os.listdir(os.getcwd()))

"""
文件打开模式：
x	写模式，新建一个文件，如果该文件已存在则会报错。
+	打开一个文件进行更新(可读可写)。
b	二进制模式。

r	以只读方式打开文件。文件的指针将会放在文件的开头
rb
r+	打开一个文件用于读写。文件指针将会放在文件的开头
rb+

w	只写。并从开头开始编辑，覆盖。不存在则创建
wb
w+
wb+

a   追加 不存在则创建
ab
a+
ab+
"""

