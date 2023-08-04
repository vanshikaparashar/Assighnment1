def print_table(limit):
    for i in range(1, limit + 1):
        result = 2 * i
        print(f"2 x {i} = {result}")


try:
    user_input = int(input("Enter the limit for the table of 2: "))
    print_table(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

