def oneKelly(prob, dec_odds):
    
    # Kelly Criterion
    # f = the fraction of the bankroll to bet
    # b = the decimal odds - 1
    # p = the probability
    # q = the probability of losing, which is 1 - p
    
    p = prob
    b = dec_odds - 1
    q = 1 - prob
    
    kelly = ((b * p) - q) / b
    
    return kelly
    
    
def halfKelly(prob, dec_odds):
    
    # oneKelly Criterion / 2
    
    p = prob
    b = dec_odds - 1
    q = 1 - prob
    
    halfKelly = (((b * p) - q) / b) / 2
    
    return halfKelly
    
def twoKelly(prob, dec_odds):

    # twoKelly Criterion * 2
    
    p = prob
    b = dec_odds - 1
    q = 1 - prob
    
    twoKelly = (((b * p) - q) / b) * 2
    
    return twoKelly

def fourthKelly(prob, dec_odds):

    # Kelly Criterion / 2
    
    p = prob
    b = dec_odds - 1
    q = 1 - prob
    
    fourthKelly = (((b * p) - q) / b) / 4
    
    return fourthKelly