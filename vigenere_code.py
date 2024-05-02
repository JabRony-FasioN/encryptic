import re

def encrypt_vigenere(text, key):
    text = text.upper()
    text = re.sub(r'[^А-Я]', '', text)
    key = key.upper()
    encrypted_text = ""
    
    for i, char in enumerate(text):
        shift = ord(key[i % len(key)]) - ord('А')
        encrypted_char = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
        encrypted_text += encrypted_char
    
    return encrypted_text


text = "Пример текста для шифрования"
key = "КРИПТО"

encrypted_text = encrypt_vigenere(text, key)
print(encrypted_text)


##########################



def decrypt_vigenere(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    decrypted_text = ""
    
    for i, char in enumerate(encrypted_text):
        shift = ord(key[i % len(key)]) - ord('А')
        decrypted_char = chr((ord(char) - ord('А') - shift) % 32 + ord('А'))
        decrypted_text += decrypted_char
    
    return decrypted_text


encrypted_text = input("Введите зашифрованную строку: ")
key = input("Введите ключ дешифрования: ")

decrypted_text = decrypt_vigenere(encrypted_text, key)
print(decrypted_text)