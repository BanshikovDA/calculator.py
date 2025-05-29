# calculator.py

def add(a, b):
    """Складывает два числа и возвращает их сумму."""
    return a + b

def subtract(a, b):
    """Вычисляет разницу между двумя числами (первое минус второе)."""
    return a - b

def multiply(a, b):
       return a * b

def divide(a, b):
       if b != 0:
           return a / b
       else:
        raise ValueError("Division by zero")