from graphic import logo

def rotate_alphabet(alphabet, shift):
    """This method is using the same strategy as original Caesar cipher: 
    Two alignet discs with alphabet, smaller one is rotating and changing positions 
    according to the selected shift. 
    Then we have new order in which original letter corresponds to new letter and shift is the
    key to encrypt or decrypt the letter."""
    return alphabet[shift:] + alphabet[:shift]

def encrypt(text, shift, alphabet):
    new_alphabet = rotate_alphabet(alphabet, shift)
    
    encrypted_word = ""
    word_indexed = [] # original word indexed

    for letter in text:
        word_indexed.append(alphabet.index(letter))
    for idx in word_indexed:
        encrypted_word += new_alphabet[idx]
    
    print(encrypted_word)
    
def decrypt(text, shift, alphabet):
    new_alphabet = rotate_alphabet(alphabet, shift)

    decrypted_word = ""
    word_index = [] 

    for letter in text:
        word_index.append(alphabet.index(letter))
    for idx in word_index:
        decrypted_word += new_alphabet[idx]

    print(decrypted_word)

def main():    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " "]
    print(logo)

    finish_task = False

    while not finish_task:
        direction = input("Type operation required -> (encode OR decode)\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number: ABS(1-25):\n"))  
        if direction == "encode":
            encrypt(text, shift, alphabet)
            task = input("Do you want to continue? (yes/no): ") 
        elif direction == "decode":
            decrypt(text, shift, alphabet)
            task = input("Do you want to continue? (yes/no): ")
        elif direction != "encode" and direction != "decode":
            print("Wrong key word!")
            task = input("Do you want to continue? (yes/no): ")

        if task == "no":
            finish_task = True
            print("Goodbye")

if __name__ == "__main__":
    main()