# PNS-CLIP

Final project

Introduction

The goal of this project is to develop a program named CLIP (CLImate Plotter) to display climate data about some US cities over the past year. This data is provided CSV  files, one file for one kind of data. The three data recorded in the files are, for each city, the average temperature (in degree Celsius), the average rainfall (in millimeters) and the average sunshine hours (in hours) per month, for each of the twelve months of the past year (2020). The program must allow the user to choose one or more cities (among all the available cities), one or more data (among temperature, rainfall and sunshine hours) and one or more months (among the twelve months of the year) to be displayed and plot on the screen. For each data, the program will display the raw data for each month plus the minimum and the maximum values, and also the average value over the given period of time, and will plot the corresponding data.

There are five versions of the project. You are to turn in the highest possible version.
File format
CLIP is handling three different kind of data, the temperature data, the rainfall data and the sunshine hours data. Each data is collected in a data file (a CSV file). The data files have all the same following format:

    the file is made of lines, one line for one city
    each line starts with a string, the name of one city, followed by exactly 12 double values, one value for each month. The double values appear in order (first value for January, second value for February, etc) and all the values are separated by a comma (',')

For example, in the file temperature.csv there is the following line:

Boston,-1.5,0.0,3.7,9.1,14.6,20.0,23.2,22.4,18.4,12.4,7.2,1.7

showing that for Boston (Massachusetts), the average temperature for January was -1.5 °C, the average temperature for February was 0.0 °C and so on until the average temperature for December which was 1.7 °C. Another example is in the file rainfall.csv with the line:

Nashville,95.3,100.1,104.4,101.6,139.7,105.2,92.2,80.3,86.6,77.2,109.5,107.7

showing that for Nashville (Tennessee), the average rainfall for January was 95.3 mm, the average rainfall for February was 100.1 mm and so on until the average rainfall for December which was 107.7 mm. You can assume that the files are correct and have exactly the same format (same number of lines, same cities and 1 string followed by 12 values on each line) but the order of appearance of the cities may differ for each file. For example, the first three lines in the file temperature.csv are:

Austin,10.8,12.8,16.5,20.6,24.7,27.9,29.4,29.8,26.7,21.8,16.1,11.4
Chicago,−3.7,−1.5,4.1 10.3 16.2, 21.7 24.3 23.4 19.3 12.4 5.5 −1.5
Boston,−1.5,0,3.7,9.1,14.6,20,23.2, 22.4 18.4 12.4 7.2 1.7

although the first three lines in the rainfall.csv file are:

    Washington 71.1 65.5 88.4 77.7 101.3 95.8 94.5 74.2 94.5 86.4 80.5 77.5
    Austin 56.4 51.3 70.1 53.1 112 110 47.8 59.7 75.9 98.6 75.2 61
    Boston 85.3 82.6 109.7 95 88.4 93.5 87.1 83.6 87.4 100.1 101.3 96

This file must be used to store the name of the cities in the program (inside an array), so we should not see any literal string llke "Austin", "Houston" or "Washington" in the program source code!

Version 1

CLIP allows the user to choose the cities, the data and the month she or he wants to display on the screen. After the program is started, a sequence of menus allow the user to choose:

    one or more cities among all the possible cities available
    one or more data among the 3 different kinds of data
    one or more months among the 12 possible months

Once the user selected these input information the program displays, for each city and for each data selected:

    a table showing the raw value of the data for the months selected
    the minimum value and the month where it occurs
    the maximum value and the month where it occurs
    the average of all the values over the selected months

For example, this is how to use CLIP to get information about the temperature and rainfall for Chicago for  March, April and May (user input is in bold):

Welcome to CLIP,  the CLImate Plotter

loading the data... done!

choose the cities: chicago
choose the data: temp(erature) rain(fall) sun(shine hours) OR all: temp rain
choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: mar apr may
-----------------------------------
Data for Chicago:

Temperature:
March     April     May       
4.10      10.30     16.20     
Minimum occurs in March: -3.7
Maximum occurs in May: 4.1
Average value: 10.20

Rainfall:
March     April     May       
69.30     92.20     104.60    
Minimum occurs in April: 49.0
Maximum occurs in May: 69.3
Average value: 88.70

