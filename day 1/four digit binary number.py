binary_digits = [int(input(f"Enter binary digit {i+1}: ")) for i in range(4)]
decimal_value = sum(digit * (2 ** (3 - i)) for i, digit in enumerate(binary_digits))
print(f"The decimal value is {decimal_value}")
