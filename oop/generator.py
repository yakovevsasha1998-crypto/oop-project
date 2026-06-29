import sys

big_list = [x for x in range(1000000)]

def function():
    for x in range(100000):
        yield x
    
print(f'Размер списка в памяти: {sys.getsizeof(big_list)} байт')
print(f'Размер списка в генераторе: {sys.getsizeof(function)} байт')

big_generation = (x for x in range(100))
print(f'Размер списка в генераторе: {sys.getsizeof(big_generation)} байт')