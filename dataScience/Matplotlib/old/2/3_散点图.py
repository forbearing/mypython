1:
    1:散点图通常用于比较跨类别的聚合数据
    2:散点图可以提供两类信息
        1:变量之间是否存在数值或数量的关联趋势，以及关联趋势是线性还是非线性的；
        2:如果有某一个点或者某几个点偏离大多数点，也就是离群值，通过散点图可以一目了然，
          从而可以进一步分析这些离群值是否可能在建模分析中对总体产生很大影响。



2:
matplotlib.pyplot.scatter(x,y,s=None,c=None,marker=None,cmap=None,norm=None,
    vmin=None,vmax=None,alpha=None,linewidths=None,verts=None,edgecolors=None,
    hold=None,data=None,**kwargs)
    x,y     接收 array。表示 x 轴和 y 轴对应的数据，无默认；
    s       接收数值或者一维的 array。指定点的大小，若传入一维 array，则表示每个点的大小，默认为 None
    c       接收颜色或者一维的 array。指定点的颜色，若传入一维 array，则表示每个点的颜色，默认为 None
    marker  接收特定 string。表示绘制的点的类型，默认为 None
    alpha   接收 0~1 的小数。表示点的透明度，默认为 None

---
import numpy as np
import matplotlib.pyplot as plt
#导入数据
Emp_data= np.loadtxt('d:\data\Employedpopulation.csv',delimiter = ",",
                     usecols=(1,2,3,4,5,6,7,8,9,10),dtype=int)
# 设置Matplotlib正常显示中文和负号
plt.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
plt.rcParams['axes.unicode_minus']=False     # 正常显示负号
#创建一个绘图对象, 并设置对象的宽度和高度
plt.figure(figsize=(6, 4))
#绘制全部就业人员散点图
plt.scatter(Emp_data[0],Emp_data[1],marker='o')
#绘制城镇就业人员散点图
plt.scatter(Emp_data[0],Emp_data[2],marker='x')
#绘制乡村就业人员散点图
plt.scatter(Emp_data[0],Emp_data[3],marker='v')
plt.xlabel('年份')
plt.ylabel('人员(万人)')
plt.ylim((30000,80000))
plt.xlim(2006,2017)
plt.title("2007-2016年城镇、乡村和全部就业人员情况散点图")
#添加图例
plt.legend({'全部就业','城镇就业'，'乡村就业'})
plt.savefig('d:/data/Employedpopulation_s.png')
plt.show()
