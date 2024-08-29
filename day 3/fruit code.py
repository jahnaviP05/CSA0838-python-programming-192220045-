def display_fruit(choice):
    """Display the corresponding fruit based on user choice."""
    if choice == 'A':
        return 'Apple'
    elif choice == 'B':
        return 'Banana'
    elif choice == 'C':
        return 'Coconut'
    else:
        return 'Invalid choice'
user_choice = input("Enter 'A', 'B', or 'C': ").upper()
print(display_fruit(user_choice))
