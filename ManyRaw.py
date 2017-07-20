#coding=utf-8
#r'....' 克服其中有多个转义字符的情况，但是不能够应对‘’和“”的显示
#'''.....'''显示多行字符串
#r'''.....'''转换为raw字符串，既可以展示多行同时可以克服其中包含的多个转义字符
#u'''....'''打印中文Unicode编码

a = r'(~~~~~~~~)'
print a
b = '(~~~/~~\\~~/~~\\~)'
print b
c = r'''i' am "jason"'''
print c

print '''line1
line2
line3'''

print r'''  '\"To be,or not to be\":that is the question.\nWhether it \'s nobler in the in the mind to suffer '''

print u'''静夜思
床前明余光
意识地上黄
'''