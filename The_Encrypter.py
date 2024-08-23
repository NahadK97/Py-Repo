from ciphers.cipher import *
# abcdefghijklmnopqrstuvwxyz 1234567890 !@#$%^&*()

f = open("codes.txt", "w")
g = open("Crisis_Updates", "r")
message = g.read()  # Message to be encrypted
print("1.Caeser 2.Morse 3.Jumbled 4.Reverse 5. Alpha-Numeric")
choice = input("Enter choice: ")  # Type of encryption
function = input("E/D?: ")  # Encrypt or Decrypt?

if choice == "1":  # For Caeser Cipher
    sh = int(input("Enter shift: "))  # shifting by how much letters
    if function == "E":
        f.write(c_encrypt(message, sh))
    elif function == "D":
        f.write(c_decrypt(message, sh))

elif choice == "2":  # For Morse Code
    #print("Not 100% efficient use an online translator")
    if function == "E":
        f.write(m_encrypt(message))
    elif function == "D":
        f.write(m_decrypt(message))

elif choice == "3":  # For Jumbled
    if function == "E":
        g.seek(0)  # goes to starting of the file
        message = g.readlines()  # makes list of all the lines
        for line in message:  # for each line in the list
            for word in line.split():  # for each word in a line
                jw = jumble(word) + " "
                f.write(jw)
            f.write('\n')
    elif function == "D":
        print("Not possible to decrypt jumbled messages ")

elif choice == "4":  # For Reverse
    if function == "E":
        f.write(reverse(message))
    elif function == "D":
        f.write(reverse(message))

elif choice == "5":  # For Alpha-Numeric
    if function == "E":
        g.seek(0)  # goes to starting of the file
        message = g.readlines()  # makes list of all the lines
        for line in message:  # for each line in the list
            for word in line.split():  # for each word in a line
                jw = alph_num(word) + " / "
                f.write(jw)
            f.write('\n')
    elif function == "D":
        g.seek(0)  # goes to starting of the file
        message = g.readlines()  # makes list of all the lines
        for line in message:  # for each line in the list
            LS = line.split()
            for word in line.split():  # for each word in a line
                jw = num_alph(word)
                f.write(jw)
            f.write('\n')

else:
    print("Error")
f.close()
g.close()
