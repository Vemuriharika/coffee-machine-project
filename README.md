# coffee-machine-project

# ☕ Coffee Machine Simulator

## Overview

The **Coffee Machine Simulator** is a Python-based console application that simulates the functionality of a real-world coffee vending machine. Developed using **Object-Oriented Programming (OOP)** principles, the application allows users to order beverages, validates resource availability, processes coin-based payments, and updates machine resources after each successful transaction.

This project demonstrates modular programming, clean code organization, and the practical implementation of OOP concepts in Python.



## Features

* Multiple beverage options:

  * Espresso
  * Latte
  * Cappuccino
* Resource availability verification before preparing a drink
* Coin-based payment processing
* Automatic change calculation
* Profit tracking
* Real-time resource reporting
* Resource deduction after each successful order
* Handles invalid selections, insufficient resources, and insufficient payment



## Project Structure

coffee-machine/

│

├── main.py              # Application entry point

├── menu.py              # Menu and MenuItem classes

├── coffee_maker.py      # CoffeeMaker class for resource management

├── money_machine.py     # MoneyMachine class for payment processing

└── README.md            # Project documentation


## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)


## System Components

### MenuItem

Represents an individual beverage available in the coffee machine. Each menu item contains:

* Beverage name
* Required water quantity
* Required milk quantity
* Required coffee quantity
* Cost

### Menu

Maintains the list of available beverages and provides methods to:

* Display available menu items
* Retrieve beverage details based on user input

### CoffeeMaker

Responsible for managing machine resources by:

* Monitoring available ingredients
* Verifying resource sufficiency
* Preparing beverages
* Updating resource levels after each order

### MoneyMachine

Handles all payment-related operations, including:

* Accepting coin inputs
* Calculating the total amount received
* Validating payments
* Returning change
* Tracking total profit


## Application Workflow

1. Display available beverage options.
2. Accept the user's selection.
3. Verify sufficient resources are available.
4. Accept coin inputs from the user.
5. Validate the payment.
6. Dispense the selected beverage.
7. Deduct the required ingredients from the available resources.
8. Update the total profit.


## Sample Execution


What would you like? (latte/espresso/cappuccino): latte

Please insert coins.

How many quarters?: 10

How many dimes?: 0

How many nickles?: 0

How many pennies?: 0

Here is $0.00 in change.

Here is your latte ☕️. Enjoy!


## Available Commands

| Command    | Description                                             |
| ---------- | ------------------------------------------------------- |
| latte      | Orders a Latte                                          |
| espresso   | Orders an Espresso                                      |
| cappuccino | Orders a Cappuccino                                     |
| report     | Displays the current machine resources and total profit |
| off        | Terminates the application                              |



## Learning Outcomes

This project reinforces the following Python programming concepts:

* Object-Oriented Programming
* Class and Object Design
* Constructors (`__init__`)
* Encapsulation
* Dictionaries and Lists
* Loops and Conditional Statements
* Modular Programming
* User Input Handling
* Resource Management
* Payment Processing Logic



## Future Enhancements

Potential improvements include:

* Support for additional beverage options
* Persistent storage for sales history
* Graphical User Interface (GUI) using Tkinter or PyQt
* Database or JSON-based menu management
* Digital receipt generation
* Inventory refill functionality
* Unit testing and exception handling



## Conclusion

The Coffee Machine Simulator provides a practical implementation of Object-Oriented Programming concepts while simulating the core functionality of an automated coffee vending machine. The project emphasizes modular design, maintainability, and clean code practices, making it an excellent learning project for Python developers interested in building interactive console applications.
