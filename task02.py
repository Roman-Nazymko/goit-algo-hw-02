from collections import deque

def is_palindrome(input_string):
    # Нормалізація рядка: переведення в нижній регістр і видалення всіх пробілів 
    normalized_string = ''.join(input_string.lower().split())
 
    # Створення двосторонньої черги 
    char_deque = deque(normalized_string)
    
    # Порівняння символів з обох кінців
    while len(char_deque) > 1:
        # Видаляємо символ з лівого кінця та правого кінця, порівнюємо їх
        if char_deque.popleft() != char_deque.pop():
            # Якщо символи не збігаються, рядок не є паліндромом
             print(f"{input_string} - не є паліндромом")
             return False
    
    # Якщо всі символи збіглися, рядок є паліндромом
    print(f"{input_string} - є паліндромом")
    return True

# Тестування функції
is_palindrome("A man a plan a canal Panama")  # Очікуваний результат: є паліндромом
is_palindrome("Hello")                        # Очікуваний результат: не є паліндромом
is_palindrome("Racecar")                      # Очікуваний результат: є паліндромом
is_palindrome("No lemon no melon")            # Очікуваний результат: є паліндромом
is_palindrome("Rotor")                        # Очікуваний результат: є паліндромом
