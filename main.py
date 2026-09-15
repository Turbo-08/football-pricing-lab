from pricing import(
implied_probability, 
normalize_probability,
calculate_overround,
fair_odds, 
expected_value
)

MIN_EV_THRESHOLD = 0.05

def get_valid_odds(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 1:
                return value
            print ("Decimal odds must be greater than 1")

        except ValueError:
            print("Invalid input. Enter a number.")

odds = {
    "Home": get_valid_odds ("Enter Home odds:"),
    "Draw": get_valid_odds("Enter draw odds:"),
    "Away": get_valid_odds("Enter Away odds:")
}

probabilities = {}

for outcome, price in odds.items():
    probabilities[outcome] = implied_probability(price)

    total_probability = sum(probabilities.values())

    overround = calculate_overround(total_probability)




normalized_probabilities = {}

for outcome, probability in probabilities.items():
    normalized_probabilities[outcome] = normalize_probability(
        probability, total_probability
    )




fair_market_odds = {}

for outcome, probability in normalized_probabilities.items():
    fair_market_odds[outcome] = fair_odds(probability)




for outcome, probability in probabilities.items():
    print(f"{outcome}: {probability: .2%}")

print(f"Total: {total_probability:.2%}")

print(f"Bookmarker overround: {overround:.2%}")

print ()
print ("Margin-adjusted probabilities:")
for outcome, probability in normalized_probabilities.items():
    print(f"{outcome}: {probability: .2%}")

print()
print("Margin-free market odds:")
for outcome, price in fair_market_odds.items():
    print(f"{outcome}: {price: 2f}")


print()

while True:
    selection = input(
        "Which outcome do you want to evaluate? Home/Draw/Away: "
    ).strip().title()

    if selection in odds:
        break

    print("Invalid selection. Enter Home, Draw, or Away.")

while True:
    try:
        model_probability_percent = float(
            input("Enter your estimated probability for this outcome (%): ")
        )

        if 0 <= model_probability_percent <= 100:
            break

        print("Probability must be between 0 and 100.")

    except ValueError:
        print("Invalid input. Enter a number.")

model_probability = model_probability_percent/100

selected_odds = odds[selection]

ev = expected_value(selected_odds, model_probability)


print()
print(f"Selected outcome: {selection}")
print(f"Bookmaker odds: {selected_odds:.2f}")
print(f"Your estimated probability: {model_probability:.2%}")
print(f"Expected value: {ev:.2%}")


if ev >= MIN_EV_THRESHOLD:
    print("Decision: Positive EV candidate")

else:
    print("Decision: NO BET")


