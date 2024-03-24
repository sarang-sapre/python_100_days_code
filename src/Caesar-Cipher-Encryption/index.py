alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift,direction):
    cipher_text = []
    for i in text:
        cipher_text.append(alphabet[(alphabet.index(i)+shift)%26])
    end_text = ''.join(map(str, cipher_text))
    print(f"Here's the {direction}d result: {end_text}")

def decrypt(text,shift,direction):
    cipher_text = []
    for i in text:
        cipher_text.append(alphabet[(alphabet.index(i)-shift)%26])
    end_text = ''.join(map(str, cipher_text))
    print(f"Here's the {direction}d result: {end_text}")

if(direction == 'encode') :
    encrypt(text,shift,direction)
elif(direction == 'decode') :
    decrypt(text,shift,direction)
else :
    print("Wrong Direction")


