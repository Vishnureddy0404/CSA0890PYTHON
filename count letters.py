paragraph = """This is the first line.
This is the second line.
And here is the third line."""
lines = paragraph.split('\n')
line_count = 0
for line in lines:
    words = line.split()
    word_count = len(words)
    print("line",line_count+1,"no of words",word_count)
    line_count += 1
print("the no of lines:",line_count)
