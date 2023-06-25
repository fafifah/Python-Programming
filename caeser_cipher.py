alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)
'''direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(text,shift):
  encrypt_word = ''
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    if new_position > 26:
      new_position = new_position-26
      new_word = alphabet[new_position]
      encrypt_word += new_word
      
    else:
      new_word = alphabet[new_position]
      encrypt_word += new_word
  print(f"The encrypted word is {encrypt_word}")

def decrypt(text,shift):
  decrypt_word = ''
  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift
    new_word = alphabet[new_position]
    decrypt_word += new_word
  print(f"The decrypted word is {decrypt_word}")

if direction == 'encode':
  encrypt(text,shift)
elif direction == 'decode':
  decrypt(text,shift)'''

# combining encode and decode
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  # combining encode and decode
  def caesar(text,shift,direction):
    crypted_word = ''
    if direction == 'decode':
      shift *= -1
    for letter in text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift % 26
        new_word = alphabet[new_position]
        crypted_word += new_word
      else:
        crypted_word += letter
        
        
        
    print(f"The {direction}d word is {crypted_word}")
  
  caesar(text,shift,direction)

  response = input("Do you want to continue? Type 'yes' or 'no'").lower()

  if response == 'yes':
    should_continue = True
  elif response == 'no':
    should_continue = False
    print("Goodbye!")