empty_tuple = ()

brothers = ('Juan', 'Brandon')
sisters = ('Yeiny', 'Ahisha')

siblings = brothers + sisters

number_of_siblings = len(siblings)

father = 'Juan'
mother = 'Katy'
family_members = siblings + (father, mother)

siblings, father, mother = family_members[:-2], family_members[-2], family_members[-1]

fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'egg')

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

middle_item = food_stuff_lt[len(food_stuff_lt) // 2]  

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

is_estonia_nordic = 'Estonia' in nordic_countries
is_iceland_nordic = 'Iceland' in nordic_countries

print("Número de hermanos:", number_of_siblings)
print("¿Estonia es un país nórdico?", is_estonia_nordic)
print("¿Islandia es un país nórdico?", is_iceland_nordic)