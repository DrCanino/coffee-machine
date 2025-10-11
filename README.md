# ☕ coffee-machine
A console-based simulation program that models the operation of an automated coffee machine. The system manages internal resources — water, milk, coffee beans, sugar, disposable cups, and cash balance — and processes user requests for three coffee types: espresso, latte, and cappuccino.
This project demonstrates basic programming logic, resource management, and user interaction — perfect for practicing control flow, functions, and state handling.


# Stage 2

## Description
A real coffee machine doesn't have an infinite supply of water, milk, or coffee beans. And if you input a really big number, it's almost certain that a real coffee machine wouldn't have the supplies needed to make all that coffee for you.

In this stage, you need to improve the previous program. Now you will check amounts of water, milk, and coffee beans available in your coffee machine at the moment.

# Objectives
Write a program that does the following:

1.It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.

2.If the coffee machine has enough supplies to make the specified amount of coffee, the program should print "Yes, I can make that amount of coffee".

3.If the coffee machine can make more than that, the program should output "Yes, I can make that amount of coffee (and even N more than that)", where N is the number of additional cups of coffee that the coffee machine can make.

4.If the amount of given resources is not enough to make the specified amount of coffee, the program should output "No, I can make only N cups of coffee".

Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk, and 15 g of coffee beans to make one cup of coffee.





# Stage 1

Let's start with a program that makes you a coffee – virtual coffee, of course. In this project, you will implement functionality that simulates a real coffee machine. It can run out of ingredients, such as milk or coffee beans, it can offer you various types of coffee, and, finally, it will take money for the prepared drink.

## Objective
The first version of the program just makes you a coffee. It should print to the standard output what it is doing as it makes the drink.