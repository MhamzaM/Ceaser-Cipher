def EncryptCeaserCipher(plainText):

    plainText = list(plainText)
    for j in range(len(plainText)):

        if plainText[j] == 'z':
            plainText[j] = 'c'
            
        elif plainText[j] == 'Z':
            plainText[j] = 'C'
        
        elif plainText[j] == 'y':
            plainText[j] = 'b'
            
        elif plainText[j] == 'Y':
            plainText[j] = 'B'

        elif plainText[j] == 'x':
            plainText[j] = 'a'
            
        elif plainText[j] == 'X':
            plainText[j] = 'A'

        elif plainText[j] == ' ':
            continue 

        else:
            plainText[j] = chr(ord(plainText[j]) + 3)


    plainText = "".join(plainText)
    return plainText



def DecryptCeaserCipher(cipherText):

    cipherText = list(cipherText)

    for j in range(len(cipherText)):

        if cipherText[j] == 'a':
            cipherText[j] = 'x'
            
        elif cipherText[j] == 'A':
            cipherText[j] = 'X'
        
        elif cipherText[j] == 'b':
            cipherText[j] = 'y'
            
        elif cipherText[j] == 'B':
            cipherText[j] = 'Y'

        elif cipherText[j] == 'c':
            cipherText[j] = 'z'
            
        elif cipherText[j] == 'C':
            cipherText[j] = 'Z'

        elif cipherText[j] == ' ':
            continue 

        else:
            cipherText[j] = chr(ord(cipherText[j]) - 3)


    cipherText = "".join(cipherText)
    return cipherText



        

print("Enter String to convert into ceaser cipher.\n")
plainText = input()

print("Encrypting\n")

cipherText = EncryptCeaserCipher(plainText)
print("Plain Text: " + plainText)
print("Ciper Text: " + cipherText)
        

print("\nDecrypting\n")

print(DecryptCeaserCipher(cipherText))

