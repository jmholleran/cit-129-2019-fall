def adjustProbability(modelProb, pastModelProb):
    
    # Using Bayes's Theorem to Adjust Probability from Model (Monte Carlo Sim)
    # to use in the Kelly Criterion
    
    # Source: 'The Signal and the Noise' by Nate Silver, page 247
    
    # Equation
    
    # Model Probability = x
    # Past Results - Model Predict Winner = y
    # Past Results - Model Did not Predict Winner: z = 1 - y
    # PosteriorProb = (xy) / (xy + z(1-x))
    
    x = modelProb
    y = pastModelProb
    z = (1 - pastModelProb)
    
    adjustedProb = (x * y) / ((x * y) + (z * (1 - x)))
    
    return adjustedProb

