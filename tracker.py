import csv
from pathlib import Path

FIELDS = [
    "sport",
    "prediction_id",
    "created_at",
    "event",
    "market_type",
    "subject",
    "line",
    "selection",
    "bookmaker",
    "odds",
    "model_probability",
    "ev",
    "stake",
    "result",
    "profit_loss",
    "model_version"
]

def save_record(record, filename):
    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    file_path = data_folder/ filename
    file_has_data = file_path.exists() and file_path.stat().st_size > 0

    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if not file_has_data:
             writer.writeheader()

        writer.writerow(record)

def save_prediction(prediction):
    save_record(prediction, "predictions.csv")


def save_bet(bet):
    save_record(bet, "bets.csv")



def calculate_profit_loss(result, stake, odds):
    if result == "Win":
        return stake * (odds - 1)

    if result == "Loss":
        return -stake

    if result == "Void":
        return 0

    raise ValueError("Result must be Win, Loss or Void")

def update_result(filename, prediction_id, result):
    file_path = Path("data") / filename

    rows = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["prediction_id"] == prediction_id:
                stake = float(row["stake"])
                odds = float(row["odds"])

                row["result"] = result
                row["profit_loss"] = calculate_profit_loss(
                    result, stake, odds
                )

            rows.append(row)

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

def get_unsettled_bets():
    file_path = Path("data") / "bets.csv"

    unsettled_bets = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row.get("result", "") == "":
                unsettled_bets.append(row)

    return unsettled_bets 