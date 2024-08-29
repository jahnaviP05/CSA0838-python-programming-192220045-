def display_powers_of_2(n):
    """Display powers of 2 from 2^1 to 2^n."""
    for i in range(1, n + 1):
        print(f"2^{i} = {2**i}")
n = int(input("Enter the value of n: "))
display_powers_of_2(n)
