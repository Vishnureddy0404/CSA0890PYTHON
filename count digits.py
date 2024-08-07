def count_digits():
    number = int(input("Enter a number: "))
    original_number = number  
    count = 0
    while number != 0:
        number = number // 10
        count += 1
    print(f"The number of digits in {original_number} is {count}.")
count_digits()
