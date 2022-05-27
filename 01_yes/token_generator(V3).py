import random

#initialising variables
startingbalance = 100

balance = startingbalance
#generating variables
for item in range (0,10):
    chosen_num = random.randint(1,100)

    #Calculating the amount they hold
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5


    #Output
    print("You got a {}. Your balance is "
          "${:.2f}".format(chosen, balance))

print("Starting balance: {} \nFinal balance {} ".format(startingbalance,balance))
