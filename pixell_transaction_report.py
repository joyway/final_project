"""
Description: A program that reads through transaction records and reports the results.
Author: ACE Faculty
Edited by: Jiawei
Date: Feb 1 2024
Usage: This program will read transaction data from a .csv file, summarize and 
report the results.
"""

import csv
import os


valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_records = []
total_transaction_count = 0
total_transaction_amount = 0
valid_record = True
error_message = ''

os.system('cls' if os.name == 'nt' else 'clear')

try:
    with open('bank_data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in list(reader)[1:]:
            # Reset valid record and error message for each iteration
            valid_record = True
            error_message = ''

            # Extract the customer ID from the first column
            customer_id = row[0]
            
            # Extract the transaction type from the second column
            transaction_type = row[1]
            ### VALIDATION 1 ###
            if transaction_type not in valid_transaction_types:
                valid_record = False
                error_message += 'Invalid transcation type. '
            # Extract the transaction amount from the third column
            ### VALIDATION 2 ###
            try:
                transaction_amount = float(row[2])
            except ValueError:
                valid_record = False
                error_message += 'Transcation amount is not numeric. '

            if valid_record:
                # Initialize the customer's account balance if it doesn't already exist
                if customer_id not in customer_data:
                    customer_data[customer_id] = {'balance': 0, 'transactions': []}

                # Update the customer's account balance based on the transaction type
                if transaction_type == 'deposit':
                    customer_data[customer_id]['balance'] += transaction_amount
                    total_transaction_count += 1
                    total_transaction_amount += transaction_amount
                else: # Substract from the balance
                    customer_data[customer_id]['balance'] -= transaction_amount
                    total_transaction_count += 1
                    total_transaction_amount += transaction_amount
                
                # Record transactions in the customer's transaction history
                customer_data[customer_id]['transactions'].append((transaction_amount, transaction_type))
            
            ### COLLECT INVALID RECORDS ###
            else:
                rejected_records.append((row, error_message))


    print("PiXELL River Transaction Report\n===============================\n")
    # Print the final account balances for each customer
    # Format all numbers in the output to have 2 decimal places
    for customer_id, data in customer_data.items():
        balance = data['balance']

        print(f"\nCustomer {customer_id} has a balance of ${balance:,.2f}.")
        # Print the transaction history for the customer
        print("Transaction History:")
        for transaction in data['transactions']:
            amount, type = transaction
            print(f"\t{type.capitalize()}: ${amount:,.2f}")

    
    print(f"\nAVERAGE TRANSACTION AMOUNT: ${(total_transaction_amount / total_transaction_count):,.2f}")
    print("\nREJECTED RECORDS\n================")
    for record in rejected_records:
        print("REJECTED:", record)
except FileNotFoundError as e:
    print(f'Error: {e}')