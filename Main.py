from Person import *
from Transaction import *
from FileOpener import *
import os

all_items = os.listdir("People")
people_names = [item for item in all_items if os.path.isdir(os.path.join("People", item))]
people_objects = [Person(name) for name in people_names]

def choose_person():
    for i in range(len(people_names)):
        print(f"{i+1}. {people_names[i]}")
    return int(input("Enter person number: ")) - 1

while True:
    print(
"""Options:
1. Add a person
2. Add a reference
3. Add sessions for a person
4. Import payments from .xlsx
0. Exit
"""
)
    option = int(input("Enter option: "))
    if option == 0:
        break
    elif option == 1:
        name = input("Enter name: ")
        people_names.append(name)
        people_objects.append(Person(name))
    
    elif option == 2:
        person_number = choose_person()
        reference = input("Enter reference: ")
        people_objects[person_number].add_reference(reference)
    
    elif option == 3:
        person_number = choose_person()
        print("Enter sessions in the following format:")
        print("dd/mm/yyyy 99.99 any notes (e.g. no show")
        print("Enter 'exit' to stop")
        while True:
            inp = input()
            if inp.lower() == "exit":
                break
            inp = inp.split()
            inp.insert(2, "MANUAL SESSION")
            inp = " ".join(inp)
            people_objects[person_number].add_transaction(Transaction(inp))
    
    elif option == 4:
        file_path = open_file_dialog()
        for person in people_objects:
            person.import_transactions_from_file(file_path)