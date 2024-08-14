def hexadecimal_to_binary(hexadecimal_number):
    return bin(int(hexadecimal_number, 16)).replace("0b", "")
def hexadecimal_to_octal(hexadecimal_number):
    return oct(int(hexadecimal_number, 16)).replace("0o", "")
hexadecimal_number = input("Enter a hexadecimal number: ")
binary_number = hexadecimal_to_binary(hexadecimal_number)
octal_number = hexadecimal_to_octal(hexadecimal_number)
print(f"Hexadecimal number: {hexadecimal_number}")
print(f"Binary equivalent: {binary_number}")
print(f"Octal equivalent: {octal_number}")
