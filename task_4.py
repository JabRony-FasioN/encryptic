import random

def generate_keyword(key):
    # Удаляем повторяющиеся символы в ключе
    key = ''.join(sorted(set(key), key=key.index))
    # Дополняем ключ алфавитом
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for char in alphabet:
        if char not in key:
            key += char
    return key

def build_polybius_square(keyword):
    # Создаем квадрат Полибия с использованием ключевого слова
    square = [['' for _ in range(6)] for _ in range(6)]
    chars = list(keyword) + [chr(i) for i in range(65, 91) if chr(i) != 'J']
    for i in range(6):
        for j in range(6):
            square[i][j] = chars[i*6 + j]
    return square

def encrypt(message, keyword):
    keyword = generate_keyword(keyword)
    square = build_polybius_square(keyword)
    encrypted = ''
    for char in message.upper():
        if char == 'J':
            char = 'I'
        for i in range(6):
            for j in range(6):
                if square[i][j] == char:
                    encrypted += 'ADFGVX'[i] + 'ADFGVX'[j]
    return encrypted

# Пример использования функции
message = 'HELlllllLO'
keyword = 'KEYWORD'
encrypted_message = encrypt(message, keyword)
print(encrypted_message)
