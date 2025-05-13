
import random
set=[]
h='H'
t='T'
number_of_streaks=0
round=0
while round <10000:
    set=[]
    for i in range (1,101):
        flip=random.randint(0,1)
        if flip == 0:
            set.append(h)
        else:
            set.append(t)
    for s in range(len(set)-6):
        if set[s]== set[s+1]==set[s+2]==set[s+3]==set[s+4]==set[s+5]!=set[s+6]:
            number_of_streaks+=1
    round += 1
print("there's a"+str(number_of_streaks/round*100)+"%  chance of a streak of 6 in a 100 flips based on 10,000 rounds.")

