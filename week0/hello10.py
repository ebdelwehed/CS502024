# Demonstrates defining a function with a parameter with a default value
def hello(to="world"):
    print(f"Hello, {to}!")
hello()
name = input("What is your name? ")
hello(name)
