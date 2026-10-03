from tracker import get_unsettled_bets, update_result

bets = get_unsettled_bets()

if len(bets) == 0:
    print ("No unsettled bets")

else:
    print("\nUnsettled bets:")

    for index, bet in enumerate(bets, start=1):
        print(
           f"{index}. {bet['event']} | "
            f"{bet['selection']} | "
            f"@{bet['odds']} | "
            f"Stake €{bet['stake']}" 
        )
    while True:
        try:
           choice = int(input("\nSelect bet number: "))

           if 1 <= choice <=len(bets):
            break

           print("Invalid selection.")

        except ValueError:
            print("Enter a number.")
               
    selected_bet = bets[choice -1 ]

    while True:
        result = input("Enter result (Win/Loss/Void): ").strip().title()

        if result in ["Win", "Loss", "Void"]:
            break

        print("Invalid result.")

    update_result(
        "bets.csv",
        selected_bet["prediction_id"],
        result
    )

    print("Bet result updated.")
