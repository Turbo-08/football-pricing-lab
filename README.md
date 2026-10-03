# Football Pricing Lab

A Python project for football odds pricing, expected value analysis, prediction tracking, and bet settlement.

## Current Features
- 1X2 odds input
- Implied probability calculation
- Bookmaker overround calculation
- Margin-adjusted probabilities
- Margin-free market odds
- Expected value calculation
- Positive EV / NO BET decision
- Input validation
- Prediction tracking
- Bet tracking
- Automatic prediction IDs
- Bet settlement and profit/loss calculation
- Automated tests

## Project Structure
- `main.py` - main program flow
- `pricing.py` - pricing and probability calculations
- `tracker.py` - prediction and bet tracking
- `settle_bet.py` - bet settlement
- `test_pricing.py` - pricing tests
- `test_tracker.py` - tracker tests
- `data/` - CSV prediction and bet data

## Current Limitation
The model probability is still entered manually. A statistical prediction model and API integration will be added later.

## Roadmap
- Football data API integration
- Automated odds retrieval
- Statistical probability model
- More football markets
- Backtesting
- Model evaluation and calibration
- Dashboard
- Expansion to other sports