def calculate_total_amount(denominations, notes):
    total_amount = 0
    for denom, count in zip(denominations, notes):
        total_amount += denom * count
    return total_amount
denominations_input = input("Enter the denominations:")
denominations = list(map(int, denominations_input.split()))
notes_input = input(f"Enter the number of notes for each denomination as the order({' '.join(map(str, denominations))}): ")
notes = list(map(int, notes_input.split()))
total_amount = calculate_total_amount(denominations, notes)
print(f"The total available balance in the ATM machine is:{total_amount}")

