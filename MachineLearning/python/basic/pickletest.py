#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pickle
import codecs

data = {'name': 'jerry', 2: [23, 4], '234': {1: 2, 'd': 'sad'}}

with open('testdata1.txt', 'w') as f:
    # pickle.dump(data,f)
    f.write('Hello, world!')
    f.close()



with codecs.open('testdata.txt', 'r', 'gbk') as f:
    r = f.read()
    print(r)
    f.close()



# 注意事项
# pickle.dump  读写文件类型时，默认使用t（文本），其他数据类型，比如这里data字典会报错

# 参考资料

# pickle.dump文档 https://morvanzhou.github.io/tutorials/python-basic/basic/13-08-pickle/

# 文件标识符类型列表  http://www.runoob.com/python/python-files-io.html