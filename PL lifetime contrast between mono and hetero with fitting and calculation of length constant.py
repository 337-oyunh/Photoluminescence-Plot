#to read data
import pandas as pd

#plot tool
import matplotlib as mpl
import matplotlib.pyplot as plt

#fitting tool
import numpy as np
from numpy import exp
from scipy.optimize import curve_fit

#this is the code for plotting spectrometer datas
print('This is the code for plotting spectrometer datas.')

# Change the plot setting below
line_width = 7.0 #I prefer 7.0
line_style = '' #I prefer -
marker_type = '.'
figsize_x = 60 #I prefer 60
figsize_y = 30 #I prefer 30
xaxis = 'Length (a.u.)'
yaxis = 'Counts (a.u.)'

#plot file list
filename1 = 'C:/Users/이윤호/Desktop/21진장/WSWSE 195.csv'
column_number1 = 620.3646570035348
filename2 = 'C:/Users/이윤호/Desktop/21진장/WSWSE 195.csv'
column_number2 = 767.5592787768918
filename3 = 'C:/Users/이윤호/Desktop/21진장/WSWSE 195.csv'
column_number3 = 842.758584950299


#plot data extraction
df1  = pd.read_csv(filename1)
df1 = df1.rename(columns={df1.columns[0]: '0', df1.columns[1]: '1', df1.columns[2]: '2', df1.columns[3]: '3'})
df1 = df1.loc[(df1['2'] == column_number1)].iloc[:]
df1 = df1.iloc[199:311].iloc[:]
df1.reset_index(drop=True, inplace=True)
df1['1'] = df1.index

df2 = pd.read_csv(filename2)
df2 = df2.rename(columns={df2.columns[0]: '0', df2.columns[1]: '1', df2.columns[2]: '2', df2.columns[3]: '3'})
df2 = df2.loc[(df2['2'] == column_number2)].iloc[:]
df2 = df2.iloc[199:311].iloc[:]
df2.reset_index(drop=True, inplace=True)
df2['1'] = df2.index

df3  = pd.read_csv(filename3)
df3 = df3.rename(columns={df3.columns[0]: '0', df3.columns[1]: '1', df3.columns[2]: '2', df3.columns[3]: '3'})
df3 = df3.loc[(df3['2'] == column_number3)].iloc[:]
df3 = df3.iloc[188:300].iloc[:]
df3.reset_index(drop=True, inplace=True)
df3['1'] = df3.index

#fitting setting
def exp1(x1, a1, b1, c1,):
    return a1 * exp(-x1 / b1) + c1

x1 = df1['1']
y1 = df1['3']

def exp2(x2, a2, b2, c2,):
    return a2 * exp(-x2 / b2) + c2

x2 = df2['1']
y2 = df2['3']

def exp3(x3, a3, b3, c3,):
    return a3 * exp(-x3 / b3) + c3

x3 = df3['1']
y3 = df3['3']

const1, pcov1 = curve_fit(exp1, x1, y1, [15000.0, 10000.0, 0.0])
const2, pcov2 = curve_fit(exp2, x2, y2, [15000.0, 10000.0, 0.0])
const3, pcov3 = curve_fit(exp3, x3, y3, [1000.0, 1000.0, 0.0])

#plot figure setting
fig1 = df1.plot(x=df1.columns[1], y=df1.columns[3], label = 'WS2 original', linestyle = line_style, color = 'blue', marker = marker_type)
fit1 = plt.plot(x1, exp1(x1, *const1), color = 'skyblue', label = 'WS2 fitting')

fig2 = df2.plot(x=df2.columns[1], y=df2.columns[3], label = 'WSe2 original', linestyle = line_style, color = 'green', marker = marker_type, ax = fig1)
fit2 = plt.plot(x2, exp2(x2, *const2), color = 'lightgreen', label = 'WSe2 fitting')

fig3 = df3.plot(x=df3.columns[1], y=df3.columns[3], label = 'HS original', linestyle = line_style, color = 'red', marker = marker_type,
ax = fig2, secondary_y = True, figsize=(figsize_x, figsize_y))
fit3 = plt.plot(x3, exp3(x3, *const3), 'lightcoral', label = 'HS fitting')

print("WS2 : " + str(const1[1]) +  " rows, " + "WSe2 : " + str(const2[1]) + " rows, " + " HS : " + str(const3[1]) + " rows")

plt.show()