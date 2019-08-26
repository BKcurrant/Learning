# -*- coding= utf-8 -*-
import pandas as pd
data=pd.read_excel('13.xlsx')
col=data.iloc[:,2]
arrs=col.values
#输出结果
print(arrs)
print(arrs.size)
i = 1
a = 0.0
b = 0.0
c = 0.
for i in range(arrs.size):
    if arrs[i-1]>90:
        a = a + 1.0
    elif arrs[i-1]>80:
        b = b + 1.0
    else:
        c = c + 1.0
s = a+b+c
aa = round(a/s,2)
bb = round(b/s,2)
cc = round(c/s,2)


import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
plt.figure(figsize=(6,6))#将画布设定为正方形，则绘制的饼图是正圆
label=['优秀','良好','及格']#定义饼图的标签，标签是列表
explode=[0.01,0.01,0.01]#设定各项距离圆心n个半径
values=[aa,bb,cc]
plt.pie(values,explode=explode,labels=label,autopct='%1.1f%%')#绘制饼图
plt.title('成绩分布比例')#绘制标题
plt.show()
