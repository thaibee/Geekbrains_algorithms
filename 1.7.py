a = int(input('Enter year please(4 digits)'))
if (a % 4 == 0 and a % 100 != 0) or (a % 100 == 0 and a % 400 == 0):
    print("It's leap year")
else:
    print("It's not leap year")
