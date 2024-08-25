my_dict = {'denis': 7391, 'kate': 7392, 'dima': 7393}
print(my_dict)
print(my_dict ['dima'])
print(my_dict.get('alex'))
my_dict['egor'] = 7394
my_dict['oleg'] = 7395
a = my_dict.pop('dima')
print(a)

my_set = {1, 2, 1, 2, 'a', 's', 'a', 's'}
print(my_set)
my_set.add(3)
my_set.add('d')
my_set.discard(1)
print(my_set)