To select the various information, the program display three menus in a row. In case the user input non legal value, CLIP issues a warning. For example, in the following :

    choose the cities: nashville antibes
    antibes is not a legal value (ignored)
    choose the data: temp(erature) rain(fall) sun(shine hours) OR all: temp pluie
    pluie is not a legal value (ignored)
    choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: jan feb mars
    mars is not a legal value (ignored)
    -----------------------------------
    Data for nashville:

    Temperature:
    January   February 
    3.40      5.70     
    Minimum occurs in January: 3.4
    Maximum occurs in February: 5.7
    Average value: 4.55

the user input a wrong city (antibes), a wrong data (pluie) and a wrong month (mars). Illegal values are ignored. If the user input only illegal values, CLIP asks for at least one legal input:

    choose the cities: nashville
    choose the data: temp(erature) rain(fall) sun(shine hours) OR all: tmp  pluie sunny
    tmp is not a legal value (ignored)
    pluie is not a legal value (ignored)
    sunny is not a legal value (ignored)
    please input at least one legal value
    choose the data: temp(erature) rain(fall) sun(shine hours) OR all:

It is possible to choose all the menu entries at once using the value 'all'. For example, the following display the all the available data (temperature, rainfall and sunshine hours) for the cities of Boston, Houston and Washington, for the twelve months: 

    choose the cities: boston houston
    choose the data: temp(erature) rain(fall) sun(shine hours) OR all: all
    choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: all
    -----------------------------------
    Data for Boston:

    Temperature:
    January   February  March     April     May       June      July      August    September October   November  December 
    -1.50     0.00      3.70      9.10      14.60     20.00     23.20     22.40     18.40     12.40     7.20      1.70     
    Minimum occurs in January: -1.5
    Maximum occurs in July: 23.2
    Average value: 10.93

    Rainfall:
    January   February  March     April     May       June      July      August    September October   November  December 
    85.30     82.60     109.70    95.00     88.40     93.50     87.10     83.60     87.40     100.10    101.30    96.00    
    Minimum occurs in February: 82.6
    Maximum occurs in March: 109.7
    Average value: 92.5

    Sunshine hours:
    January   February  March     April     May       June      July      August    September October   November  December 
    164.30    169.50    213.90    228.00    266.60    288.00    300.70    275.90    237.00    207.70    144.00    142.60   
    Minimum occurs in December: 142.6
    Maximum occurs in July: 300.7
    Average value: 219.85

    -----------------------------------
    Data for Houston:

    Temperature:
    January   February  March     April     May       June      July      August    September October   November  December 
    11.50     13.30     16.90     20.70     24.80     27.70     28.90     29.00     26.30     21.70     16.60     12.80    
    Minimum occurs in January: 11.5
    Maximum occurs in August: 29.0
    Average value: 20.85

    Rainfall:
    January   February  March     April     May       June      July      August    September October   November  December 
    85.90     81.30     86.60     84.10     129.30    150.60    96.30     95.50     104.60    144.80    110.20    95.00    
    Minimum occurs in February: 81.3
    Maximum occurs in June: 150.6
    Average value: 105.35

    Sunshine hours:
    January   February  March     April     May       June      July      August    September October   November  December 
    142.60    155.40    192.20    210.00    248.00    282.00    294.50    269.70    237.00    229.40    168.00    148.80   
    Minimum occurs in January: 142.6
    Maximum occurs in July: 294.5
    Average value: 214.8

After displaying information for a group of cities, data type and months, the program asks the user if she or he wants to display more data:

Do you want to continue (enter 'yes' or 'no')?

Again, the user must give a valid answer ('yes' or 'no') or else the program will ask again.

Version 2

