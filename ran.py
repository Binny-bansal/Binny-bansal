from random import randint
Avengers = ['Iron Man', 'Thor', 'Hulk', 'Black Widow', 'Doctor Strange', 'Ant Man', 'Black Panther', 'Winter Soldier', 'Vision', 'Wasp', 'Spider Man', 'Captain America']

l = len(Avengers)
k = randint(0,l-1)
print(Avengers[k])

s= ""
for i in Avengers[k]:
        if i == " " or i == 'a'or i == 'e'or i == 'i' or i == 'o'or i == 'u':
                s+=i
                s += " "
                continue
        s+= "_ "
print (s)