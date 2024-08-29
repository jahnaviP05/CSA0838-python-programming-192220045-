def count_values():
    positive_count = 0
    negative_count = 0
    
    while True:
        try:
            number = int(input("Enter an integer (or 0 to stop): "))
            if number == 0:
                break
            elif number > 0:
                positive_count += 1
            elif number < 0:
                negative_count += 1
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    return positive_count, negative_count
pos_count, neg_count = count_values()
print(f"Number of positive values: {pos_count}")
print(f"Number of negative values: {neg_count}")
