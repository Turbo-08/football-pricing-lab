def implied_probability(odds):
    if odds <=1:
        raise ValueError ("Decimal odds must be greater than 1.")
    probability = 1 / odds
    return probability


def normalize_probability(probability, total_probability):
    normalize_probability = probability / total_probability
    return normalize_probability

def calculate_overround(total_probability): 
    return total_probability - 1 

def fair_odds(probability):
    if probability <= 0 or probability > 1:
        raise ValueError("Probability must be greater than 0 and at most 1.")
    return 1 /probability

def expected_value(odds, probability):
    if odds <=1: 
        raise ValueError("Decimal odds must be greater than 1.")
    
    if probability < 0 or probability > 1:
        raise ValueError ("Probability must be between 0 and 1.")

    return probability * odds - 1
    