# 2048
# 2048
n = 4
empty_list = [i for i in range(n**2)]

import random
import copy

def print_arr(_array):
    for i in range(n):
        print '[%4d, %4d, %4d, %4d]' %(_array[i][0], _array[i][1], _array[i][2], _array[i][3])
    print '************'

def update_empty_list(_array):
    _list = [i for i in range(n**2)]
    for row in range(n):
        for col in range(n):
            if _array[row][col] != 0:
                _list.remove(row*n+col)
    return _list

def randomly_add_to_array(_array):
    empty_list = update_empty_list(_array)
    if len(empty_list) > 0:
        x = random.choice(empty_list)
        empty_list.remove(x)
        if _array[x/n][x%n] == 0:
            _array[x/n][x%n] = random.choice([2,2,2,4])
    else:
        print 'Game Over!'
        score = 0
        for i in range(n)
            for j in range(n)
                score += _array[i][j]
        print 'Your score: ', score
        exit()
    print_arr(arr)

def move_line(_list):
    temp_num = 0
    temp_list = []
    while len(_list) > 0:
        num = _list.pop()
        if num != 0:
            if temp_num == num:
                temp_num += num
                temp_list.insert(0, temp_num)
                temp_num = 0
            else:
                if temp_num != 0:
                    temp_list.insert(0, temp_num)
                temp_num = num
    if temp_num != 0:
        temp_list.insert(0, temp_num)
    _list += temp_list
    while len(_list) < n:
        _list.insert(0, 0)

def move_up(_array):
    flag_update = False
    for i in range(n):
        work_list = []
        for j in range(n):
            work_list.append(_array[n-1-j][i])
        backup_list = copy.deepcopy(work_list)
        move_line(work_list)
        if flag_update == False and backup_list != work_list:
            flag_update = True
        # put back
        for j in range(n):
            _array[j][i] = work_list[n-1-j]
    # if not move, then do nothing
    if flag_update:
        randomly_add_to_array(_array)

def move_right(_array):
    flag_update = False
    for i in range(n):
        backup_list = copy.deepcopy(_array[i])
        move_line(_array[i])
        if flag_update == False and backup_list != _array[i]:
            flag_update = True
    # if not move, then do nothing
    if flag_update:
        randomly_add_to_array(_array)
        
def move_down(_array):
    flag_update = False
    for i in range(n):
        work_list = []
        for j in range(n):
            work_list.append(_array[j][i])
        backup_list = copy.deepcopy(work_list)
        move_line(work_list)
        if flag_update == False and backup_list != work_list:
            flag_update = True
        # put back
        for j in range(n):
            _array[j][i] = work_list[j]
    # if not move, then do nothing
    if flag_update:
        randomly_add_to_array(_array)
    
def move_left(_array):
    flag_update = False
    for i in range(n):
        backup_list = copy.deepcopy(_array[i])
        _array[i].reverse()
        move_line(_array[i])
        _array[i].reverse()
        if flag_update == False and backup_list != _array[i]:
            flag_update = True
    # if not move, then do nothing
    if flag_update:
        randomly_add_to_array(_array)

arr = [[0 for j in range(n)] for i in range(n)]

# initialize array(2 blocks)
for i in range(2):
    randomly_add_to_array(arr)

print 'Game Start! Up(w) Down(s) Left(a) Right(d) Exit(Enter)'
input_direction = raw_input('move: ')
while len(input_direction) > 0:
    if input_direction[0] in ('W', 'w'):
        move_up(arr)
    elif input_direction[0] in ('D', 'd'):
        move_right(arr)
    elif input_direction[0] in ('S', 's'):
        move_down(arr)
    elif input_direction[0] in ('A', 'a'):
        move_left(arr)
    else:
        print 'Invalid input!'
    input_direction = raw_input('move Up(w) Down(s) Left(a) Right(d) Exit(Enter): ')

exit()
