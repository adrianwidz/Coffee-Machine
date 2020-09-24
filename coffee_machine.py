# Write your code here
class CoffeeMachine:
    def __init__(self, cash, water, milk, coffee_beans, disposable_cups):
        self.cash = cash
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.mode = "choosing an action"
        self.filling_step = 1

    def print_state(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, " of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.cash, "of money")
        print()

    def make_coffee(self, needed_water, needed_milk, needed_coffee_beans, needed_cash):
        self.mode = "choosing an action"
        if self.water - needed_water < 0:
            print("Sorry, not enough water!")
            print()
        elif self.milk - needed_milk < 0:
            print("Sorry, not enough milk!")
            print()
        elif self.coffee_beans - needed_coffee_beans < 0:
            print("Sorry, not enough coffee beans!")
            print()
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            print()
        else:
            self.water -= needed_water
            self.milk -= needed_milk
            self.coffee_beans -= needed_coffee_beans
            self.disposable_cups -= 1
            self.cash += needed_cash
            print("I have enough resources, making you a coffee!")
            print()

    def buy_coffee(self, coffee_option):
        if coffee_option == "1":
            self.make_coffee(250, 0, 16, 4)
        elif coffee_option == "2":
            self.make_coffee(350, 75, 20, 7)
        elif coffee_option == "3":
            self.make_coffee(200, 100, 12, 6)
        elif coffee_option == "back":
            self.mode = "choosing an action"
            print()

    def fill(self, add):
        if self.filling_step == 1:
            self.water += int(add)
            self.filling_step = 2
        elif self.filling_step == 2:
            self.milk += int(add)
            self.filling_step = 3
        elif self.filling_step == 3:
            self.coffee_beans += int(add)
            self.filling_step = 4
        elif self.filling_step == 4:
            self.disposable_cups += int(add)
            self.filling_step = 1
            self.mode = "choosing an action"
            print()

    def take(self):
        print("I gave you", self.cash)
        print()
        self.cash = 0

    def action(self, action):
        if self.mode == "choosing an action":
            if action == "exit":
                self.mode = "off"
            elif action == "buy":
                self.mode = "choosing a type of coffee"
            elif action == "fill":
                self.mode = "filling"
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.print_state()
        elif self.mode == "choosing a type of coffee":
            self.buy_coffee(action)
        elif self.mode == "filling":
            self.fill(action)

    def interface(self):
        while self.mode != "off":
            if self.mode == "choosing an action":
                print("Write action (buy, fill, take, remaining, exit):")
            elif self.mode == "choosing a type of coffee":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif self.mode == "filling":
                if self.filling_step == 1:
                    print("Write how many ml of water do you want to add:")
                elif self.filling_step == 2:
                    print("Write how many ml of milk do you want to add:")
                elif self.filling_step == 3:
                    print("Write how many grams of coffee beans do you want to add:")
                elif self.filling_step == 4:
                    print("Write how many disposable cups of coffee do you want to add:")
            self.action(input("> "))
            print()


coffee_machine = CoffeeMachine(550, 400, 540, 120, 9)
coffee_machine.interface()




