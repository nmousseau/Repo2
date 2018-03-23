mystring = "TCATCCGACGCCGAGGCTAATAGCAATTGACGTGGGTAGTACCTAGGGTAACATTACATGGACC"
count_A = 0
count_C = 0
count_G = 0
count_T = 0
add = 0
for letter in mystring:
    if letter == 'A':
        count_A += 1
    if letter == 'C':
        count_C += 1
    if letter == 'G':
        count_G += 1
    if letter == 'T':
        count_T += 1
    add += 1

#add = count_A + count_C + count_G + count_T
print(str(add) + " Total entries")
#print(add + " Total entries")

divide = count_A / add
multiply = divide * 100
print(str(multiply) + " % are A's")

divide = count_C / add
multiply = divide * 100
print(str(multiply) + " % are C's")

divide = count_G / add
multiply = divide * 100
print(str(multiply) + " % are G's")

divide = count_T / add
multiply = divide * 100
print(str(multiply) + " % are T's")




