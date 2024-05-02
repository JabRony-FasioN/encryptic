import re

def encrypt(input_string, shift):
    input_string = input_string.upper()
    input_string = re.sub('[^А-Я]', '', input_string)
    encrypted_string = ''
    for char in input_string:
        encrypted_string += chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
    return encrypted_string

def decrypt(encrypted_string, shift):
    decrypted_string = ''
    for char in encrypted_string:
        decrypted_string += chr((ord(char) - ord('А') - shift) % 32 + ord('А'))
    return decrypted_string

# Пример использования
input_string = "Пример текста для шифрования"
shift = 3

encrypted_string = encrypt(input_string, shift)
print("Зашифрованная строка:", encrypted_string)

decrypted_string = decrypt(encrypted_string, shift)
print("Расшифрованная строка:", decrypted_string)


################################

def decrypt_caesar(encrypted_text, shift):
    decrypted_text = ""
    
    for char in encrypted_text:
        decrypted_char = chr((ord(char) - ord('А') - shift) % 32 + ord('А'))
        decrypted_text += decrypted_char
    
    return decrypted_text

def crack_caesar(encrypted_text):
    decrypted_texts = []
    
    for shift in range(1, 33):
        decrypted_text = decrypt_caesar(encrypted_text, shift)
        decrypted_texts.append(decrypted_text)
    
    return decrypted_texts

encrypted_text = input("Введите зашифрованную строку: ")

decrypted_texts = crack_caesar(encrypted_text)

for i, decrypted_text in enumerate(decrypted_texts):
    print(f"Ключ сдвига {i+1}: {decrypted_text}")