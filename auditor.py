inventory = 0


def call_programme(isrunning, inventory):
    isrunning = True
    while isrunning:
        print("Current inventory is: {}".format(inventory) )
        userinput = input("Please input your inventory count: " )
        if userinput.lower() == "quit":
            print("ending")
            break
        elif userinput.isdigit():
            userint = int(userinput)
            if userint >= 0:
                isrunning = False
                inventory = inventory + int(userinput)
            if userint >= 500:
                print("ALERT, STORAGE IS FULL")
                break
        else:
            isrunning = False
            print("ERROR, PLEASE INPUT IN A POSITIVE NUMBER")
        call_programme(True,inventory)


call_programme(True, inventory)