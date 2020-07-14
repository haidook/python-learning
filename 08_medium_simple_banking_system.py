import random
import sqlite3

class UserAccount:

    def db_connection(self):
        try:
            self.conn = sqlite3.connect('card.s3db')
            # print('Connection succesful')
        except:
            pass
        self.cur = self.conn.cursor()
        try:
            self.cur.execute('''CREATE TABLE card (
                                id INTEGER,
                                number TEXT,
                                pin TEXT,
                                balance INTEGER DEFAULT 0
                                );'''
                        )
            # print('Table created')
            self.conn.commit()
        except:
            pass
        return self.cur, self.conn

    def luhn_check(self, card_number15):
        card_no_list = [int(no) for no in card_number15]
        multiply_no = (enumerate(card_no_list))
        for i, j in multiply_no:
            if i % 2 == 0:
                if j * 2 > 9:
                    card_no_list[i] = (j * 2) - 9
                else:
                    card_no_list[i] = j * 2
            else:
                card_no_list[i] = j
        for i in range(0,10):
            if (sum(card_no_list) + i) % 10 == 0:
                checksum = i
        return checksum

    def luhn_check_full(self, card_number):
        card_no_list = [int(no) for no in card_number]
        multiply_no = (enumerate(card_no_list))
        for i, j in multiply_no:
            if i % 2 == 0:
                if j * 2 > 9:
                    card_no_list[i] = (j * 2) - 9
                else:
                    card_no_list[i] = j * 2
            else:
                card_no_list[i] = j
        if (sum(card_no_list)) % 10 == 0:
            return True

    def generate_card(self):
        bin_no = '400000'
        account_id = ''
        for i in range(9):
            account_id += str(random.randint(0, 9))
        card_number15 = bin_no + account_id
        checksum = self.luhn_check(card_number15)
        card_number15 += str(checksum)
        return card_number15

    def generate_pin(self):
        pin = ''.join([str(random.randint(0,9)) for no in range(4)])
        return pin

    def store(self, card_no, pin_no):
        self.cur.execute('SELECT * FROM card')
        i = len(self.cur.fetchall())
        self.cur.execute("INSERT INTO card (id, number, pin, balance) VALUES (?, ?, ?, ?)", (i, card_no, pin_no, 0))
        self.cur.execute('SELECT * FROM card')
        self.conn.commit()
        self.card_number = card_no
        self.pin_no = pin_no
        return self.card_number, self.pin_no

    def check_card(self, user_card, user_pin):
        self.cur.execute('SELECT number, pin FROM card WHERE number = ? AND pin = ?', (user_card, user_pin))
        if self.cur.fetchone():
            return True

    def check_balance(self):
        self.cur.execute('SELECT * FROM card WHERE number = ?', (user_card,))
        self.balance = str([x for x in self.cur.fetchone()][3])
        return self.balance

    def add_money(self):
        income = int(input('Enter income:\n'))
        self.cur.execute('SELECT * FROM card WHERE number = ?', (user_card,))
        self.balance = int([x for x in self.cur.fetchone()][3]) + income
        self.cur.execute('UPDATE card SET balance = ? WHERE number = ?', (self.balance, user_card))
        self.conn.commit()
        print('Income was added!\n')
        return self.balance

    def do_transfer(self):
        card_number = input('Enter card number:\n')
        self.cur.execute('SELECT * FROM card WHERE number = ?', (card_number,))
        if user_card == card_number:
            print("You can't transfer money to the same account!\n")
        elif self.luhn_check_full(card_number) != True:
                print('Probably you made mistake in the card number. Please try again!\n')
        elif self.cur.fetchone() == None:
            print('Such a card does not exist.\n')
        else:
            money = int(input('Enter how much money you want to transfer:\n'))
            if money > int(self.check_balance()):
                print('Not enough Money')
            else:
                self.cur.execute('SELECT * FROM card WHERE number = ?', (user_card,))
                self.balance = int([x for x in self.cur.fetchone()][3]) - money
                self.cur.execute('UPDATE card SET balance = ? WHERE number = ?', (self.balance, user_card))
                self.cur.execute('SELECT * FROM card WHERE number = ?', (card_number,))
                new_balance = int([x for x in self.cur.fetchone()][3]) + money
                self.cur.execute('UPDATE card SET balance = ? WHERE number = ?', (new_balance, card_number))
                self.conn.commit()
                print('Succes!\n')

    def close_account(self):
        self.cur.execute('DELETE FROM card WHERE number = ?', (user_card,))
        self.conn.commit()
        print('\nThe account has been closed!\n')

    def logged_in(self):
        while True:
            print('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
            self.user_choice = input()
            if new_user.user_choice == '0':
                print('\nBye!')
                self.conn.close()
                exit()
            elif new_user.user_choice == '1':
                new_user.check_balance()
                print('\nBalance: ' + new_user.balance + '\n')
            elif new_user.user_choice == '2':
                new_user.add_money()
            elif new_user.user_choice == '3':
                new_user.do_transfer()
            elif new_user.user_choice == '4':
                new_user.close_account()
                break
            elif new_user.user_choice == '5':
                print('\nYou have successfully logged out!\n')
                break

while True:
    print('''1. Create an account
2. Log into account
0. Exit''')
    new_user = UserAccount()
    new_user.db_connection()
    user_choice = input()
    if user_choice == '0':
        print('\nBye!')
        new_user.conn.close()
        break
    if user_choice == '1':
        print('\nYour card has been created')
        new_user.store(new_user.generate_card(), new_user.generate_pin())
        print('Your card number:')
        print(new_user.card_number)
        print('Your card pin:')
        print(new_user.pin_no + '\n')
    elif user_choice == '2':
        user_card = input('\nEnter your card number:\n')
        user_pin= input('Enter your pin number:\n')
        if new_user.check_card(user_card, user_pin):
            print('You have successfully logged in!\n')
            new_user.logged_in()
        else:
            print('\nWrong card number or PIN!\n')