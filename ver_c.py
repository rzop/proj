# Richard
def Encode(string):
    res = []
    # what we need to return
    for num in string:
        if num == "9":
            res.append("2")
        elif num == "8":
            res.append("1")
        elif num == "7":
            res.append("0")
        elif num == "6":
            res.append("9")
        elif num == "5":
            res.append("8")
        elif num == "4":
            res.append("7")
        elif num == "3":
            res.append("6")
        elif num == "2":
            res.append("5")
        elif num =="1":
            res.append("4")
        elif num =="0":
            res.append("3")
    return "".join(res)
    # Always output string so the list can be joined
if __name__ == "__main__":
    menu_cont = True
    # We need to continue pulling up the menu until the user input 3
    while menu_cont:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option_pick = input("Please enter an option:")
        if option_pick == "1":
            string = input("Please enter you password to encode:")
            # Need to save this for option == 2 and printing the og password and for use of Encode().
            encoded_string = Encode(string)
            # Need to use encoded_string for option 2/the decode function
            print("Your password has been encoded and stored!")
        if option_pick == "2":
            pass
        elif option_pick == "3":
            menu_cont = False
            # Exit the loop




