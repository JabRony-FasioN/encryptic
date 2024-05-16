from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(input_file, 'rb') as file_in:
        with open(output_file, 'wb') as file_out:
            while True:
                chunk = file_in.read(16) # Считываем 16 байт
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk = pad(chunk, 16) # Дополняем последний блок до 16 байт
                encrypted_chunk = cipher.encrypt(chunk)
                file_out.write(encrypted_chunk)

def decrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(input_file, 'rb') as file_in:
        with open(output_file, 'wb') as file_out:
            while True:
                chunk = file_in.read(16) # Считываем 16 байт
                if len(chunk) == 0:
                    break
                decrypted_chunk = cipher.decrypt(chunk)
                decrypted_chunk = unpad(decrypted_chunk, 16) # Удаляем дополнение
                file_out.write(decrypted_chunk)

# Пример использования
key = b'0123456789abcdef' # 16-байтный ключ
input_file = 'input.txt'
encrypted_file = 'encrypted.bin'
decrypted_file = 'decrypted.txt'

# Шифрование файла
encrypt_file(input_file, encrypted_file, key)
print('Файл успешно зашифрован и сохранен в encrypted.bin')

# Дешифрование файла
decrypt_file(encrypted_file, decrypted_file, key)
print('Файл успешно дешифрован и сохранен в decrypted.txt')
