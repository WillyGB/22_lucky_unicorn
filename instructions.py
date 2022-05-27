
valid = False
while not valid:

    # Ask user if played before
    instructions = input("Have you played this game before? (yes or no): ").lower().strip()

    # If user says yes
    if instructions == "yes" or instructions == "y":
        print("Instructions have been skipped...")
        valid = True

    # If user says no
    elif instructions == "no" or instructions == "n":
        print("Display Instructions...")
        valid = True

    # If user says something else
    else:
        print("You must enter either yes or no.")
