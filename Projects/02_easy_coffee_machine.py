class CoffeeMachine:
    current_state = 'choose'

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.coffee_water = [250, 350, 200]
        self.coffee_milk = [0, 75, 100]
        self.coffee_beans = [16, 20, 12]

    def user_input(self, action):
        if action == 'buy':
            self.current_state = 'buy'
        elif action == 'exit':
            self.current_state = 'exit'
        elif action == 'back':
            self.current_state = 'back'
        elif action == 'fill':
            self.current_state = 'fill'
        elif action == 'remaining':
            self.current_state = 'remaining'
        elif action == 'take':
            self.current_state = 'take'

    def buy(self, action):
        if self.cups == 0:
            self.current_state = 'choose'
            print('Sorry, not enough cups!')
        else:
            if action == '1':
                if self.water > self.coffee_water[0] and self.beans > self.coffee_beans[0]:
                    print('I have enough resources, making you a coffee!')
                    self.water -= self.coffee_water[0]
                    self.beans -= self.coffee_beans[0]
                    self.cups -= 1
                    self.money += 4
                    self.current_state = 'choose'
                else:
                    if self.water < self.coffee_water[0]:
                        print('Sorry, not enough water!')
                    elif self.beans < self.coffee_beans[0]:
                        print('Sorry, not enough coffee beans!')
                    self.current_state = 'choose'
            elif action == '2':
                if self.water > self.coffee_water[1] and self.milk > self.coffee_milk[1] and self.beans > self.coffee_beans[1]:
                    print('I have enough resources, making you a coffee!')
                    self.water -= self.coffee_water[1]
                    self.milk -= self.coffee_milk[1]
                    self.beans -= self.coffee_beans[1]
                    self.cups -= 1
                    self.money += 7
                    self.current_state = 'choose'
                else:
                    if self.water < self.coffee_water[1]:
                        print('Sorry, not enough water!')
                    elif self.milk < self.coffee_milk[1]:
                        print('Sorry, not enough milk!')
                    elif self.beans < self.coffee_beans[1]:
                        print('Sorry, not enough coffee beans!')
                    self.current_state = 'choose'
            elif action == '3':
                if self.water > self.coffee_water[2] and self.milk > self.coffee_milk[2] and self.beans > self.coffee_beans[2]:
                    print('I have enough resources, making you a coffee!')
                    self.water -= self.coffee_water[2]
                    self.milk -= self.coffee_milk[2]
                    self.beans -= self.coffee_beans[2]
                    self.cups -= 1
                    self.money += 6
                    self.current_state = 'choose'
                else:
                    if self.water < self.coffee_water[2]:
                        print('Sorry, not enough water!')
                    elif self.milk < self.coffee_milk[2]:
                        print('Sorry, not enough milk!')
                    elif self.beans < self.coffee_beans[2]:
                        print('Sorry, not enough coffee beans!')
                    self.current_state = 'choose'
            elif action == 'back':
                self.current_state = 'choose'

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.beans += int(input('Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))
        self.current_state = 'choose'

    def remaining(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.money, 'of money')
        self.current_state = 'choose'

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        self.current_state = 'choose'


the_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    if the_machine.current_state == 'choose':
        print('Write action (buy, fill, take, remaining, exit):')
        the_machine.user_input(input())
    elif the_machine.current_state == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        the_machine.buy(input())
    elif the_machine.current_state == 'fill':
        the_machine.fill()
    elif the_machine.current_state == 'remaining':
        the_machine.remaining()
    elif the_machine.current_state == 'take':
        the_machine.take()
    elif the_machine.current_state == 'exit':
        # print('Thank you for using our coffee machine!')
        break