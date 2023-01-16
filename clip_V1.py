def ele_dans_liste(element,liste):
    for chara in liste:
        if element in chara:
            return None
    return False
    
def dat(ville, data, month):
    indice = None
    temp = []
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
    print(dic_name[month], ':', data[indice][dic_indice[month]])
    a= "\nMinimum occurs in " + dic_inverse[str((data[indice]).index(str(mini)))] + " " + str(mini)
    b= "Maximum occurs in " + dic_inverse[str((data[indice]).index(str(maxi)))] + " " + str(maxi)
    c= "Average value " + str(moy)
    return(a,b,c)

def traitement(months, data):
    for month in months:
        a,b,c = dat (ele, data, month)
    print(a)
    print(b)
    print(c, '\n')
    
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
    print('---------------------------------------------')

    for ele in cities_v2:
        print("Data for", ele, '\n')

        if 'temp' in data_v2:
            print("Temperature:")
            traitement(months_v2, temperature)
                            
        if 'rain' in data_v2:
            print("Rainfall:")
            traitement(months_v2, rainfall)

        if 'sun' in data_v2:
            print("Sunshine:")
            traitement(months_v2, sunshine)

    print('---------------------------------------------')
                
    reponse = input("Do you want to continue (enter 'yes' or 'no')? ")
    while reponse not in ['yes','no']:
        reponse = input("Do you want to continue (enter 'yes' or 'no')? ")
