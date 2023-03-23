# With Transaction History functionality

import os
import json
import datetime as d

def save_data():
    with open('total_balance.txt','w') as f:
        json.dump(total_balance,f)
    now_date = d.datetime.now().strftime("%m/%d/%Y")
    now_time = d.datetime.now().strftime("%H:%M:%S")
    dollar_amount = "${:,.2f}".format(amount_input)
    dollar_total = "${:,.2f}".format(total_balance)
    with open('transaction_history.txt','a') as f:
        f.write('\n'"{: <20}{: <20}{: <20}{: <20}{: <20}".format((now_date),(now_time),(dollar_amount),(trans_category),(dollar_total)))

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
    save_data()
    print('\nThanks, have a great day!\n')
    quit()

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print('\n~~~ Welcome to your terminal checkbook ~~~\n')

while True:
    print('''What would you like to do?
         
    1) View current balance
    2) Record a debit (withdraw)
    3) Record a credit (deposit)
    4) View Transaction History
    5) Exit
    ''')
    user_input = input('Please enter a value (1-5): ')

    if user_input not in list('12345'):
        print('\nThat is not a valid selection.')
        continue

    elif user_input == '1': # view balance
        print(f'\n\t\tYour current balance is: ${view_balance()}\n')

    elif user_input == '2': # withdraw
        while True:
            amount_input = input('How much was the debit? $').replace(',','').replace('-','')
            if amount_input.isdigit() == False and isfloat(amount_input) == False:
                print('That is not a valid input.')
                continue
            else:
                trans_category = 'Debit'
                amount_input = float(amount_input)
                total_balance = record_debit(amount_input)
                save_data()
                print(f'\n\t\tGreat! Your current balance is now: ${view_balance()}\n')
                break
                
    elif user_input == '3': # deposit
        while True:
            amount_input = input('How much was the credit? $').replace(',','').replace('-','')
            if amount_input.isdigit() == False and isfloat(amount_input) == False:
                print('That is not a valid input.')
                continue
            else:
                trans_category = 'Credit'
                amount_input = float(amount_input)
                total_balance = record_credit(amount_input)
                save_data()
                print(f'\n\t\tGreat! Your current balance is now: ${view_balance()}\n')
                break
    
    elif user_input == '4': # view transaction history
        f = open('transaction_history.txt', 'r')
        file_contents = f.read()
        print()
        print(file_contents)
        print()

    elif user_input == '5': # exit
        exit_program()