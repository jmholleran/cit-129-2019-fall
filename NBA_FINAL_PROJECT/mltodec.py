def convertmltodec(line):
    
    # To convert moneyline odds to decimal odds:
    # if the moneyline is positive, divide by 100 and add 1
    # if it is negative, divide 100 by the moneyline amount (without the minus sign) and add 1

    if line > 0:
        dec_odds = (line / 100) + 1
        return dec_odds
    else:
        dec_odds = (100 / (line * -1)) + 1
        return dec_odds
        