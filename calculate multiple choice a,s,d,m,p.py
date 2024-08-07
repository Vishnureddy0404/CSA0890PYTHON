def pow_x_n(x,n):
    return x ** n
def add_x_n(x,n):
    return x + n
def sub_x_n(x,n):
    return x - n
def mul_x_n(x,n):
    return x * n
def div_x_n(x,n):
    if n==0:
        return "Division by zero is not allowed"
    return x/n
x = float(input("enter the value of X:"))
n = float(input("enter the value of N:"))

print("choose an operation:")
print("1: pow(X,N)")
print("2: add(X,N)")
print("3: sub(X,N)")
print("4: mul(X,N)")
print("5: div(X,N)")

choice = int(input("Enter your choice:"))

if choice == 1:
    result = pow_x_n(x,n)
    operator = "pow(X,N)"
elif choice == 2:
    result = add_x_n(x,n)
    operator = "add(X,N)"
elif choice == 3:
    result = sub_x_n(x,n)
    operator = "sub(X,N)"
elif choice == 4:
    result = mul_x_n(x,n)
    operator = "mul(X,N)"
elif choice == 5:
    result = div_x_n(x,n)
    operator = "div(X,N)"
else:
    print("Invalid choice:")
    result = None
    operator = None

if result is not None:
    print(f"{operator}={result}")
