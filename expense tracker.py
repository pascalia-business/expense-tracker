class Category:
    def __init__(self, type_of_expense, name, amount):
        self.type_of_expense = type_of_expense
        self.name = name
        self.amount = float(amount)

    def __str__(self):
        return f"{self.type_of_expense} - {self.name}: ${self.amount:.2f}"


class Person:
    def __init__(self, name, occupation, expense=None):
        self.name = name
        self.occupation = occupation
        self.expense = expense if expense is not None else []

    def add_expense(self):
        expense_type = input("Enter type of expense: ")
        expense_name = input("Enter name of expense: ")
        expense_amount = float(input("Enter amount of expense: "))
        new_expense = Category(expense_type, expense_name, expense_amount)
        self.expense.append(new_expense)

    def view_expenses(self):
        if not self.expense:
            print("No expenses recorded.")
        else:
            for exp in self.expense:  # Go through each expense in the list
                print(exp)  # This calls __str__() automatically!

    def calculate_total_expenses(self):
        total = 0
        for exp in self.expense:  # Loop through the expense list
            total += exp.amount  # Get amount from each Category object
        return total

    def display_info(self):
        print(f'Hi {self.name} from {self.occupation}, here are your expenses:')
        for exp in self.expense:
            print(exp)  # This calls __str__() from Category
        total = self.calculate_total_expenses()
        print(f'Total expenses: ${total:.2f}')


username = input("Enter your name: ")
job = input("Enter your occupation: ")
person1 = Person(username, job)

while True:
    adding_expense = input('Do you want to add expense: ').lower()
    if adding_expense == 'yes':
        person1.add_expense()
    elif adding_expense == 'no':
        viewing_information = input('Type 1 to view expenses, 2 to display personal info, '
                                    'or 3 to calculate total expenses: ')
        if viewing_information == "1":
            person1.view_expenses()
        elif viewing_information == "2":
            person1.display_info()
        elif viewing_information == "3":
            total_cost = person1.calculate_total_expenses()
            print(f"Total expenses: ${total_cost:.2f}")
        else:
            print("Invalid choice, please try again.")

    exit_program = input("Do you want to exit? (yes/no): ").lower()
    if exit_program == "yes":
        print("Goodbye!")
        break  # Exit the loop

