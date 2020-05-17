sct=input("Enter a number: ")
if sct.isdigit():
    sct=int(sct)
    if sct % 2 == 0:
        print("EVEN")
    else:
        print('ODD')
else:
    print("Bad input.")