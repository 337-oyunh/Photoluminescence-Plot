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

number_of_plot = int(input('How many files do you want to plot together at the same time : '))

if number_of_plot == 1:
    #this is the code for plotting 1 graphs
    print("This is the code for plotting only 1 graph.")

    filename = input('Write file directory (ex) C:/Users/... : ')
    column_number = int(input('The column you want to plot : '))

    df  = pd.read_csv(filename)
    df = df.loc[(df['0.1'] == column_number)].iloc[:,2:4]
    #print(df.columns)

    sample_name = input('Your sample name :')

    df = df.rename(columns={df.columns[0]: 'Wavelength', df.columns[1]: sample_name})
    df.plot(x=df.columns[0], y=df.columns[1], color='red', linestyle=line_style, figsize=(figsize_x, figsize_y), linewidth = line_width, xlabel= xaxis, ylabel= yaxis)



if number_of_plot == 2:
    #this is the code for plotting 2 graphs
    print("this is the code for plotting 2 graphs")

    filename1 = input('Write file directory1 (ex) C:/Users/... : ')
    column_number1 = int(input('The column you want to plot : '))
    sample_name1 = input('Your sample name1 :')

    filename2 = input('Write file directory2 (ex) C:/Users/... : ')
    column_number2 = int(input('The column you want to plot : '))
    sample_name2 = input('Your sample name2 :')

    df1  = pd.read_csv(filename1)
    df2  = pd.read_csv(filename2)

    df1 = df1.loc[(df1['0.1'] == column_number1)].iloc[:,2:4]
    df2 = df2.loc[(df2['0.1'] == column_number2)].iloc[:,2:4]

    df1 = df1.rename(columns={df1.columns[0]: 'Wavelength (nm)', df1.columns[1]: sample_name1})
    df2 = df2.rename(columns={df2.columns[0]: 'Wavelength (nm)', df2.columns[1]: sample_name2})

    fig1 = df1.plot(x=df1.columns[0], y=df1.columns[1], color='red', linewidth = line_width)
    fig2 = df2.plot(x=df2.columns[0], y=df2.columns[1], color='green', secondary_y = False, ax=fig1,
    linestyle = line_style, figsize = (figsize_x, figsize_y), linewidth = line_width, xlabel= xaxis, ylabel= yaxis)



if number_of_plot == 3:
    #this is the code for plotting 3 graphs
    print("this is the code for plotting 3 graphs")

    filename1 = input('Write file directory1 (ex) C:/Users/... : ')
    column_number1 = int(input('The column you want to plot : '))
    sample_name1 = input('Your sample1 name :')

    filename2 = input('Write file directory2 (ex) C:/Users/... : ')
    column_number2 = int(input('The column you want to plot : '))
    sample_name2 = input('Your sample2 name :')

    filename3 = input('Write file directory3 (ex) C:/Users/... : ')
    column_number3 = int(input('The column you want to plot : '))
    sample_name3 = input('Your sample3 name :')

    df1  = pd.read_csv(filename1)
    df2  = pd.read_csv(filename2)
    df3  = pd.read_csv(filename3)

    df1 = df1.loc[(df1['0.1'] == column_number1)].iloc[:,2:4]
    df2 = df2.loc[(df2['0.1'] == column_number2)].iloc[:,2:4]
    df3 = df3.loc[(df3['0.1'] == column_number3)].iloc[:,2:4]

    df1 = df1.rename(columns={df1.columns[0]: 'Wavelength', df1.columns[1]: sample_name1})
    df2 = df2.rename(columns={df2.columns[0]: 'Wavelength', df2.columns[1]: sample_name2})
    df3 = df3.rename(columns={df3.columns[0]: 'Wavelength', df3.columns[1]: sample_name3})

    fig1 = df1.plot(x=df1.columns[0], y=df1.columns[1], color='red', linewidth = line_width)
    fig2 = df2.plot(x=df2.columns[0], y=df2.columns[1], color='green', secondary_y = False, ax=fig1, linewidth = line_width)
    fig3 = df3.plot(x=df3.columns[0], y=df3.columns[1], color='blue', secondary_y = True, ax=fig2,
    linestyle = line_style, figsize = (figsize_x, figsize_y), linewidth = line_width, xlabel= xaxis, ylabel= yaxis)

plt.show()