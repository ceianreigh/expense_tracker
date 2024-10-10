# learning lambda functions by building an expense tracker
# add expense
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    print('Expense added.')

# list all expenses
def list_expenses(expenses):
    for expense in expenses:
        print(f"Category: {expense['category']}, Amount: {expense['amount']}")

# show total expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# filter expenses by category
def filter_expenses(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []
    
    # create a menu
    choices = {1: 'Add an expense', 
               2 : 'List all expenses', 
               3: 'Show total expenses', 
               4: 'Filter expenses by category', 
               5: 'Exit'}
    
    # create a loop to keep the program running
    while True:
        print("Welcome to your Expense Tracker!")

        for key, value in choices.items():
            print(f'{key}. {value}')
        
        # get the user's choice
        choice = int(input('\nEnter your choice: '))

        # logic to handle the user's choice
main()