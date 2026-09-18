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

def save_prediction(prediction):
    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    file_path = data_folder/ "bets.csv"

    file_exists = file_path.exists()

    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if not file_exists:
            writer.writeheader()

        writer.writerow(prediction)




    