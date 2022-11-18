def bubbleSort(friends,sort_by):
    size = len(friends)
     
    for i in range(size):
        swapped = False

        for j in range(0, size-i-1):
            if friends[j][sort_by].lower() > friends[j+1][sort_by].lower() :
                friends[j], friends[j+1] = friends[j+1], friends[j]
                swapped = True

        if swapped == False:
            break
    return friends
    
friends = [
    {'name': 'Rachel' , 'year': '1969'} ,
    {'name': 'Ross' , 'year': '1966'} ,
    {'name': 'joey' , 'year': '1967'} ,
    {'name': 'Monica' , 'year': '1964'} ]

print(f'Before sorting:', *friends, sep='\n')

sort_year = 'year'
sort_name = 'name'


year_sorted_friends = bubbleSort(friends,sort_year )
print(f'\nAfter Bubble Sorting (descending) by \'year\':\n', *year_sorted_friends, sep='\n')

name_sorted_friends = bubbleSort(friends,sort_name )
print(f'\nAfter Bubble Sorting (ascending) by \'name\':\n', *name_sorted_friends, sep='\n')

    
