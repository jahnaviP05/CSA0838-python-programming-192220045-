def count_letter_a(names):
    return sum(name.lower().count('a') for name in names)

def main():
    names = input("Enter a list of first names separated by spaces: ").split()
    print(f"The letter 'a' appears {count_letter_a(names)} times.")
main()
