import pandas as pd
import string
import matplotlib.pyplot as plt
import random
from random import randint
from time import sleep 
import os

def COLORS():

    global ylw,end,blu,red
    blu = '\033[94m'
    ylw = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'

COLORS()

class Security:

    def Code_Maker():

        Numb1 = str(randint(1,3))
        Numb2 = str(randint(4,6))
        Numb3 = str(randint(7,9))

        String = string.ascii_letters
        Alfa = ''.join(random.sample(String, 3))
        Alfa = set(Alfa)
        Numbers = {Numb1,Numb2,Numb3}

        Final = (Alfa | Numbers )

        global Code

        Code=''
        for x in Final:
            Code +=x

        print(Code)


    def Code_Request():
        Speed = 1
        Counter = 0
        while Counter < 9:
            os.system('cls') 
            print(ylw,'Processing',Speed*'.',end)
            sleep(0.2)

            if Speed == 3:
                Speed = 0

            Speed +=1
            Counter +=1
        print(blu,'\n',27 * ' ','>>>> Welcome To the Program <<<<\n',end)

#______________________________________________________________________________________
data = pd.read_csv(r'C:\Users\Panta\Desktop\Global_Terrors.csv')                        # 1970_2017
data.rename(columns={"Target's Nationality":"Target Nationality"},inplace=True)         

def Attack_Years():                                                                     # 1

    ''' All Attacks From 1970_2017 ''' 

    Years = {}                                                                                    
    for i in data.index:
        Years[data['Year'].loc[i]] = Years.get(data['Year'].loc[i] , 0 ) + 1

    x = []
    for k,v in Years.items():
        x.append((k,v))
    x.sort()

    year = []
    No = []
    for i in x:
        year.append(i[0])
        No.append(i[1])

    plt.style.use('Solarize_Light2')
    plt.plot(year , No ,color=('red'))

    plt.fill_between(year,No,color='gray',)

    plt.title('All Attacks From 1970_2017')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.show()

#______________________________________________________________________________________
def Target_Nationality():                                                              # 2
                                                            
    ''' The 10 Most Attacked To Countries '''

    Success = {}
    Countries = {}
    for i in data.index:
        Countries[data['Target Nationality'].loc[i]] = Countries.get(data['Target Nationality'].loc[i] , 0 ) + 1

        if data['Success Rate'].loc[i] == 1:
            Success[data['Target Nationality'].loc[i]] = Success.get(data['Target Nationality'].loc[i] , 0 ) + 1

    x = []
    for k,v in Countries.items():
        if v > 4500:
            x.append((v,k))
    x.sort()

    Success_Attack = []
    for k,v in Success.items():
        if v > 4000:
            Success_Attack.append((v,k))
    Success_Attack.sort()


    Country = []
    No = []
    for i in x:
        Country.append(i[1])
        No.append(i[0])

    Country1 = []
    No1 = []
    for i in Success_Attack:
        No1.append(i[0])
        Country1.append(i[1])

    plt.style.use('ggplot')
    plt.barh(Country , No ,color='green',label='Failure Attack')
    plt.barh(Country,No1,color='red',label='Success Attack')
    plt.title('The 10 Most Attacked To Countries')
    plt.legend()
    plt.show()

#______________________________________________________________________________________
def Success_OR_Failure_Rate():                                                          # 3

    No = data.value_counts('Success Rate')
    Percent = data.value_counts('Success Rate',normalize=True)

    x = []
    for i in No:
        x.append(i)

    s = 0
    p = []
    for i in Percent:
        p.append(('%.2f'%(i*100)))
        t = i * 100
        if i > 0.50:
            print('Success Attack ::: ',x[s],' (','%.2f'%t,'%)')
        else:
            print('Failure Attack ::: ',x[s],'  (','%.2f'%t,'%)')
        s +=1

    X = ['Success','Failure']
    plt.style.use('ggplot')
    plt.bar(X , No ,color=('red','green'),label=(f'{p[0]}%',f'{p[1]}%'))
    plt.title('Success Or Failure Rate In Terror')
    plt.xlabel('Condition')
    plt.legend()
    plt.show()

#______________________________________________________________________________________
def Type_Of_Attack():                                                                  # 4

    Failure = {}
    Types = {}
    for i in data.index:
        Types[data['Type of Attack'].loc[i]] = Types.get(data['Type of Attack'].loc[i] , 0) + 1

        if data['Success Rate'].loc[i] == 1:
            Failure[data['Type of Attack'].loc[i]] = Failure.get(data['Type of Attack'].loc[i] , 0) + 1

    T = []
    for k,v in Types.items():
        for x,z in Failure.items():
            if k == x:
                T.append((v,z,k))

    T.sort(reverse=True)

    Total =[]
    Fail = []
    Tip  = []
    for i in T:
        Total.append(i[0])
        Fail.append(i[1])
        Tip.append(i[2])

    A = '.' * 30
    B = '.' * 38
    C = '.' * 39
    D = '.' * 15
    E = '.' * 16
    F = '.' * 46
    G = '.' * 34
    H = '.' * 4
    I = '.' * 46

    plt.style.use('Solarize_Light2')
    plt.barh(Tip , Total,color='orange',label=f'\
    Total Attack\n\n\
    {Tip[0]}{A}: {Total[0]}\n\
    {Tip[1]}{B}: {Total[1]}\n\
    {Tip[2]}{C}: {Total[2]}\n\
    {Tip[3]}{D}: {Total[3]}\n\
    {Tip[4]}{E}: {Total[4]}\n\
    {Tip[5]}{F}: {Total[5]}\n\
    {Tip[6]}{G}: {Total[6]}\n\
    {Tip[7]}{H}: {Total[7]}\n\
    {Tip[8]}{I}: {Total[8]}\n')

    plt.barh(Tip , Fail,color='r' , label=f'''
    Success\n\n\
    {Tip[0]}{A}: {Fail[0]}\n\
    {Tip[1]}{B}: {Fail[1]}\n\
    {Tip[2]}{C}: {Fail[2]}\n\
    {Tip[3]}{D}: {Fail[3]}\n\
    {Tip[4]}{E}: {Fail[4]}\n\
    {Tip[5]}{F}: {Fail[5]}\n\
    {Tip[6]}{G}: {Fail[6]}\n\
    {Tip[7]}{H}: {Fail[7]}\n\
    {Tip[8]}{I}: {Fail[8]}\n''')

    plt.title('Types Of Attack And Success Percent')
    plt.legend()
    plt.show()

