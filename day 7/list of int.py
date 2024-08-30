def process_numbers():
    numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
    print(['over' if num > 100 else num for num in numbers])
process_numbers()
