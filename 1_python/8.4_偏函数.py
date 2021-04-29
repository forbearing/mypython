1:概念
    1:函数在执行的时候，要带上所有必要的参数。但是，有时参数可以在函数被调用之前提前
      获知。这种情况下，一个函数有一个或多个参数预先就能用上，
      以便函数能用更少的参数进行调用
    2:偏函数是将所要承载的函数作为 partial() 函数的第一个参数，原函数的各个参数依次
      作为 partial() 函数后续的参数，除非使用关键字参数

    ---
    from functools import partial
    def mod(n,m):
        return n % m
    mod_by_100 = partial(mod, 100)
    print(mod(100,7))
    print(mod_by_100(7))

    ---
    from functools import partial
    bin2dec = partial(int, base=2)
    print bin2dec( '0b10001' )
    print bin2dec( '10001' )

    hex2dec = partial( int, base=16 )
    print hex2dec( '0x67' )  # 103
    print hex2dec( '67' )  # 103
