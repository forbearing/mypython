#!/usr/bin/env python3
'''
1:排列
    从n个元素中取出 m 个元素,按照一定的顺序排成一列,叫做从n个元素取出m个元素的一个排列.
    特别的, 当 m=n 时,这个排列被称为全排列(Permutation).
'''

import itertools
print("排列")
mylist = list(itertools.permutations([1,2,3,4], 3))
print(mylist)
print(len(mylist))


'''
2:组合
    从 m 个不同的元素中,任取n(n<=m) 个元素为一组,叫做从 m 个不同元素中取出n个元素的
    进行组合(有顺序)
'''
import itertools
print("组合")
mylist = list(itertools.combinations([1,2,3,4], 3))
print(mylist)
print(len(mylist))


# 排列组合
import itertools
mylist = list(itertools.product("0123456789", repeat=10))
print(mylist)
print(len(mylist))

# 破解密码
import itertools
passwd = (".join(x)" for x in itertools.product("0123456789", repeat=3))
while True:
    try:
        str = next(passwd)
        print(str)
    except StopIteration as e:
        break
