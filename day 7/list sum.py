def main():
    list1 = list(map(int, input("Enter integers for the first list separated by spaces: ").split()))
    list2 = list(map(int, input("Enter integers for the second list separated by spaces: ").split()))

    print(f"Same length: {len(list1) == len(list2)}")
    print(f"Same sum: {sum(list1) == sum(list2)}")
    print(f"Common elements: {bool(set(list1) & set(list2))}")
main()
