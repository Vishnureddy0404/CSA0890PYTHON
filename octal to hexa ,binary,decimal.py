def octal_to_decimal(octal_number):
    return int(octal_number, 8)
def octal_to_binary(octal_number):
    return bin(int(octal_number, 8)).replace("0b", "")
def octal_to_hexadecimal(octal_number):
    return hex(int(octal_number, 8)).replace("0x", "").upper()
octal_number = input("Enter an octal number: ")
decimal_number = octal_to_decimal(octal_number)
binary_number = octal_to_binary(octal_number)
hexadecimal_number = octal_to_hexadecimal(octal_number)
print(f"Octal number: {octal_number}")
print(f"Decimal equivalent: {decimal_number}")
print(f"Binary equivalent: {binary_number}")
print(f"Hexadecimal equivalent: {hexadecimal_number}")
