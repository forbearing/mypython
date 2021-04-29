str1=" func1 "
print(str1.center(40, "="))
a = 10
def func1(x):
    y = x                   # x,y,a 的地址相同，都是指向常量10 id(x )= id(y )= id(a)
    print("y = x")
    print("id(x):", id(x))
    print("id(y):", id(y))
    y = x = 20              # x,y 的地址指向新的常量20, id(x) = id(y) !=id(a)
    print("y = x = 20")
    print("id(x):", id(x))
    print("id(y):", id(y))
    y = 30                  # y 的地址指向新的常量30, id(x) != id(y)
    print("y = 30")
    print("id(x):", id(x))
    print("id(y):", id(y))
func1(a)
print(id(a))


str2 = " func2 "
print(str2.center(40, "="))
li = [1,2,3]
def func2(li):
    myli = li                       # id(x) = id(y) = id(a)
    print("myli = li")
    print("id(myli):", id(myli))
    print("id(li):", id(li))
    myli[0] = 100                   # id(myli) = id(li)
    print("myli[0]=100")
    print("id(myli):", id(myli))
    j=print("id(li):", id(li))
    myli = [2,3,4]                  # id(myli) != id(li)
    print("myli=[2,3,4]")
    print("id(myli):", id(myli))
    print("id(li)", id(li))
func2(li)
print(id(li))
