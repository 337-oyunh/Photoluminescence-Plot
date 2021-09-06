#to read data
import pandas as pd

#plot tool
import matplotlib as mpl
import matplotlib.pyplot as plt

print('Hi :)')

# Change the plot setting below
line_width = 7.0 #I prefer 7.0
line_style = '-' #I prefer -
figsize_x = 60 #I prefer 60
figsize_y = 30 #I prefer 30
xaxis = 'Wavelength (nm)'
yaxis = 'Intensity (a.u.)'

filename1 = 'C:/Users/이윤호/Desktop/학부인턴/1번 테이블/20210830/0deg row 218 60 exposure center 700 150 800 grating slit.csv' #file directory and name
column_number1 = 218 #row
sample_name1 = 'LHC' #polarization

filename2 = 'C:/Users/이윤호/Desktop/학부인턴/1번 테이블/20210830/45deg row 218 60 exposure center 700 150 800 grating slit.csv'
column_number2 = 225
sample_name2 = 'RHC'

sample_name3 = 'Polarization'

df1  = pd.read_csv(filename1)
df2  = pd.read_csv(filename2)

print(df1.columns)
print(df2.columns)

df1 = df1[ df1.iloc[:,2] > 600.0 ] #interested region
df1 = df1[ df1.iloc[:,2] < 900.0 ] #interested region
df2 = df2[ df2.iloc[:,2] > 600.0 ]
df2 = df2[ df2.iloc[:,2] < 900.0 ]

df1 = df1.loc[(df1['0.1'] == column_number1)].iloc[:,2:4]
df2 = df2.loc[(df2['0.1'] == column_number2)].iloc[:,2:4]

df1.reset_index(drop=True, inplace=True) #resetting index for calculation
df2.reset_index(drop=True, inplace=True)

df1 = df1.rename(columns={df1.columns[0]: '0', df1.columns[1]: '1'})
df2 = df2.rename(columns={df2.columns[0]: '0', df2.columns[1]: '1'})
df3  = pd.DataFrame(columns=["1", "2"]) #creating new dataframe of polarization


df3["1"] = df2["0"]
df3["2"] = (df1["1"] - df2["1"]) / (df1["1"] + df2["1"]) #the calculation

df1 = df1.rename(columns={df1.columns[0]: 'Wavelength (nm)', df1.columns[1]: sample_name1})
df2 = df2.rename(columns={df2.columns[0]: 'Wavelength (nm)', df2.columns[1]: sample_name2})
df3 = df3.rename(columns={df3.columns[0]: 'Wavelength (nm)', df3.columns[1]: sample_name3})

fig1 = df1.plot(x=df1.columns[0], y=df1.columns[1], color='red', linewidth = line_width)
fig2 = df2.plot(x=df2.columns[0], y=df2.columns[1], color='green', secondary_y = False, ax=fig1, linewidth = line_width)
fig3 = df3.plot(x=df3.columns[0], y=df3.columns[1], color='skyblue', secondary_y = True, ax=fig2,
linestyle = line_style, figsize = (figsize_x, figsize_y), xlabel= xaxis, ylabel= yaxis, linewidth = 3.0)

plt.show()