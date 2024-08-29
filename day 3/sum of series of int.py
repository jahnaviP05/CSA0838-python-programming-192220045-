total_sum = 0
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        if number <= 100:
            total_sum += number
    except ValueError:
        pass
print(f"Total sum: {total_sum}")
