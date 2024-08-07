string = input("Enter the string:")
vowels = "aeiouAEIOU"
length = len(string)
newtext=""
for i in range(length):
    if string[i]not in vowels:
        newtext = string[i]
        print(newtext)
