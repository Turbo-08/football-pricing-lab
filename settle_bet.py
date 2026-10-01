from tracker import update_result

prediction_id = input("Enter prediction ID:").strip()

while True:
    result = input("Enter result (Win/Loss/void): ").strip().title()

    if result in ["Win", "Loss", "Void"]:
        break

    print("Invalid result. Entre Win, Loss, or Void")

    update_result("bets.csv", prediction_id, result)

print("Bet result updated.")