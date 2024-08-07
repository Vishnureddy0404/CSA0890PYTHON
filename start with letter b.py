paragraph = """This is the first sentence
 But this is the second sentence
Another sentence here
 Be sure to check this one
Better look here too"""
lines=paragraph.split("\n")
b_start_count=0
for line in lines:
    line=line.strip()
    if line.startswith("B"):
        b_start_count+=1
print(b_start_count)
