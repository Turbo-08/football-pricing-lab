import csv
import os 
import tempfile 
import unittest

from tracker import (
    save_prediction,
    calculate_profit_loss,
    update_result

)

class TestTracker(unittest.TestCase):

    def setUp(self):
        self.original_folder = os.getcwd()
        self.temp_folder = tempfile.TemporaryDirectory()
        os.chdir(self.temp_folder.name)

    def tearDown(self):
        os.chdir(self.original_folder)
        self.temp_folder.cleanup()

    def test_profit_loss_win(self):
        result = calculate_profit_loss("Win", 5, 1.80)
        self.assertAlmostEqual(result, 4.00)

    def test_profit_loss_loss(self):
        result = calculate_profit_loss("Loss", 5, 1.80)
        self.assertAlmostEqual(result, -5.00)

    def test_profit_loss_void(self):
        result = calculate_profit_loss("Void", 5, 1.80)
        self.assertAlmostEqual(result, 0.00)

    def test_save_prediction_creates_csv(self):
        prediction = {
            "sport": "Football",
            "prediction_id": "test-1",
            "created_at": "2026-10-03 20:00:00",
            "event": "Portugal vs Spain",
            "market_type": "1X2",
            "subject": "",
            "line": "",
            "selection": "Home",
            "bookmaker": "Bet365",
            "odds": 1.80,
            "model_probability": 0.60,
            "ev": 0.08,
            "stake": 5,
            "result": "",
            "profit_loss": "",
            "model_version": "v0.1"
        }

        save_prediction(prediction)

        self.assertTrue(os.path.exists("data/predictions.csv"))


    def test_update_result(self):
        prediction = {
            "sport": "Football",
            "prediction_id": "test-2",
            "created_at": "2026-10-03 20:00:00",
            "event": "Portugal vs Spain",
            "market_type": "1X2",
            "subject": "",
            "line": "",
            "selection": "Home",
            "bookmaker": "Bet365",
            "odds": 1.80,
            "model_probability": 0.60,
            "ev": 0.08,
            "stake": 5,
            "result": "",
            "profit_loss": "",
            "model_version": "v0.1"
        }

        save_prediction(prediction)

        update_result(
            "predictions.csv",
            "test-2",
            "Win"
        )

        with open("data/predictions.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            row = next(reader)

        self.assertEqual(row["result"], "Win")
        self.assertAlmostEqual(float(row["profit_loss"]), 4.00)


if __name__ == "__main__":
    unittest.main()


    