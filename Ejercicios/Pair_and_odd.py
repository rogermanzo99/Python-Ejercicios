if __name__ == '__main__':
    n = int(raw_input())
    print(("Not " if (n%2 == 0) and (n<=4 or n>20) else"") + "Weird")
#si numero       es   ENTERO     Y  cumple que NUMERO <= 4 o NUMERO > 20 "NOT"