it_companies = {'Google', 'Facebook', 'Microsoft', 'Apple', 'IBM'}

length_of_it_companies = len(it_companies)

it_companies.add('Twitter')

it_companies.update({'Amazon', 'Netflix', 'Adobe'})

it_companies.remove('Facebook')

A = {1, 2, 3}
B = {3, 4, 5}

joined_set = A.union(B)

intersection_set = A.intersection(B)

is_subset = A.issubset(B)

are_disjoint = A.isdisjoint(B)

joined_ab = A.union(B)
joined_ba = B.union(A)

symmetric_difference = A.symmetric_difference(B)

del A
del B

ages = [10, 23, 33, 34, 40, 40, 60]
ages_set = set(ages)
length_of_list = len(ages)
length_of_set = len(ages_set)

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
number_of_unique_words = len(unique_words)

print("Longitud de it_companies:", length_of_it_companies)
print("Número de palabras únicas:", number_of_unique_words)