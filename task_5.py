import re
from collections import Counter

with open('temp.txt', 'r') as texter:
    
    text = texter.read()  # Замените на ваш текст

text = text.lower()

letters_count = Counter(re.findall(r'[а-я]', text))
pairs_count = Counter(re.findall(r'(?=([а-я]{2}))', text))

total_letters = sum(letters_count.values())
total_pairs = sum(pairs_count.values())
print('total_pairs')
letters_frequency = {letter: count / total_letters for letter, count in letters_count.items()}
pairs_frequency = {pair: count / total_pairs for pair, count in pairs_count.items()}

zero_occurrence_pairs = [pair for pair, count in pairs_count.items() if count == 0]

less_than_3_occurrences_pairs = [pair for pair, count in pairs_count.items() if count < 3]
#print(less_than_3_occurrences_pairs)
# Вывод результатов
print("Частота букв:")
for letter, frequency in letters_frequency.items():
    print(f"{letter}: {frequency}")

print("\nЧастота пар:")
for pair, frequency in pairs_frequency.items():
    print(f"{pair}: {frequency}")

print("\nПары, которые ни разу не встретились в тексте:")
print(zero_occurrence_pairs)

print("\nПары, которые встретились менее 3 раз:")
print(less_than_3_occurrences_pairs)