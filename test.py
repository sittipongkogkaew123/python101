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
        t = int(t)
        check_temp(t)
        t = input("Enter your temperture :")
    sys.exit(0)



