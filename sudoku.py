import math

zero = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
     ]

pass_5312 = [
        [5, 4, 9, 0, 0, 0, 1, 0, 0],
        [7, 0, 0, 9, 3, 0, 5, 0, 0],
        [0, 0, 2, 8, 0, 0, 0, 0, 0],
        [3, 1, 0, 0, 0, 2, 0, 8, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 9],
        [0, 0, 0, 0, 0, 0, 4, 0, 6],
        [8, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 2, 0, 0, 0, 1, 0, 0, 0]
     ]

pass_103381 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 1, 0, 4, 0, 0, 0],
        [6, 2, 0, 0, 3, 0, 0, 0, 5],
        [0, 9, 8, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 2, 1, 0, 0],
        [5, 0, 0, 0, 0, 9, 4, 8, 7],
        [0, 0, 0, 8, 0, 0, 2, 0, 0],
        [0, 0, 0, 3, 1, 0, 0, 0, 0]
     ]

# takes 30 seconds
pass_92139 = [
        [0, 0, 0, 0, 0, 8, 0, 0, 5],
        [3, 6, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 7],
        [9, 0, 7, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 1, 0, 0, 5, 0, 2, 0, 0],
        [8, 9, 0, 6, 0, 0, 1, 2, 0],
        [5, 0, 0, 2, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 3, 0, 0, 0, 9]
     ]

# 0.654 seconds
pass_154333 = [
        [0, 0, 0, 0, 0, 2, 9, 0, 0],
        [6, 0, 0, 4, 0, 0, 0, 3, 1],
        [7, 0, 9, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 6, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 4, 0, 3, 8, 0, 0, 6, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 7, 2, 0, 0],
        [0, 2, 0, 0, 0, 0, 5, 1, 9]
     ]

# 22 seconds
pass_108205 = [
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 1, 7, 0, 0, 0, 0, 0],
        [9, 8, 4, 0, 0, 6, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 5, 7, 9, 8],
        [3, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 3, 0, 0, 5],
        [0, 0, 2, 0, 0, 0, 0, 3, 4]
     ]

# 2 seconds
pass_138382 = [
        [0, 0, 0, 0, 3, 0, 2, 6, 7],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 8, 0, 5, 0, 0, 0],
        [3, 0, 6, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 7, 0, 5, 0],
        [7, 0, 0, 0, 0, 4, 5, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 4, 0],
        [6, 0, 0, 2, 0, 0, 0, 0, 0]
     ]

I = [
        [0, 0, 0, 0, 3, 0, 2, 6, 7],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 8, 0, 5, 0, 0, 0],
        [3, 0, 6, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 7, 0, 5, 0],
        [7, 0, 0, 0, 0, 4, 5, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 4, 0],
        [6, 0, 0, 2, 0, 0, 0, 0, 0]
     ]

n = 9

def pretty_print(result):
    # for i in result:
    #    print(i)
    print('-----------------')
    print('\n'.join(' '.join(str(x) for x in row) for row in result))
    print('-----------------\n')

def get_ele(result, index):
    """
    return the indexed element of the sudoku
    :param result: the sudoku
    :param index: the index, range [0, n*n-1]
    :return: the indexed element of the sudoku
    """
    if index < 0 or index >= n*n:
        raise ValueError("index is out of range")
    i = index // n
    j = index % n
    return result[i][j]

def set_ele(result, index, value):
    """
    set the indexed element of the sudoku
    :param result: the sudoku
    :param index: the index, range [0, n*n-1]
    :param value: the value of the indexed element
    :return:
    """
    if index < 0 or index >= n*n:
        raise ValueError("index is out of range")
    i = index // n
    j = index % n
    result[i][j] = value

def copy_sudoku(sudoku):
    """
    copy a sudoku and return
    :return: the copy of the given sudoku
    :todo: make a class sudoku and move this method to the class
    """
    c = []
    for i in range(n):
        c.append(sudoku[i].copy())
    return c


def is_fixed(index):
    """
    return true if the indexed element is fixed by initial value
    :param index:
    :return:
    """
    return get_ele(I, index) > 0


def get_block_elements(result, index):
    # the sub-block size
    bn = int(math.sqrt(n))

    i = index // n
    j = index % n

    # see result as a sqrt(n) by sqrt(n) blocks

    # the row index of the block
    b_i = i // bn

    # the column index of the block
    b_j = j // bn

    i0 = b_i*bn
    j0 = b_j*bn

    block = []
    for i in range(bn):
        for j in range(bn):
            block.append(result[i0+i][j0+j])
    return block

def is_valid(result, index):
    """
    check if the element of result at index is valid
    by comparing the column, the row and the small cube
    :param result:
    :param index:
    :return:
    """
    i = index // n
    j = index % n

    # get the elements of the column j
    col = []
    for k in range(n):
        col.append(result[k][j])

    block = get_block_elements(result, index)

    v = result[i][j]
    if result[i].count(v) > 1:
        return False
    elif col.count(v) > 1:
        return False
    elif block.count(v) > 1:
        return False

    return True

def reset_init_elements(sudoku, init_sudoku, start, end):
    """
    reset the element of range [start, end] in the sudoku to initial value
    note that both start and end elements will be reset
    :param start: the index of start
    :param end: the index of end
    :return:
    """
    for i in range(start, end+1):
        value = get_ele(init_sudoku, i)
        set_ele(sudoku, i, value)

def back_trace(result, index):
    """
    set the index back to the position of result which can
    increase its value by 1
    :param result: the sudoku
    :param index:  the index of the list range from 0 to 80
                    which should go back to the last value
                    index which can increase its value by 1
    :return: the new index which can increase its value by 1
    """
    if get_ele(result, index) != n:
        raise ValueError("element of indexed is not n before back_trace")

    init_index = index
    while index > 0:
        index = index -1
        if not is_fixed(index):
            value = get_ele(result, index)
            if value < n:
                reset_init_elements(result, I, index+1, init_index)
                return index
    raise RuntimeError("can not back_trace to a valid index")


def main():
    A = copy_sudoku(I)
    #pretty_print(A)
    index = 0
    value = 1
    iter = 0
    while 0 <= index and index < n*n:
        if not is_fixed(index):

            # not initialized pos
            set_ele(A, index, value)
            if is_valid(A, index):
                index = index+1
                value = 1
            elif value < 9:
                value = value + 1
            else:
                index = back_trace(A, index)
                value = get_ele(A, index) + 1
                set_ele(A, index, value)
        else:
            index = index + 1

        iter = iter+1
        if iter % 10 == 0:
            pretty_print(A)

    if index == n*n:
        print("succeeded")
        pretty_print(A)
    else:
        print("Error, can not find the solution")



if __name__ == "__main__":
    main()