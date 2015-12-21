n = 4
i = 0
j = 0
empty_list = [i for i in range(n**2)]

import random

def print_arr(_array):
    for i in range(n):
        print _array[i]
    print '************'

def update_empty_list(_array, _list):
    empty_list = [i for i in range(n**2)]
    for i in range(n):
        for j in range(n):
            if _array[i][j] == 0:
                empty_list.remove(i*n+j)

def randomly_add_to_array(_array):
    if len(empty_list) > 0:
        x = random.choice(empty_list)
        empty_list.remove(x)
        if _array[x/n][x%n] == 0:
            _array[x/n][x%n] = 2
    else:
        print 'Game Over!'
    print_arr(arr)

def move_right(_array):
    flag_update = False
    for i in range(n):
        import copy
        temp_list = []
        temp_num = 0
        backup_list = copy.deepcopy(_array[i])
        while len(_array[i]) > 0:
            num = _array[i].pop() 
            if num != 0:
                if temp_num == num:
                    temp_num += num
                    temp_list.insert(0,temp_num)
                    temp_num = 0
                else:
                    if temp_num != 0:
                        temp_list.insert(0,temp_num)
                    temp_num = num
        if temp_num != 0:
            temp_list.insert(0, temp_num)
        _array[i] += temp_list
        while len(_array[i]) < n:
            _array[i].insert(0,0)
        if flag_update == False and backup_list != _array[i]:
            flag_update = True
    # if not move, then add new block
    if flag_update:
        update_empty_list(_array, empty_list)
        randomly_add_to_array(_array)

arr = [[0 for j in range(n)] for i in range(n)]

# initialize array(2 blocks)
for i in range(2):
    randomly_add_to_array(arr)

print 'Game Start!'

for i in range(5):
    move_right(arr)
