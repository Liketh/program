plain = input("Enter plaintext: ").replace(" ", "")
ciphertext = input("Enter ciphertext: ")


def cipher_encrypt(plain, key):
  
    result = ""
    
    matrix = [["" for x in range(len(plain))] for y in range(key)]

    increment = 1
    row = 0
    col = 0

    for c in plain:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1

        matrix[ row ][ col ] = c

        row += increment
        col += 1

    for list in matrix:
        result += "".join(list)
    return result

for i in range(1, 100):
    res = cipher_encrypt(plain, i)
    if res == ciphertext:
        print(i)
        break