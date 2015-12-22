n = 4
empty_list = [i for i in range(n**2)]
flag_win = False

import random
import copy

# display the matrix
def print_arr(_array):
    print '************************'
    for i in range(n):
        print '[%4d, %4d, %4d, %4d]' %(_array[i][0], _array[i][1], _array[i][2], _array[i][3])
    print '************************'

# check where is empty
def update_empty_list(_array):
    _list = [i for i in range(n**2)]
    for row in range(n):
        for col in range(n):
            if _array[row][col] != 0:
                _list.remove(row*n+col)
    return _list

def compute_score(_array):
    _score = 0
    for i in range(n):
        for j in range(n):
            _score += _array[i][j]
    return _score

def can_move(_array):
    for i in range(4):
        for j in range(4):
            if i < 3 and _array[i][j] == _array[i + 1][j]:
                return True
            if j < 3 and _array[i][j] == _array[i][j + 1]:
                return True

# add 2 or 4 to matrix
def randomly_add_to_array(_array):
    empty_list = update_empty_list(_array)
    if len(empty_list) > 0:
        x = random.choice(empty_list)
        empty_list.remove(x)
        _array[x/n][x%n] = random.choice([2,2,2,4])
    print_arr(_array)
    if flag_win == True:
        print 'Congratulations! You win! Your score is ', compute_score(_array)
    if len(empty_list) == 0:
        if not can_move(_array):
            print 'Game Over! Your score is ', compute_score(_array)
            exit()

def move_line(_list):
    temp_num = 0
    temp_list = []
    while len(_list) > 0:
        num = _list.pop()
        # only deal the ones not 0
        if num != 0:
            # combine the same two numbers
            if temp_num == num:
                temp_num += num
                temp_list.insert(0, temp_num)
                temp_num = 0
            else:
                # saved number is not 0, then move to list
                if temp_num != 0:
                    temp_list.insert(0, temp_num)
                # save new number
                temp_num = num
    # if has saved number, then move to list
    if temp_num != 0:
        temp_list.insert(0, temp_num)
    _list += temp_list
    if _list.count(2048) > 0:
        flag_win = True
    while len(_list) < n:
        _list.insert(0, 0)

def move_up(_array):
    backup_array = copy.deepcopy(_array)
    for i in range(n):
        work_list = []
        # select the column for bottom
        for j in range(n):
            work_list.append(_array[n-1-j][i])
        move_line(work_list) 
        # put back to list in matrix
        for j in range(n):
            _array[j][i] = work_list[n-1-j]
    # if not move, then do nothing
    if backup_array != _array:
        randomly_add_to_array(_array)

def move_right(_array):
    backup_array = copy.deepcopy(_array)
    for i in range(n):
        move_line(_array[i])
    # if not move, then do nothing
    if backup_array != _array:
        randomly_add_to_array(_array)

def move_down(_array):
    backup_array = copy.deepcopy(_array)
    for i in range(n):
        work_list = []
        # select the column for top
        for j in range(n):
            work_list.append(_array[j][i])
        move_line(work_list)
        # put back to list in matrix
        for j in range(n):
            _array[j][i] = work_list[j]
    # if not move, then do nothing
    if backup_array != _array:
        randomly_add_to_array(_array)

def move_left(_array):
    backup_array = copy.deepcopy(_array)
    for i in range(n):
        _array[i].reverse()
        move_line(_array[i])
        _array[i].reverse()
    # if not move, then do nothing
    if backup_array != _array:
        randomly_add_to_array(_array)

arr = [[0 for j in range(n)] for i in range(n)]

#initialize array(2 blocks)
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