import os.path
from os import path
import matplotlib.pyplot as plt

def ele_dans_liste(element,liste):
    for chara in liste:
        if element in chara:
            return None
    return False
    
def dat(ville, data, months):
    indice = None
    temp = []
    a = []
    abscisses = []
    ordonnees = []
    for chara in data:
        if ville in chara:
            indice = data.index(chara)
            break
    for i in range(1,len(data[indice])):
        try:
            temp += [int(data[indice][i])]
        except:
            temp += [float(data[indice][i])]
    mini = min(temp)
    maxi = max(temp)
    moy = round(sum(temp)/len(temp),2)
    b= " \nMinimum occurs in " + dic_inverse[str((data[indice]).index(str(mini)))] + " " + str(mini)
    c= "Maximum occurs in " + dic_inverse[str((data[indice]).index(str(maxi)))] + " " + str(maxi)
    d= "Average value " + str(moy) +'\n'
    for month in months:
        a += [dic_name[month] + ':' + data[indice][dic_indice[month]]]
        if not (len(data_v2)>1) and len(cities_v2)<=4:
            abscisses += [month]
            ordonnees += [float(data[indice][dic_indice[month]])]
    if abscisses != []:
        return (a,b,c,d,abscisses,ordonnees)
    return(a,b,c,d)

def graph (abscisses, ordonnees, title, city):
    plt.plot(abscisses, ordonnees, label = city)
    plt.title(title)
    plt.legend()
    
# main script starts here

print('Welcome to CLIP, the CLImate Plotter')

temp = open("temperature.csv", 'r')
temperature = [line.strip().split(",") for line in temp]
temp.close()

rain = open("rainfall.csv", 'r')
rainfall = [line.strip().split(",") for line in rain]
rain.close()

sun = open("sunshine.csv", 'r')
sunshine = [line.strip().split(",") for line in sun]
sun.close()

mon = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

print('loading the data... done!')

reponse = 'yes'

while reponse =='yes':
    cities_v2 = []
    while cities_v2 == []:
        cities = input('choose the cities: ')
        cities = cities.split(" ")
        for ele in cities:
            if ele_dans_liste(ele,temperature) == False or ele in cities_v2:
                   print(ele, 'is not a legal value or already in the list (ignored)')
            else :
                cities_v2 += [ele]
        if cities_v2 == []:
            print('please input at least one legal value')
            
    data_v2 = []
    while data_v2 == []:
        data = input('choose the data: temp(erature) rain(fall) sun(shine hours) OR all: ')
        data = data.split(" ")
        for ele in data:
            if ele not in ['temp', 'rain', 'sun', 'all'] or ele in data_v2:
                   print(ele, 'is not a legal value or already in the list (ignored)')
            else :
                data_v2 += [ele]
        if data_v2 == []:
            print('please input at least one legal value')

    monthsv2 = []
    while monthsv2 == []:
        months = input('choose the months: jan(uary) feb(ruary) ... dec(ember) OR all: ')
        months = months.split(" ")
        for ele in months:
            if ele not in ( mon + ['all']) or ele in monthsv2:
                   print(ele, 'is not a legal value or already in the list (ignored)')
            else :
                monthsv2 += [ele]
        if monthsv2 == []:
            print('please input at least one legal value')

    if 'all' in data_v2:
        data_v2 = ['temp', 'rain', 'sun']

    if 'all' in monthsv2:
        months_v2 = mon
    else:
        months_v2 = []
        for month in mon:
            if month in monthsv2:
                months_v2 += [month]

    dic_indice = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
    dic_inverse = {'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}
    dic_name = {'jan': "January", 'feb': "February", 'mar': "March", 'apr':"April", 'may':"May", 'jun': "June", 'jul': "July", 'aug':"August", 'sep':"September", 'oct':"October", 'nov':"November", 'dec':"December"}
    dic_data_name = {'temp': "Temperature", 'rain': "Rainfall", 'sun': "Sunshine hours"}
    dic_data = {'temp': temperature, 'rain': rainfall, 'sun': sunshine}

    print('---------------------------------------------')

    res = []
    for ele in cities_v2:
        res += ["Data for " + ele + '\n']

        if not (len(data_v2)>1) and len(cities_v2)<=4:
            res += [dic_data_name[data_v2[0]] + ":\n"]
            a,b,c,d,abscisse,ordonnee = dat (ele, dic_data[data_v2[0]], months_v2)
            res += a + [b] + [c] + [d]
            graph(abscisse, ordonnee, dic_data_name[data_v2[0]], ele)
        else:
            for c in data_v2:
                res += [dic_data_name[c] + ": \n"]
                a,b,c,d = dat (ele, dic_data[c], months_v2)
                res += a + [b] + [c] + [d]

        res += ['---------------------------------------------']
    for ele in res:
        print(ele)

    if not(len(data_v2)>1) and len(cities_v2)<=4:
        print("The resulting plot is:")
        plt.show()
        plt.close()
    else:
        res += ['warning : no plot available']
        print(res[-1])

    save = input("Do you want to save these results in a file (enter 'yes' or 'no')? ")
    while save not in ['yes','no']:
        save = input("Do you want to save these results in a file (enter 'yes' or 'no')? ")

    if save == 'yes':
        file = input('Enter the file path (with file extension) : ')
        if path.exists(file):
            save = input("This file exists. Do you want to update this file (enter 'yes' or 'no')? ")
            while save not in ['yes','no']:
                save = input("This file exists. Do you want to update this file (enter 'yes' or 'no')? ")
            if save == 'yes':
                infile = open(file, 'a')
                for line in res:
                    infile.write(line + '\n')
                infile.close()
            else:
                infile = open(file, 'w')
                for line in res:
                    infile.write(line + '\n')
                infile.close()
        else:
            infile = open(file, 'w')
            for line in res:
                infile.write(line +'\n')
            infile.close()        

        print("Done.")

        print('---------------------------------------------')
    
    reponse = input("Do you want to continue (enter 'yes' or 'no')? ")
    while reponse not in ['yes','no']:
        reponse = input("Do you want to continue (enter 'yes' or 'no')? ")
