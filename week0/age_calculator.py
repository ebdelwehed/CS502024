
current_year = 2025

def main():
    birth_year = int(input("What year were you born? "))
    calculate_age(current_year - birth_year)

def calculate_age(age):
    print(f"You are {age} years old")
    
main()