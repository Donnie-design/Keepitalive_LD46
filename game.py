# This game is played completly in the commandline.
# I am very aware that there are bugs and balancing issues.
# This is how far i could get in 48H of Ludum Dare. Please don't be to harsh.

# IMPORTS

import os
import time
import random

# GLOBAL VARIABLES

name = "something"
day = 0
pop_list = []
food = 10000
houses = 0
fields = 0
pregnancies = []
females = 0

# ROUTINES

def days_to_years(days):
    years = days/365

def adding_colonists(): #crates random Colonists
    global pop_list
    global females
    count = 0

    tmp = []

    if len(pop_list) == 0:
        for i in range(16):
            tmp.append(str("c"+str(i)))
            if random_gender() == 0:
                tmp.append(0)
                females = females+1
                tmp.append(random_name_girl())
            else:
                tmp.append(1)
                tmp.append(random_name_male())
            tmp.append(random_age())
            pop_list.append(tmp[:])
            del tmp[:]

def add_new_colonist():
    global pop_list
    global females

    tmp = []

    tmp.append(str("c"+str(len(pop_list))))
    if random_gender() == 0:
        tmp.append(0)
        females = females+1
        tmp.append(random_name_girl())
    else:
        tmp.append(1)
        tmp.append(random_name_male())
    tmp.append(random_age())
    pop_list.append(tmp[:])

def random_gender():
    if random.randint(0,10) <= 5:
        female = "female"
        return 0
    else:
        male = "male"
        return 1

def random_age():
    return random.randint(6000,7000)

def random_name_girl():
        names_female  =  ['Anna', 'Bella','Emilia','Frederike','Ines','Joanna','Michelle','Norma','Sammy','Tammy','Uma','Vanessa','Wanda','Xanda','Yanda','Zenzi']
        return random.choice(names_female)

def random_name_male():
        names_male = ['Christian','Dick','Gill','Huck','Karl','Lamar','Otto','Philipp','Q - Just Q','Rudolph']
        return random.choice(names_male)

def check_for_pregnancy():
    global pregnancies
    global food

    if len(pregnancies) <= females:
        for i in range(1, females):
            if random.randint(1,100) <=1:
                pregnancies.append(int(280))

    food = food-(len(pregnancies)*3)

    count=0
    for i in pregnancies:
        pregnancies[count] = i-1
        count = count+1

    for i in pregnancies:
        if int(i) <= 0:
            add_new_colonist()
            del pregnancies[0]

def counting_days():
    global day
    global food

    check_for_pregnancy()
    food = food-(len(pop_list)*3)
    day = day+1

def month():
    modulo = day%365
    int(modulo/30.4)
    if modulo == 0:
        return "May"
    elif modulo == 1:
        return "June"
    elif modulo == 2:
        return "July"
    elif modulo == 3:
        return "August"
    elif modulo == 4:
        return "September"
    elif modulo == 5:
        return "October"
    elif modulo == 6:
        return "November"
    elif modulo == 7:
        return "December"
    elif modulo == 8:
        return "Januar"
    elif modulo == 9:
        return "Februar"
    elif modulo == 10:
        return "March"
    elif modulo == 11:
        return "April"

def harvesting():
    global food

    tmp = 0

    for i in range(1, fields):
        tmp = tmp+random.randint(30,100)*fields

    print("Harvesting-Day!!!!!!!",tmp," was harvested.")

    food = food+tmp

def harvest():
    harvest = 0
    harvest = 365-(day%365)
    if day%365 == 0:
        harvesting()
        return "Harvesting Day!!!"
    return int(harvest)

