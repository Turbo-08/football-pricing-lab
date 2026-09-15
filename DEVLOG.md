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
