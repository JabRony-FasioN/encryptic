matrix = [
    ['а', 'б', 'в', 'г', 'д', 'е'],
    ['ё', 'ж', 'з', 'и', 'й', 'к'],
    ['л', 'м', 'н', 'о', 'п', 'р'],
    ['с', 'т', 'у', 'ф', 'х', 'ц'],
    ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь']
]

# Функция для дешифрования текста методом Плейфера
def decrypt(text):
    decrypted_text = ""
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]

        row1, col1 = divmod(decrypted_text.index(char1), 6)
        row2, col2 = divmod(decrypted_text.index(char2), 6)

        if col1 == col2:
            decrypted_text += matrix[row1 - 1][col1]
            decrypted_text += matrix[row2 - 1][col1]
        elif row1 == row2:
            decrypted_text += matrix[row1][col1 - 1]
            decrypted_text += matrix[row1][col2 - 1]
        else:
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]

    return decrypted_text

# Пример использования дешифрования
cipher_text = "дкпглбрдпбт"
decrypted_text = decrypt(cipher_text)
print("Расшифрованный текст:", decrypted_text)