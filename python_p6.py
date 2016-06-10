# -*- coding: utf-8 -*- #处理汉（双字节字符）
import matplotlib.pyplot as plt #引用matplotlib绘图，matplotlib的pyplot子库提供了和matlab类似的绘图API，方便用户快速绘制2D图表。

import xlrd #python语言中读取Excel的扩展工具
import numpy as np #科学计算工具
import math #数学函数库
from  statistics import mean,stdev,pstdev,variance,pvariance #引入平均数、标准差、样本总体的标准偏差、方差、样本总体的标准偏差

from prettytable import PrettyTable #python通过prettytable模块可以将输出内容如表格方式整齐的输出。
excel = xlrd.open_workbook('p6_data.xlsx')
sheet = excel.sheets()[0]     #获取第一个sheet   
xx=[]
yy=[]
xxdata=[]
yydata=[]

for i in range(0,4): #获取数据存放在xx，yy列表中
    xx.append(sheet.col_values(2*i))
    yy.append(sheet.col_values(2*i+1))
def setData(x,y):
    xsta={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None} #x的数据处理，将各个数放入字典中
    ysta={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None} #y的数据处理，将各个数放入字典中

    xsta['avg']=mean(x) #x平均数
    ysta['avg']=mean(y) #y平均数

    xsta['stdev']=stdev(x) #x标准差
    ysta['stdev']=stdev(y) #y标准差

    xsta['pstdev']=pstdev(x) #x样本总体的标准偏差
    ysta['pstdev']=pstdev(y) #x样本总体的标准偏差

    xsta['var']=variance(x) #x方差
    ysta['var']=variance(y) #y方差

    xsta['pvar']=pvariance(x) #x样本总体的方差
    ysta['pvar']=pvariance(y) #y样本总体的方差

  

    return  xsta,ysta #返回各数
def fitData(x,y):
    #find linear fit 线性拟合
    a,b = np.polyfit(x,y,1) #返回一次项和常数项系数
    predictedY = a*np.array(x) + b #拟合的线性函数
    return a,b,predictedY #返回拟合结果
def processing_data():
    datax=[]
    datay=[]
    for i in range(0,4):
        aa,bb=setData(xx[i],yy[i])
        datax.append(aa)
        datay.append(bb)
    return datax,datay
def processing_table():
    table = PrettyTable(["data set","x-avg", "x-std", "x-pstd", "x-var","x-pvar","y-avg", "y-std", "y-pstd", "y-var","y-pvar"])
    table.align= "l" # right align
    table.padding_width = 1 # One space between column edges and contents (default)
    for i in range(0,4):
        table.add_row([i,xxdata[i]['avg'],xxdata[i]['stdev'],xxdata[i]['pstdev'],xxdata[i]['var'],xxdata[i]['pvar'],
                         yydata[i]['avg'],yydata[i]['stdev'],yydata[i]['pstdev'],yydata[i]['var'],yydata[i]['pvar']])
    print(table)

def plotData(x,y,a,b, predictedY):
    plt.plot(x,y, 'bo')
    plt.xlabel('x') #设置X轴的文字
    plt.ylabel('y') #设置y轴的文字

    plt.plot(x,predictedY,
               label = 'Y by\nlinear fit, y = '
               + str(round(a, 6))+'*x+'+str(round(b, 6)),color="black") #画拟合曲线图

    plt.legend(loc = 'best') #添加图例，loc告诉matplotlib要将图例放在哪，“best”是不错的选择，因为它会选择最不碍事的位置。
def processing_plot():

    fig=plt.figure(figsize=(12.0,8.0))#图大小
    fig.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)#图间距

    figcol=2
    figrow=2

    for i in range(0,4):
        aa,bb,cc=fitData(xx[i],yy[i])
        fig.add_subplot(figrow, figcol,i+1)#分别加图、画图
        plotData(xx[i],yy[i],aa,bb,cc)

    plt.show()#显示

xxdata,yydata=processing_data()
processing_table()
processing_plot()

