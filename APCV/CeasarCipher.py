#CeasarCipher Assignment APCV 320 Kristin Skipper

def encode(msg, shift):
    new_msg = ""
    # Used a for loop to check each char in msg:
    for i in range(len(msg)):
        ch = msg[i]

        # check if space is there then simply add space
        if ch == " ":
            new_msg += " "
        # check if a character is uppercase then encrypt it accordingly
        elif ch.isupper():  # if the character is an uppercase letter
            # used ord below to convert the unicode char to its integer equivalent
            new_msg += chr((ord(ch) + shift - 65) % 26 + 65)
        # check if a character is digit then leave the way it is then encrypt it accordingly
        elif ch.islower():
            new_msg += chr((ord(ch) + shift - 97) % 26 + 97)
        else:
            new_msg += ch

    return new_msg


msg = input("Enter message to be encrypted: ")
shift_str = input("Enter shift amount (1-25): ")
shift = int(shift_str)
print("Encrypted message: " + encode(msg, shift))
