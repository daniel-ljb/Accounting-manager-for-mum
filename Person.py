from Transaction import *

import pandas as pd
import bisect
import os
        
class Person():
    def __init__(self, name: str):
        self.__name = name
        self.__folder_path = f"People\\{self.__name}"
        self.__ledger_path = f"{self.__folder_path}\\Ledger.txt"
        self.__references_path = f"{self.__folder_path}\\References.txt"
        
        os.makedirs(self.__folder_path, exist_ok=True)
        
        self.__transactions = [Transaction(line) for line in open(self.__ledger_path)] if os.path.exists(self.__ledger_path) else []
        self.__references = list(open(self.__references_path)) if os.path.exists(self.__references_path) else []
    
    def write_transactions(self):
        with open(self.__ledger_path, 'w') as f:
            f.writelines("\n".join([str(x) for x in self.__transactions]))
    
    def add_transaction(self, transaction: Transaction):
        bisect.insort(self.__transactions, transaction)
        self.write_transactions()
    
    def remove_transaction(self, transaction: Transaction):
        self.__transactions.remove(transaction)
        self.write_transactions()
    
    def write_references(self):
        with open(self.__references_path, 'w') as f:
            f.writelines("\n".join([str(x) for x in self.__references]))
        
    def add_reference(self, reference: str):
        self.__references.append(reference)
        self.write_references()
    
    def remove_reference(self, reference: str):
        try:
            self.__references.remove(reference)
        except:
            print("That reference is not added")
        self.write_references()
    
    def import_transactions_from_file(self, file_path):
        sheet = pd.read_excel(file_path, sheet_name=0, engine='openpyxl').to_numpy()
        sheet = [list(map(str, x)) for x in sheet]
        
        description_column = 3 #D
        date_column = 1 #B
        money_in_column = 5 #F
        money_out_column = 6 #G

        for row in range(5, len(sheet)):
            description = sheet[row][description_column]

            if description in self.__references:
                try:
                    date = sheet[row][date_column]
                    
                    money_in = sheet[row][money_in_column]
                    money_out = sheet[row][money_out_column]
                    
                    money_in = 0 if "nan" == money_in else float(money_in.replace('£', ''))
                    money_out = 0 if "nan" == money_out else float(money_out.replace('£', ''))
                    net_amount = money_out - money_in

                    transaction_str = f"{date} {net_amount} Bank Transfer {description}"
                    transaction = Transaction(transaction_str)
                    
                    if transaction_str not in [str(x) for x in self.__transactions]:
                        self.add_transaction(transaction)

                except Exception as e:
                    print(f"Error processing row {row + 1}: {e}")
                    continue  # Continue to the next row in case of an error
    
    def menu(self, number_per_page: int = 10):
        pages = (len(self.__transactions)-1) // number_per_page + 1
        while True:
            current_page = 1
            for i in range((current_page-1)*number_per_page, current_page*number_per_page):
                print(f"{i+1:>{len(str(number_per_page))}}. {self.__transactions[i] if i < len(self.__transactions) else ''}")
            print(f"Page {current_page} of {pages}")
            inp = input()
            if inp == ">":
                current_page = min(pages, current_page + 1)
            elif inp == "<":
                current_page = max(0, current_page - 1)
            elif inp.isdigit() and 0 <= int(inp) - 1 < len(self.__transactions):
                return self.__transactions[int(inp) - 1]
            else:
                return inp