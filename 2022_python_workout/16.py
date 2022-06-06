def unique_num_len(input_iter) -> int:
    cnt_list = []
    for item in input_iter:
        if item not in cnt_list:
            cnt_list.append(item)
    return len(cnt_list)

if __name__ == '__main__':

    _input = [1,2,3,1,2,3,4,1,2]
    _output = unique_num_len(_input)
    answer = 4
    print('Case 1:in: %s\nout:\t%s\nanswer:\t%s\n' % (_input, _output, answer))
    
    _input = (1,2,0,0)
    _output = unique_num_len(_input)
    answer = 3
    print('Case 2: in: %s\nout:\t%s\nanswer:\t%s\n' % (_input, _output, answer))
    
    _input = ()
    _output = unique_num_len(_input)
    answer = 0
    print('Case 3: in: %s\nout:\t%s\nanswer:\t%s\n' % (_input, _output, answer))
    
    _input = [1,2,3,4,5,4,3,2,1,1,1]
    _output = unique_num_len(_input)
    answer = 5
    print('Case 4: in: %s\nout:\t%s\nanswer:\t%s\n' % (_input, _output, answer))
