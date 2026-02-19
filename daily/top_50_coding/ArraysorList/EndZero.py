def move_zero_to_end_of_array(array):
    j = 0
    for i in range(0,len(array)):
        if array[i]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            j = j+1
    return array
if __name__ == '__main__':
    list=[5,0,6,3,0,4,0,-1,2,9,0,8,0]
    print(move_zero_to_end_of_array(list))
    # print(list)