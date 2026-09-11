inventory = 0
failed_inputs = 0
isrunning = True

def call_programme(isrunning, inventory, failed_inputs):
    
    while isrunning:
        print("Current inventory is: {}".format(inventory) )
        userinput = input("Please input your inventory count: " )
        if userinput.lower() == "quit":
            print("Total units processed: {}".format(inventory))
            print ("Failed/Rejected entries: {}".format(failed_inputs))
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
            failed_inputs += 1
        call_programme(True,inventory, failed_inputs)


call_programme(True, inventory, failed_inputs)