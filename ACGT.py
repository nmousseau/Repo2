mystring = "TCATCCGACGCCGAGGCTAATAGCAATTGACGTGGGTAGTACCTAGGGTAACATTACATGGACC"
count_A = 0
count_C = 0
count_G = 0
count_T = 0
for letter in mystring:
    if letter == 'A':
        count_A += 1
    if letter == 'C':
        count_C += 1
    if letter == 'G':
        count_G += 1
    if letter == 'T':
        count_T += 1

add = count_A + count_C + count_G + count_T
print(add)

divide = count_A / add
multiply = divide * 100
print("the % of A's is")
print(multiply)

divide = count_C / add
multiply = divide * 100
print("the % of C's is")
print(multiply)

divide = count_G / add
multiply = divide * 100
print("the % of G's is")
print(multiply)

divide = count_T / add
multiply = divide * 100
print("the % of T's is")
print(multiply)




