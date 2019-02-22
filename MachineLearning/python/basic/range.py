import os
# 方式一，使用range循环生成列表
r = []
for x in range(1, 11):
    r.append(x*x)
print(r)



# 方式二。使用 列表生成式 生成列表
# 生成结果写在for前，生成规则写在for后
rl = [x * x for x in range(1, 11)]
print(rl)



# 实践1，使用列表生成式的简洁语法，列出文件
test1 = [dir for dir in os.listdir('.')]
print(test1)

# 实践2，把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
test2 = [str.lower() for str in L]
print(test2)

# 参考资料
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681963899940a998c0ace64bb5ad45d1b56b103c48000