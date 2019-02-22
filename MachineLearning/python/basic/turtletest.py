#!/usr/bin/python
#coding: UTF-8

# 基础UI库，turtle（海龟）
import turtle
import time

# 当前时间
print(time.asctime())

t = turtle.Pen()
for i in range(0,4):
  t.forward(100)
  t.left(90)
  time.sleep(1)


t.reset
i = 0
while True:
  t.forward(100)
  t.left(90)
  i+=1
  if i==4:
    break;

# 注意，文件名称不能取名为 turtle.py,否则会报错 AttributeError: 'module' object has no attribute 'pen'

# 参考资料

# turtle的API文档   https://docs.python.org/3/library/turtle.html#turtle.forward

# 视频资料 https://www.icourse163.org/learn/PKU-1002536002?tid=1003797005#/learn/content?type=detail&id=1005355453&cid=1006837816&replay=true

# 报错原因： https://stackoverflow.com/questions/24317944/python-2-7-turtle-error