#_____________________________________________________________________________________
def Worst_Condition_in_2014():                                                        # 5

    region = {}
    Type = {}
    WEAPON = {}
    for i in data.index:

        if data['Year'].loc[i] == 2014:     

            Type[data['Target Type'].loc[i]] = Type.get(data['Target Type'].loc[i] , 0) + 1
            region[data['Region'].loc[i]] = region.get(data['Region'].loc[i] , 0) + 1
            WEAPON[data['Weapon Type'].loc[i]] = WEAPON.get(data['Weapon Type'].loc[i] , 0) + 1

    Weapons = []
    for k,v in WEAPON.items():
        if v >= 18:
            Weapons.append((v,k))    
    Weapons.sort()
    Weapon = []
    No_W = []
    for i in Weapons:
        Weapon.append(i[1])
        No_W.append(i[0])


    TYPE = [] 
    for k,v in Type.items():
        if v > 200:
            TYPE.append((v,k))
    TYPE.sort()
    types = []
    No1 = []
    for i in TYPE:
        No1.append(i[0])
        types.append(i[1])


    Regions = []
    for k,v in region.items():
        Regions.append((v,k))
    Regions.sort()
    Region = []
    No = []
    for i in Regions: 
        No.append(i[0])
        Region.append(i[1])


    plt.style.use('Solarize_Light2')
    fig , (ax1,ax2) = plt.subplots(nrows=2 ,ncols=1 , figsize=(10,6)) 
    fig3,(ax3)=plt.subplots()
    
    ax3.fill_between(Weapon , No_W ,color = 'darkred')
    plt.title('Weapons Used In 2014')
    plt.grid(color='gray')
    plt.xlabel('Weapons')
    plt.ylabel('Amount')

    ax1.barh(Region , No,color ='c',label='12 Regions In War')
    ax2.barh(types  , No1,color='Hotpink',label='12 Injured Groups')

    ax1.set_ylabel('Regions')
    ax2.set_ylabel('Type')

    ax1.set_title('War Condition In 2014')
    plt.tight_layout()
    ax1.grid(color='gray') 
    ax2.grid(color='gray')
    ax1.legend()
    ax2.legend()
    plt.show()

#______________________________________________________________________________________
def Name_Of_Group():                                                                   # 6

    flt = data['Name of Group'] != 'Unknown'
    Data = data[flt]

    Sucs = {}
    Group = {}
    for i in Data.index:
        Group[Data['Name of Group'].loc[i]] = Group.get(Data['Name of Group'].loc[i] , 0 ) +1
        
        if data['Success Rate'].loc[i] == 1:
            Sucs[data['Name of Group'].loc[i]] = Sucs.get(data['Name of Group'].loc[i] , 0) + 1
    
    Total = []
    for k,v in Group.items():
        for K,V in Sucs.items():
            if (k == K) and (v > 880):
                Total.append((v,V,k))
    Total.sort(reverse=True)

    total = []
    success = []
    group = []
    for i in Total:
        total.append(i[0])
        success.append(i[1])
        group.append(i[2])

    plt.style.use('Solarize_Light2')
    plt.bar(group ,total,color='y',label='Total Terrors')
    plt.bar(group ,success,color='k',label='Success Terrors')
    plt.title('20-Terrorist Group By Max Homicide')
    plt.legend()
    plt.gcf().autofmt_xdate() 
    plt.show()

#______________________________________________________________________________________
Security.Code_Maker()
Password = input('Password: ')

while True:
    
    if Password == Code:        
        Security.Code_Request()

        print(20*' ','''1) All Attacks From 1970_2017 (Future Is Gloomy! )
                     2) The 10 Most Attacked To Countries
                     3) Success Or Failure Rate In Terror
                     4) Types of Attack
                     5) Condition in 2014 (Worst Year)
                     6) 20-Terrorist Group By Max Homicide
                     _______________
                     0) Exit\n\n''')

        Choose = int(input('Choose Number Analyzed Data: '))
        if Choose == 1:
            Attack_Years()

        elif Choose == 2:
            Target_Nationality()

        elif Choose == 3:
            Success_OR_Failure_Rate()

        elif Choose == 4:
            Type_Of_Attack()

        elif Choose == 5:
            Worst_Condition_in_2014()

        elif Choose == 6:
            Name_Of_Group()

        elif Choose == 0 :
            break

    else:
        print(red,"\n",30 * ' ',' Wrong Password !!!\n',end)
        break