In this new version, after having displayed the data the user asked for, the program can ask if she or he wants to store those results in a file. If the user answers 'yes', the program will prompt for a file name and write the result in that file. The saving-in-a-file operation should be proposed after the program displayed some data and just before asking the user for another display:

    .....

    Sunshine hours:
    January   February  March     April     May       June      July      August    September October   November  December 
    142.60    155.40    192.20    210.00    248.00    282.00    294.50    269.70    237.00    229.40    168.00    148.80   
    Minimum occurs in January: 142.6
    Maximum occurs in July: 294.5
    Average value: 214.8

    -----------------------------------------------------
    Do you want to save these results in a file (enter 'yes' or 'no')? yes
    Enter the file path: washington.txt
    Done.
    -----------------------------------------------------

    Do you want to continue (enter 'yes' or 'no')?

    To achieve this functionality, you are to produce the output result as a string. Then, your program can print the string on the screen and write it into a file. Notice that CLIP is smart enough to check if the file you want to save the result in already exists. In that case, CLIP asks the user if she/he wants to overwrite the file or to append the new result to the file:

    ....
    -----------------------------------------------------
    Do you want to save these results in a file (enter 'yes' or 'no')? yes
    Enter the file path: washington.txt
    This file exists. Do you want to update this file (enter 'yes' or 'no')? yes
    Done.
    -----------------------------------------------------

    If the user answers no, then the file is overwritten  with the new content, else the new content is appended at the end of the file. To test if a file exists you must import the module os.path:

    import os.path
    from os import path

    and then call the method exists on the path object:

    if path.exists(file):
          .....


Version 3

Version 3 is similar to version 2 and additionally the program is now able to plot some results. In this version CLIP is supposed to plot the data for a single city for a single data. Any attempt to plot more than one data for more more than one city should lead to a warning message. For example, the following is printing the results for rainfall data over the twelves months of Memphis and plot this data:

choose the cities: memphis
choose the data: temp(erature) rain(fall) sun(shine hours) OR all: rain
choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: all
-----------------------------------
Data for memphis:
Rainfall:
January   February  March     April     May       June      July      August    September October   November  December  
101.10    111.50    130.80    139.70    133.10    92.20     116.60    73.20     78.50     101.10    139.40    145.80    
Minimum occurs in August: 73.2
Maximum occurs in December: 145.8
Average value: 113.58

The resulting plot is:

single plot

The plot should occurs right after the information have been printing on the screen. The program should block on the plot, and to be able to move to the next step (the question "Do you want to continue (enter 'yes' or 'no')?") the user must kill the plot window. Of course, if the user select only a few months, the plot will work accordingly. For example, the following should the temperature information for January, February, March, April, May and June for Phoenix:

choose the cities: phoenix
choose the data: temp(erature) rain(fall) sun(shine hours) OR all: temp
choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: jan feb mar apr may jun
-----------------------------------
Data for phoenix:
Temperature:
January   February  March     April     May       June      
13.60     15.40     18.50     22.70     27.80     32.70     
Minimum occurs in January: 13.6
Maximum occurs in June: 32.7
Average value: 21.78

The resulting plot is:

single plot

If the user asks for information for more than one city and/or for more than one data, there will be no plot but a warning message

choose the cities: boston houston
choose the data: temp(erature) rain(fall) sun(shine hours) OR all: all
choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: all
-----------------------------------
Data for Boston:
...
warning: no plot available


Version 4
Version 4 is similar to version 3 but now it is possible to plot more than one city for only one data. For example, the following is printing the results for rainfall data over the twelves months of Boston and Chicago and plot this data:

choose the cities: boston chicago
choose the data: temp(erature) rain(fall) sun(shine hours) OR all: rain
choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: all
-----------------------------------
Data for Boston:
Rainfall:
January   February  March     April     May       June      July      August    September October   November  December  
85.30     82.60     109.70    95.00     88.40     93.50     87.10     83.60     87.40     100.10    101.30    96.00     
Minimum occurs in February: 82.6
Maximum occurs in March: 109.7
Average value: 92.5
-----------------------------------
Data for Chicago:
Rainfall:
January   February  March     April     May       June      July      August    September October   November  December  
52.10     49.00     69.30     92.20     104.60    103.10    101.90    101.30    84.10     82.00     86.90     65.30     
Minimum occurs in February: 49.0
Maximum occurs in May: 104.6
Average value: 82.65

The resulting plot is:

multiple plots

Notice that the plots for different cities appear in different colors. Again, if the user asks for information for more than one data, there will be no plot but a warning message.

Version 5

