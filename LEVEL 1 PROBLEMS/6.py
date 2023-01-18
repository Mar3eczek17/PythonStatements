def blackjack(a, b, c):
    if a + b + c <= 21:
        print(a + b + c)
    elif a + b + b > 21 and a == 11 or b == 11 or c == 11:
        print(a + b + c - 10)
    else:
        print("BUST")


# Check
blackjack(5, 6, 7)
# Check
blackjack(9, 9, 9)
# Check
blackjack(9, 9, 11)
