def strsort(string:str) -> str:
    #quick sort
    left = ''
    right = ''
    now = string[0]
    if len(string) < 2:
        return string
    for c in string[1:]:
        if c <= now:
            left += c
        else:
            right += c
    if len(left) > 1:
        left = strsort(left)
    if len(right) > 1:
        right = strsort(right)
    return left+now+right

if __name__ == '__main__':
    _input = 'Python'
    _output = strsort(_input)
    answer = 'Phnoty'
    print('in: %s\nout:\t%s\nanswer:\t%s\n' % (_input, _output, answer))
    
    _input = 'order'
    _output = strsort(_input)
    answer = 'deorr'
    print('in: %s\nout:\t%s\nanswer:\t%s\n' % (_input, _output, answer))
