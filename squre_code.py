def encrypt(input_string, matrix):
    encrypted_string = ''
    for char in input_string:
        found = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if char == matrix[i][j]:
                    encrypted_char = matrix[j][i]  # Сдвиг вправо
                    encrypted_char = matrix[i][(j + 1) % len(matrix[i])]  # Сдвиг вниз
                    encrypted_string += encrypted_char
                    found = True
                    break
            if found:
                break
        if not found:
            encrypted_string += char
    return encrypted_string

# Пример использования
input_string = "ПРИМЕР ШИФРОВАНИЯ КВАДРАТОМ"
matrix = [
    ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё'],
    ['Ж', 'З', 'И', 'Й', 'К', 'Л', 'М'],
    ['Н', 'О', 'П', 'Р', 'С', 'Т', 'У'],
    ['Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ'],
    ['Ы', 'Ь', 'Э', 'Ю', 'Я', '1', '2'],
    ['3', '4', '5', '6', '7', '8', '9'],
    ['0', '!', '@', '#', '$', '%', '^']
]

encrypted_string = encrypt(input_string, matrix)
print("Зашифрованная строка:", encrypted_string)
