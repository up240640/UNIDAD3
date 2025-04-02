import random

def random_user_id():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(characters) for _ in range(6))

print(random_user_id())  

def user_id_gen_by_user():
    num_chars = int(input("Ingrese el número de caracteres por ID: "))
    num_ids = int(input("Ingrese la cantidad de IDs a generar: "))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    ids = [''.join(random.choice(characters) for _ in range(num_chars)) for _ in range(num_ids)]
    return ids

print(user_id_gen_by_user()) 

def rgb_color_gen():
    return f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

print(rgb_color_gen())  


def list_of_hexa_colors(num_colors):
    colors = [f"#{''.join(random.choice('0123456789abcdef') for _ in range(6))}" for _ in range(num_colors)]
    return colors

def list_of_rgb_colors(num_colors):
    colors = [rgb_color_gen() for _ in range(num_colors)]
    return colors

def generate_colors(format_type, num_colors):
    if format_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif format_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "Formato inválido. Usa 'hexa' o 'rgb'."

print(generate_colors('hexa', 3))  
print(generate_colors('rgb', 3))  

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

print(shuffle_list([1, 2, 3, 4, 5]))  

def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())  