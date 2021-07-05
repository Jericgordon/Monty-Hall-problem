from random import randint


#sheep is the door number between 1-3 that the sheep is stored. Each index is another situation wehre the sheep are.
sheep = []
pick = []
switch_pick = []
trials = 10000000


#generate a random list of guesses, and the doors behind which the sheep actually are.
for x in range(trials):
    sheep.append(randint(1,3))
    pick.append(randint(1,3))
    
#generate the choice that the host gives the contestent. There are two senarios for this option
for y in range(trials):
    # the first if deals with the case that the pick was initally right, in which case switching will inevitabley loose us the game
    if sheep[y] == pick[y]: 
         switch_pick.append(4)
    # the second senario is that the initial choice was wrong, in which case switching will give us the sheep
    else:
         switch_pick.append(sheep[y])
        

#computes the win rates of the two methods
def compare_options(pick,swtich_pick):
    pick_score = 0
    switch_pick_score = 0
    for x in range(trials):
        if pick[x] == sheep[x]:
            pick_score += 1
    for x in range(trials):
        if switch_pick[x] == sheep[x]:
            switch_pick_score += 1
    print("The win rate of sticking with your pick is:", pick_score/trials *100, "%")
    print("The win rate of switching when offered is:", switch_pick_score/trials *100, "%")


compare_options(pick, switch_pick)

