
valid = False
while not valid:


    try:

        deposit = int(input("How much money do you want to deposit? \n(You can only enter $1 - $10)"))

        #If user deposits more than 10
        if deposit >= 11:
            print("Cannot except --- Too much money deposited")

        #If user deposits less than 1
        elif deposit <= 0:
            print("Cannot except --- Too little or none money deposited")
        #Deposits the money
        else:
            print("Money deposited: ${}".format(deposit))
            valid = True
    #If user enters a float
    except ValueError:
        print("Cannot except --- You must deposit a whole number")
