def check_temp():
    if t < 15:
        return("So cold!")
    elif t < 30:
        return("It's a good day.")
    elif t < 40:
        return("So hot!!")


if __name__ == '__main__':
    t = input("Enter your temperture :")
    while t !='q':
        if t.isnumeric():
            t = int(t)
            print(check_temp(t))
        else:
            print("You must enter number of temperature:")

        t = int(t)
        check_temp(t)
        t = input("Enter mew temperture :")
    sys.exit(0)



