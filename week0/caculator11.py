# Demonstrates defining a function with a return value

def main():
    x = int(input("what's x squared? "))
    print("x squared is", square(x))
    square(x)
def square(n):
    return n * n
main()