def analyze_set_elements():
    user_set = set()
    num_elements = int(input("Enter the number of elements for the set: "))

    print("Enter elements (0-9, A-Z, or a-z):")
    for _ in range(num_elements):
        element = input(f"Enter element {_+1}: ")
        if len(element) == 1 and (element.isalnum()):
            user_set.add(element)
        else:
            print("Invalid input. Please enter a single character (0-9, A-Z, or a-z).")

    print("\nSet Elements:", user_set)
    print("Length of the set:", len(user_set))

    digit_count = 0
    lowercase_count = 0
    uppercase_count = 0

    for char in user_set:
        if char.isdigit():
            digit_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1

    print("Count of Digits:", digit_count)
    print("Count of Lowercase Letters:", lowercase_count)
    print("Count of Uppercase Letters:", uppercase_count)

analyze_set_elements()