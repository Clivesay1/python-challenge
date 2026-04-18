# Financial & Election Data Analysis with Python

**Tools:** Python | CSV I/O | os | pathlib  
**Author:** Chris Livesay

---

## Overview

This project contains two independent Python scripts that automate the analysis of real-world datasets: a financial records analysis (PyBank) and an election results analysis (PyPoll).

**Key Skills Demonstrated:** File I/O with CSV, Python loops and conditionals, data aggregation, formatted console and file output.

---

## PyBank — Financial Records Analysis

**Business Question:** What are the key financial performance metrics from a company's monthly profit/loss records?

**The script calculates:**
- Total number of months in the dataset
- Net total of Profits/Losses
- Average change in Profits/Losses month-over-month
- Month with the greatest increase in profits
- Month with the greatest decrease in profits

**Sample Output:**
```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

---

## PyPoll — Election Results Analysis

**Business Question:** Who won the election, and what was each candidate's vote share?

**The script calculates:**
- Total votes cast
- Each candidate's total votes and percentage of the vote
- The winner based on popular vote

---

## Repository Structure

```
python-challenge/
├── PyBank/
│   ├── main.py               # Financial analysis script
│   └── Resources/
│       └── budget_data.csv   # Source data
├── PyPoll/
│   ├── main.py               # Election analysis script
│   └── Resources/
│       └── election_data.csv # Source data
└── README.md
```

---

## How to Run

1. Clone the repository: `git clone https://github.com/Clivesay1/python-challenge.git`
2. Navigate to either `PyBank/` or `PyPoll/`
3. Run: `python main.py`
4. Results print to the console and are saved to a text file in the folder
