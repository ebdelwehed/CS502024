# x = 1
# y = 2

# z = x + y

# print(z)

#ask user for what's x ?
# x = input("what's x ?")
# #ask user for what's y ?
# y = input("what's y ?")
# #z holds addition value of x and y
# z = int(x) + int(y)
# #display value of z
# print(z)

#ask user for what's x ?
# x = int(input("what's x ?"))
# #ask user for what's y ?
# y = int(input("what's y ?"))


# #display value 
# print(x + y)

#example of using float.
# x = float(input("what's x ?"))
# y = float(input("what's y ?"))
# print(x + y)

#using float with round function
# x = float(input("what's x ?"))
# y = float(input("what's y ?"))
# # display value of x + y as with comma seperated by 1,000 like this 1,000
# print(f"{x + y:,.)

# x = float(input("what's x ?"))
# y = float(input("what's y ?"))
# z = x / y
# #display value of z rounded to 2 decimal places
# print((f"{z:.2f}")) 

#defining a function called print_hello
def print_hello():
    name = input("What's your name?").strip().capitalize()
    #display hello
    print(f"Hello {name}")
    
#calling the function print_hello
print_hello()