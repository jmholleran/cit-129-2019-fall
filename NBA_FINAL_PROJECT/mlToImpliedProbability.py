def convertMLtoProb(line):
    
    # Convert Moneyline to its Implied Probability

    if line > 0:
        impliedProbability = (100 / (line + 100))       
        return impliedProbability
    else:
        impliedProbability = (-(line))/((-(line)) + 100)
        return impliedProbability

