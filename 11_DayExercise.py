import math
from collections import Counter

def add_two_numbers(a, b):
    return a + b

def area_of_circle(r):
    return math.pi * r * r

def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "Todos los argumentos deben ser números."

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def check_season(month):
    seasons = {
        'Autumn': ['September', 'October', 'November'],
        'Winter': ['December', 'January', 'February'],
        'Spring': ['March', 'April', 'May'],
        'Summer': ['June', 'July', 'August']
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return "Mes inválido."

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "La pendiente es indefinida."
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No hay soluciones reales."
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(lst):
    return lst[::-1]

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(n + 1))

def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

def evens_and_odds(n):
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = n + 1 - evens
    return f"El número de pares es {evens}. El número de impares es {odds}."

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_empty(param):
    return not bool(param)


def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    mid = len(lst) // 2
    return sorted_lst[mid] if len(lst) % 2 != 0 else (sorted_lst[mid - 1] + sorted_lst[mid]) / 2

def calculate_mode(lst):
    counts = Counter(lst)
    return max(counts, key=counts.get)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def are_items_unique(lst):
    return len(lst) == len(set(lst))

def are_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

def is_valid_variable(var):
    try:
        exec(f"{var} = None")
        return True
    except:
        return False

def most_spoken_languages(data, top_n=10):
    languages = [lang for country in data for lang in country['languages']]
    counts = Counter(languages).most_common(top_n)
    return [lang for lang, count in counts]

def most_populated_countries(data, top_n=10):
    return sorted(data, key=lambda x: x['population'], reverse=True)[:top_n]