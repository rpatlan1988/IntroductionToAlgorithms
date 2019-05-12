import sys
import time
import numpy as np
def find_max_crossing_subarray(A, low, mid, high):
    left_sum = - sys.maxsize
    t_sum = 0
    left_max = None
    for i in range(mid, low -1, -1):
        t_sum = t_sum + A[i]
        if t_sum >= left_sum:
            left_sum = t_sum
            left_max = i
    
    t_sum = 0
    righ_sum = - sys.maxsize
    right_max = None
    for i in range(mid + 1, high + 1):
        t_sum = t_sum + A[i]
        if t_sum >= righ_sum:
            righ_sum = t_sum
            right_max = i

    return left_max, right_max, left_sum + righ_sum


def find_max_subarray(A, low, high):

    #Base case
    if low == high:
        return low, high, A[low]
    
    mid = low + (high - low)/2
    left_low, left_high, left_sum = find_max_subarray(A, low, mid)
    right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
    cross_left, cross_right, cross_sum = find_max_crossing_subarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_left, cross_right, cross_sum


def find_max_subarray_brute_force(A):
    over_max = -sys.maxint
    win_start = 0
    win_end = 0

    for i in range(0, len(A)):
        i_max = -sys.maxint
        right_max = i
        i_sum = 0
        for j in range(i, len(A)):
            i_sum = i_sum + A[j]
            if i_sum > i_max:
                i_max = i_sum
                right_max = j
        
        if over_max < i_max:
            over_max = i_max
            win_start = i
            win_end = right_max
        
        if i % 100 == 0:
            print("iteration number %d " %i)
    return win_start, win_end, over_max

if __name__ == '__main__':
    '''
    The main function to kick off the process
    '''
    #A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    #A = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]
    np.random.seed(2)
    A = np.random.randn(1, 10000)
    A = np.squeeze(A).tolist()

    time_start = time.time()
    print(find_max_subarray(A, 0, len(A) -1 ))
    print('TIme taken by recursive ', time.time() - time_start)
    time_start = time.time()
    print(find_max_subarray_brute_force(A))
    print('TIme taken by brute ', time.time() - time_start)