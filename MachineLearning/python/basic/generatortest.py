# 迭代器
g = (x * x for x in range(10))
s1 = next(g)
print(s1)
s2 = next(g)
print(s2)
s3 = next(g)
print(s3)
s4 = next(g)
print(s4)


print('===================')

for n in g:
  print(n)




# 参考资料

# generator生成器教程 https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681965108490cb4c13182e472f8d87830f13be6e88000
# next API文档 http://www.runoob.com/python/python-func-next.html