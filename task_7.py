import math,random

def generate_key(password):
    char_set = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # Символы, по которым будет строиться ключ
    char_map = {char: str(index) for index, char in enumerate(char_set)}

    password_value = sum([int(char_map[char]) for char in password])

    # Переводим пароль в число и извлекаем из него квадратный корень
    key = math.isqrt(password_value)

    # Если ключ рациональный, добавляем 1 и извлекаем квадратный корень снова
    while math.sqrt(key) % 1 == 0:
        key += 1
        key = math.isqrt(key)

    return key

def encrypt(text, key):
    encrypted_text = ''
    key_len = len(str(key))
    key_index = 0

    for char in text:
        encrypted_char = chr(ord(char) + int(str(key)[key_index]))
        encrypted_text += encrypted_char
        key_index = (key_index + 1) % key_len
        
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ''
    key_len = len(str(key))
    key_index = 0

    for char in text:
        decrypted_char = chr(ord(char) - int(str(key)[key_index]))
        decrypted_text += decrypted_char
        key_index = (key_index + 1) % key_len

    return decrypted_text

# Основной цикл приложения
while True:
    print("\nМеню:")
    print("1) Зашифровать текст, используя ключ")
    print("2) Дешифровать текст, используя ключ")
    print("3) Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        password = input("Введите ключевое слово (от 4 до 20 символов): ")
        key = generate_key(password)
        text = input("Введите текст для шифрования (до 100 символов): ")
        encrypted_text = encrypt(text, key)
        print(f"Зашифрованный текст: {encrypted_text}")

    elif choice == '2':
        password = input("Введите ключевое слово (от 4 до 20 символов): ")
        key = generate_key(password)
        text = input("Введите текст для дешифрования: ")
        decrypted_text = decrypt(text, key)
        print(f"Расшифрованный текст: {decrypted_text}")

    elif choice == '3':
        print("Выход из программы.")
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
