import os
import json

if os.path.exists('total_balance.txt') == True:
    with open('total_balance.txt') as f:
        total_balance = json.load(f)
else:
    with open('total_balance.txt','w') as f:
        total_balance = int(f.write('0'))

def view_balance():
    return "{:,.2f}".format(total_balance)

def record_debit(x):
    return total_balance - x 

def record_credit(x):
    return total_balance + x

def exit_program():
    with open('total_balance.txt','w') as f:
        json.dump(total_balance,f)
    print('Thanks, have a great day!')
    quit()

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print('~~~ Welcome to your terminal checkbook ~~~\n')

while True:
    print('''What would you like to do?
         
    1) View current balance
    2) Record a debit (withdraw)
    3) Record a credit (deposit)
    4) Exit
    ''')
    user_input = input('Please enter a value (1-4): ')

    if user_input not in list('1234'):
        print('\nThat is not a valid selection.')
        continue

    elif user_input == '1': # view balance
        print(f'Your current balance is: ${view_balance()}')

    elif user_input == '2': # withdraw
        while True:
            amount_input = input('How much was the debit? $')
            if amount_input.isdigit() == False and isfloat(amount_input) == False:
                print('That is not a valid input.')
                continue
            else:
                amount_input = float(amount_input)
                total_balance = record_debit(amount_input)
                print(f'Your current balance is now: ${view_balance()}')
                break
                
    elif user_input == '3': # deposit
        while True:
            amount_input = input('How much was the credit? $')
            if amount_input.isdigit() == False and isfloat(amount_input) == False:
                print('That is not a valid input.')
                continue
            else:
                amount_input = float(amount_input)
                total_balance = record_credit(amount_input)
                print(f'Your current balance is now: ${view_balance()}')
                break
                
    elif user_input == '4': # exit
        exit_program()