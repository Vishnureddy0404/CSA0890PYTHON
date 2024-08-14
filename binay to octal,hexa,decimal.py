def binary_to_decimal(binary_number):
    return int(binary_number, 2)
def binary_to_hexadecimal(binary_number):
    return hex(int(binary_number, 2)).replace("0x", "").upper()
def binary_to_octal(binary_number):
    return oct(int(binary_number, 2)).replace("0o", "")
binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_number)
hexadecimal_number = binary_to_hexadecimal(binary_number)
octal_number = binary_to_octal(binary_number)
print(f"Binary number: {binary_number}")
print(f"Decimal equivalent: {decimal_number}")
print(f"Hexadecimal equivalent: {hexadecimal_number}")
print(f"Octal equivalent: {octal_number}")
