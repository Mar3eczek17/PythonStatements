def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        print(sum([a, b, c]))
    elif 11 in [a, b, c] and sum([a, b, c]) - 10 <= 21:
        print(sum([a, b, c]) - 10)
    else:
        print("BUST")


# Check
blackjack(5, 6, 7)
# Check
blackjack(9, 9, 9)
# Check
blackjack(9, 9, 11)
