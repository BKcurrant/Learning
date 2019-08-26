# -*- coding= utf-8 -*-
import pandas as pd
data=pd.read_excel('13.xlsx')
col=data.iloc[:,3]
arrs=col.values
#输出结果
print(arrs)
print(arrs.size)
i = 1
a = 0
b = 0
c = 0
for i in range(arrs.size):
    if arrs[i-1]>=90:
        a = a + 1
    elif arrs[i-1]>=80:
        b = b + 1
    else:
        c = c + 1
s = a+b+c

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
plt.figure(figsize=(6,6))#将画布设定为正方形，则绘制的饼图是正圆
label=['优秀','良好','及格']#定义饼图的标签，标签是列表
explode=[0.01,0.01,0.01]#设定各项距离圆心n个半径
values=[a,b,c]
plt.pie(values,explode=explode,labels=label,autopct='%1.2f%%')#绘制饼图
plt.title('C语言成绩分布')#绘制标题
total = '总人数：%.f'%s
excellent = '优秀：%.f'%a
good = '良好：%.f'%b
pas = '及格：%.f'%c
plt.text(-0.9,1.15,total)
plt.text(-0.4,1.15,excellent)
plt.text(0.0,1.15,good)
plt.text(0.5,1.15,pas)
plt.savefig('./成绩分布.png')
plt.show()
