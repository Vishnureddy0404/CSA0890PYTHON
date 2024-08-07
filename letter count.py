word=input("enter the string:")
letter_count={}
repeated_letters=[]
for letter in word:
    if letter in letter_count:
        letter_count[letter]+=1
    else:
        letter_count[letter]=1
repeated_count=0
for letter in letter_count:
    if letter_count[letter]>1:
        repeated_letters.append(letter)
        repeated_count+=1
print(repeated_count)
print(repeated_letters)
