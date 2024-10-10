# learning lambda functions by building an expense tracker
# add expense
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    print('Expense added.')

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