Version 5 is similar to version 4 but now it is possible to plot multiple data information for multiple cities for the selected months. When plotting multiple data, the plots are stacking into a unique figure. For example, the following is printing the results for rainfall and sunshine hours data over the twelves months of Austin, Houston and Indianapolis and plot this data:

choose the cities: austin houston indianapolis
choose the data: temp(erature) rain(fall) sun(shine hours) OR all: rain sun
choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: all
-----------------------------------
Data for Austin:
Rainfall:
January   February  March     April     May       June      July      August    September October   November  December  
56.40     51.30     70.10     53.10     112.00    110.00    47.80     59.70     75.90     98.60     75.20     61.00     
Minimum occurs in July: 47.8
Maximum occurs in May: 112.0
Average value: 72.59
Sunshine hours:
January   February  March     April     May       June      July      August    September October   November  December  
164.30    169.50    204.60    207.00    226.30    285.00    316.20    297.60    234.00    217.00    168.00    155.00    
Minimum occurs in December: 155.0
Maximum occurs in July: 316.2
Average value: 220.38
-----------------------------------
Data for Houston:
Rainfall:
January   February  March     April     May       June      July      August    September October   November  December  
85.90     81.30     86.60     84.10     129.30    150.60    96.30     95.50     104.60    144.80    110.20    95.00     
Minimum occurs in February: 81.3
Maximum occurs in June: 150.6
Average value: 105.35
Sunshine hours:
January   February  March     April     May       June      July      August    September October   November  December  
142.60    155.40    192.20    210.00    248.00    282.00    294.50    269.70    237.00    229.40    168.00    148.80    
Minimum occurs in January: 142.6
Maximum occurs in July: 294.5
Average value: 214.8
-----------------------------------
Data for Indianapolis:
Rainfall:
January   February  March     April     May       June      July      August    September October   November  December  
67.60     58.90     90.40     96.50     128.30    107.70    115.60    79.50     79.20     79.20     94.00     80.30     
Minimum occurs in February: 58.9
Maximum occurs in May: 128.3
Average value: 89.77
Sunshine hours:
January   February  March     April     May       June      July      August    September October   November  December  
132.10    145.70    178.30    214.80    264.70    287.20    295.20    273.70    232.60    196.60    117.10    102.40    
Minimum occurs in December: 102.4
Maximum occurs in July: 295.2
Average value: 203.37

The resulting plot is:

multiple plots

Notice that each subplot has the data name as a title (Rainfall and Sunshine hours).
Coding hints

Using dictionary

The easiest way to handle the data in the project is to read the entire content of the CSV files at the beginning of the program and to store this content in a dictionary. The dictionary data structure can match the structure of the query path to fetch the data (cities first, then data and finally months). We strongly recommend that you store the content of the files in a dictionary of the form { city: { data1: [ values ], data2: [ values ], ...), ...} , where 'city' is the name of a city, 'data*' the code for a data (like 'temp', 'rain' or 'sun') and [ values ] a list a twelves float numbers (i.e. the values of the data for the twelves months). This dictionary must be created right at the beginning of the program
Storing the results in a file

In the version 2 of the project, your program must be able to store the results appearing on the screen in a text file. To achieve that in an easy way, you should first produce the result as a (rather) big string (with newline characters inside), and then print that string on the screen and optionally store (write) the string in a text file. Writing a string in a text file can be done simply by using the write method on a file object (opened for writing) like:

stringResult = ...
outfile = open('myfile.txt','w')
outfile.write(stringResult)
outfile.close()

Limit on the number of cities to plot

In versions 4 and 5 of the project, you should put a limit on the number of cities that can be plotted for the same data. A maximum of 4 cities should be allowed to be plotted simultaneously. In case the user submit more than 4 cities, the program should issue a warning message and should not plot anything.
Plotting multiple data

To plot multiple data on the same figure, you can use the subplots method on a pyplot object. You can find many examples and tutorials online about how to use Matplotlib, lor simply on the official Matplotlib documentation: Creating multiple subplots using plt.subplots.
Programming style

You should focus on the quality of your code and try as much as possible to use the best data and control structures. You must try to use the Python idioms we used in class and factorize the code when possible (like for the menus). To make the development of your code easier, you should use functions. As a guideline, my solution (for the version 5)  has 113 lines of code and 11 functions apart from the main script.
