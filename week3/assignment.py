def encrypt(plaintext):

    # Erstelle ein Dictionary mit der Caesar-Verschlüsselung.
    caesar_cipher = {
        "a": "f",
        "b": "g",
        "c": "h",
        "d": "i",
        "e": "j",
        "f": "k",
        "g": "l",
        "h": "m",
        "i": "n",
        "j": "o",
        "k": "p",
        "l": "q",
        "m": "r",
        "n": "s",
        "o": "t",
        "p": "u",
        "q": "v",
        "r": "w",
        "s": "x",
        "t": "y",
        "u": "z",
        "v": "a",
        "w": "b",
        "x": "c",
        "y": "d",
        "z": "e",
    }

    encrypted_text = ""
    for char in plaintext:
        if char in caesar_cipher:
            encrypted_char = caesar_cipher[char]
        else:
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text


def main():

    plaintext = input("Please enter a sentence: ")

    plaintext = plaintext.lower()

    encrypted_text = encrypt(plaintext)

    print("The encrypted sentence is:", encrypted_text)


if __name__ == "__main__":
    main()