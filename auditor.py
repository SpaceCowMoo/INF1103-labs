def call_programme():
    inventory = 0
    failed_inputs = 0

    while True:
        print(f"Current inventory is: {inventory}")
        userinput = input("Please input your inventory count: ").strip()

        if userinput.lower() == "quit":
            print(f"Total units processed: {inventory}")
            print(f"Failed/Rejected entries: {failed_inputs}")
            break

        if userinput.isdigit():
            userint = int(userinput)
            inventory += userint

            if inventory >= 500:
                print("ALERT, STORAGE IS FULL")
                break
        else:
            print("ERROR, PLEASE INPUT IN A POSITIVE NUMBER")
            failed_inputs += 1


call_programme()