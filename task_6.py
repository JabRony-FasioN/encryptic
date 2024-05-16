def subtract(num1, num2):
    # Дополнение чисел нулями слева, чтобы сделать их одинаковой длины
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    result = ''
    borrow = 0

    for i in range(max_len - 1, -1, -1):
        diff = int(num1[i]) - int(num2[i]) - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result = str(diff) + result

    return result.lstrip('0')

def multiply_by_digit(num, digit):
    result = ''
    carry = 0

    for i in range(len(num) - 1, -1, -1):
        product = int(num[i]) * digit + carry
        result = str(product % 10) + result
        carry = product // 10

    if carry:
        result = str(carry) + result

    return result

# Пример использования
num1 = "1234567890123456789"
num2 = "9876543210"

# Вычитание
print(subtract(num1, num2))

# Умножение на цифру
digit = 7
print(multiply_by_digit(num1, digit))
