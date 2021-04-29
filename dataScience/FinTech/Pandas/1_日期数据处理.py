#!/usr/bin/env python3
import pandas as pd

1:读取并整理数据
    # 从 csv 文件中读取数据
    df = pd.read_csv('data.csv', header=None)
    print(df.head(2))

    # 整理数据
    df.columns = ['data', 'number']
    df['date'] = pd.to_datetime(df['date'])     # 将数据类型转换为日期类型
    df = df.set_index('date')                   # 将 date 设置为 index
    print(df.head(2))
    print(df.tail(2))
    print(df.shape)

    # 查看 Dataframe 的数据类型
    print(type(df))
    print(df.index)
    print(type(df.index))

    # 构造 Series 数据
    s = pd.Series(df['number'], index=df.index)
    print(type(s))
    s.head(2)



2:按日期筛选数据
    # 1.按年度获取数据
    print('--------- 获取 2013 年的数据 -----------')
    print(df['2003'].head(2))           # 获取2013年的数据
    print(df['2003'].tail(2))           # 获取2013年的数据

    # 2.获取2016年到2017年的数据
    print('--------- 获取 2016 至 2017 年的数据 -----------')
    print(df['2016':'2017'].head(2))    # 获取2016到2017年的数据
    print(df['2016':'2017'].tail(2))    # 获取2016到2017年的数据

    # 3.获取某月数据
    print('--------- 获取某月的数据 -----------')
    print(df['2013-11'])                # 获取某月的数据

    # 4.获取具体某天的数据
    print('--------- 获取具体某天的数据 -----------')
    print(s['2013-11-06'])
        # 获取具体某天的数据，用 dataframe 直接选取某天时会报错，而 Series 的数据
        # 就没有问题。
    print(s['2013-11-06':'2013-11-06'])

    1:dataframe的truncate函数可以获取某个时期之前或之后的数据，或者某个时间区间的数据
    2:但一般建议直接用切片(slice)，这样更为直观，方便
    print('---------获取某个时期之前或之后的数据-----------')
    print('--------after------------')
    print(df.truncate(after = '2013-11'))
    print('--------before------------')
    print(df.truncate(before='2017-02'))



3:按日期显示数据
    ---
    to_period() 方法
    1:请注意 df.index 的数据类型是 DatetimeIndex
    2:df_peirod的数据类型是PeriodIndex

    # 1.按月显示，但不统计
    df_period = df.to_period('M')
    print(type(df_period))
    print(type(df_period.index))
    print(df_period.head())

    # 2.按季度显示，但不统计
    print(df.to_period('Q').head())

    # 3.按年度显示，但不统计
    print(df.to_period('A').head())

    ---
    asfreq() 方法
    # 1.按年度频率显示
    df_period.index.asfreq('A')         # 'A' 默认是'A-DEC',其他如 'A-JAN'

    # 2.按季度频率显示
    df_period.index.asfreq('Q')         # 'Q' 默认是 'Q-DEC',其他如 'Q-SEP', 'Q-FEB'
    df_period.index.asfreq('Q-SEP')     # 可以显示不同的季度财年
    df_period.index = df_period.index.asfreq('Q-DEC')
    print(df_period.head())

    # 3.按月度频率显示
    df_period.index.asfreq('M')         # 按月份显示

    # 4.按工作日显示
    df_period.index.asfreq('B', how='start')
    df_period.index.asfreq('B', how='end')



4:按日期统计数据
    --- 按日期统计数据
    # 1.按周统计数据
    print(df.resample('w').sum().head())

    # 2.按月统计
    print(df.resample('M').sum().head())

    # 3.按季度统计
    print(df.resample('Q').sum().head())

    # 4.按年统计
    print(df.resample('AS').sum())

    --- 按日期统计后，按年或季度或月份显示
    # 1.按年统计并显示
    print(df.resample('AS').sum().to_period('A'))

    # 2.按季度统计并显示
    print(df.resample('Q').sum().to_period('Q').head())

    # 3.按月度统计并显示
    print(df.resample('M').sum().to_period('M').head())
