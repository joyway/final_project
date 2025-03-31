# Troubleshooting and Exception Handling: Programming Beyond Expected Results

## Description
Assignment for module 4

## Author
Jiawei Song

## Assignment
This assignment involves troubleshooting an existing program to locate and correct logic errors. In addition, you will use exception handling to anticipate and handle potential exceptions which could lead to unexpected results and/or program crashes.

## PiXELL Transaction Report
Use Exceptions, Logging and Debugging techniques and VS Code built-in debugging tool to improve the quality of `pixell_transaction_report.py`

## Code Modification:
- Added a try-block around the executable code to catch and print FileNotFoundError.
- Added validation for `transaction_type` and `transaction_amount`
- Added an else block to store invalid records in `rejected_records`
- Renamed `total_transaction_amount` to `total_transaction_count` to align with `total_transaction_amount`
- Deleted `transaction_counter`, replaced it with `total_transaction_amount` when calculating average transcation
- `total_transaction_amount` is now incremented correctly for each transcation
- Fixed the incorrect condition for withdraw action
- Fixed an issue that user's balance was increased when withdrawing
- Formatted all numbers in the output to have 2 decimal places