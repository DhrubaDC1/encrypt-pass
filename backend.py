def addEncrypt (pas, met, am):
    enc = int((pas + am - 32) % 128)
    return enc


def addDecrypt (pas, met, am):
    enc = int((pas - am + 32) % 128)
    return enc


print("Welcome to the bridge of Security: \nYou can Encrypt as well as Decrypt your password and save it safely")
sel = int(input("Which one do you want?\n1. Encryption\n2. Decryption\n"))
if sel == 1:
    print("Encryption: ")
    x = input("Enter your Password\n")
    old = (list(x))
    s = int(input("Which encryption method do you want?\n1. Addition\n2. Multiplication\n"))
    print("You have selected ", end="")
    if s == 1:
        q = int(input("Addition\nHow much Addition do you want?\n"))
    else:
        q = int(input("Multiplication\nThis is not yet available. Coming Soon"))
    count = 0
    for i in old:
        old[count] = chr(addEncrypt(ord(i), 1, q))
        count = count + 1

    print("Encrypting\n==========\nEncryption Done\nYour Encrypted Key: ", end="")
else:
    print("Decryption: ")
    x = input("Enter your Encrypted Key\n")
    old = list(x)
    s = int(input("Which encryption method did you use?\n1. Addition\n2. Multiplication\n"))
    print("You have selected ", end="")
    if s == 1:
        q = int(input("Addition\nHow much amount did you add?\n"))
    else:
        q = int(input("Multiplication\nThis is not yet available. Coming Soon"))
    count = 0
    for i in old:
        old[count] = chr(addDecrypt(ord(str(i)), 1, q))
        count = count + 1
    print("Decrypting\n==========\nDecryption Done\nYour Encrypted Key: ", end="")
new = ""
for i in old:
    new = new + i
print(new)