def set_up_sign():
    print("                                                                 Pregnant:",pregnancies,"                        ")
    print("                                                                 Month:",month(),"                        ") #2
    print("                                                                 Fields:",fields,"                        ")
    print("                                                                 Harvest:",harvest(),"                        ") #4
    print("         |----------------------|                                                        ")
    print("         |°",'{:^18}'.format(name.upper()),"°|                                           ") #6
    print("         |                      |                                                        ")
    print("         |°       Pop.:",'{:^6}'.format(len(pop_list)),"°|                                         ") #8
    print("         |----------------------|                                                        ")
    print("                    ||                                                                   ") #10
    print("~~~~~~~~~~~~~~~~~~~~||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DAY:",'{:^6}'.format(day),"~~~Year:",int(day/365),"~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

def input_name():
    global name
    name = input("What will your colony be named? ")
    print("")
    print(name,"sounds wonderful.")
    time.sleep(2)
    clear()
    return name

def clear():
    os.system('cls')

def kill():
    del pop_list[0]
    print("One of your colonists died. Are you happy now? You should keep them alive!")

def check_food():
    global food
    global pop_list

    if food < 0:
        print("You are going to starve.")
        for i in range(random.randint(1,3)):
            kill()
    if len(pop_list) != 0:
        print("There is:",food,". The food is going to last:", int(food/(len(pop_list)*3)))
    else:
        clear()
        print("You should have kept them alive. You failed.... Donnerparty.... oh those memories....")
        exit()


def check_houses():
    global houses

    if houses == 0:
        print("You should build some houses.", int(len(pop_list)/2), "should be build.")
        if day > 90:
            kill()
    elif (len(pop_list)/2) >= houses:
        print("You should build some houses.", int((len(pop_list)/2)-houses), "should be build.")
        if day > 90:
            kill()
    elif (len(pop_list)/2) <= houses:
        print("There are enough houses.")

def build_house():
    global houses

    for i in range(0,7):
        counting_days()

    houses = houses+1

def make_field():
    global fields

    for i in range(1,21):
        counting_days()

    fields = fields +1

def go_hunt():
    global food

    for i in pop_list:
        food = food+(random.randint(2,7))

def check_population():
    if len(pop_list) <= 0:
        clear()
        print("You should have kept them alive. You failed.... Donnerparty.... oh those memories....")
        exit()

def main():
    counting_days()
    clear()
    set_up_sign()
    check_food()
    check_houses()
    print("")
    print("1: Build a house! 2: Make a field. 3: Let the group go hunting. 4: Hunting for a month!")
    check_population()
    x = eval(input("What are you going to do?")) #Menue einfügen
    if x == 1:
        print("They Build a house")
        build_house()
        main()
    elif x == 2:
        print("They make a field")
        make_field()
        main()
    elif x == 3:
        print("They hunt all the freaking deers,....")
        go_hunt()
        main()
    elif x == 4:
        print("Kill all that damn deer you can find. Slaughter them.")
        for i in range(0,30):
            go_hunt()
            counting_days()
        main()


def intro():
    clear()
    adding_colonists()
    print("Warning: May contain very dark humor. If Bambi is a trigger for you: consider yourself as warned.")
    print("")
    print("")
    print("You went out there in the wild. Crossed wild and unknown territory. Withstood harsh climate....")
    #time.sleep(2)
    print("You arrived at what seemed to be a little, lovley, dear, valley,...")
    #time.sleep(2)
    print("Wide green fields, a shallow river, a forest. There seems to be everything you need for a humble beginning,...")
    #time.sleep(2)
    print("You decide, to settle down here. This looks just like the place you were looking for.")
    print("")
    print("Please note: You should build houses for your colonists they only survive 90 days without shelter.")
    print("")
    #time.sleep(2)
    input_name()
    #time.sleep(2)
    print("")
    set_up_sign()
    time.sleep(2)
    print("Today you will rest. You light up a bonfire. Grill some meat. Drink wine you brought with you and celebrate your arrival,...")
    time.sleep(2)
    print("Tomorrow you will start to build your new settlement. It looks like a bright future lays ahead,....")
    time.sleep(2)
    #clear()
    print("Rested you are going to organize everything, as your fellow clonists are awaking,...")


# Starting the actual game

intro()


main()
