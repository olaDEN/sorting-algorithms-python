
def selection_sort(friends, sort_by):
        for x in range(len(friends)):
            min_index = x
            for y in range(x, len(friends)):
                if friends[y][sort_by].lower() < friends[min_index][sort_by].lower():
                    min_index = y
            if x != min_index:
                friends[x], friends[min_index] = friends[min_index], friends[x]
        
        return friends

                        


     

friends = [
    {'name': 'Rachel' , 'year': '1969'} ,
    {'name': 'Ross' , 'year': '1966'} ,
    {'name': 'joey' , 'year': '1967'} ,
    {'name': 'Monica' , 'year': '1964'} ]

print(f'Before sorting:', *friends, sep='\n')

sort_year = 'year'
sort_name = 'name'


year_sorted_friends = selection_sort(friends,sort_year )
print(f'\nAfter selection Sorting (descending) by \'year\':\n', *year_sorted_friends, sep='\n')

name_sorted_friends = selection_sort(friends,sort_name )
print(f'\nAfter selection Sorting (ascending) by \'name\':\n', *name_sorted_friends, sep='\n')

