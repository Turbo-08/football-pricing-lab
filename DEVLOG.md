# Football Pricing Lab Dev Log

## Current Project Status
- 1X2 odds input working
- Implied probability working
- Overround working
- Margin-adjusted probabilities working
- Margin-free odds working
- EV calculation working
- No real prediction model yet
- No APIs yet
- No bet tracker yet

## Session 1 - 2026-09-15

### Goal
- Add decision engine
- Add basic automated tests
- Set up Git and make first commit

### Done
- Added EV-based decision engine with minimum threshold
- Added input validation for outcome, probability and odds
- Added automated tests for pricing functions
- Set up Git repository
- Added .gitignore
- Made first commit: "Initial 1X2 pricing engine"

### Learned
- How a minimum EV threshold affects bet decisions
- How try/except prevents crashes from invalid input
- How automated tests catch mistakes
- Basic Git workflow: init, add, status, commit

### Next Session
- Create GitHub repository and connect local project
- Push first commit to GitHub
- Design the bet tracker
- Decide what data each prediction should store
- Start saving predictions/results


## Session 2 - 2026-09-17

### Goal
- Connect project to GitHub and push first commit
- Design the bet tracker
- Start saving predictions

### Done
- Connected local Git repository to GitHub
- Pushed first commit to GitHub
- Designed flexible prediction tracker structure
- Added sport, event, market type, subject, line and selection fields
- Created tracker.py
- Created data/bets.csv
- Connected main.py to tracker.py
- Successfully saved a prediction to CSV

### Learned
- Difference between local Git commits and pushing to GitHub
- How CSV files can store structured prediction data
- Why generic tracker fields are better than separate columns for every market
- How one prediction flows from main.py to tracker.py to bets.csv

### Next Session
- Improve tracker input validation
- Separate predictions from actual bets
- Add automatic prediction IDs
- Add result and profit/loss updating
- Consider adding a README