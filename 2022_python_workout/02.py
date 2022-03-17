def my_sum(*args):
    #*args for optional parameter
    if len(args) == 0:
        return
    elif len(args) > 0:
        if type(args[0]) == type(0):
            _sum = 0
        elif type(args[0]) == type(0.0):
            _sum  = 0.0
        else:
            return
        for num in args:
            _sum += num
        return _sum
        

if __name__ == '__main__':
    in_list = [1,2,3]
    answer = 6
    out = my_sum(*in_list)
    #*: unpacks the sequence into its individual components
    print('in: %s, out: %s, answer: %s\n' % (in_list, out, answer))

    in_list = [1,2,3,4,5]
    answer = 15
    out = my_sum(*in_list)
    #*: unpacks the sequence into its individual components
    print('in: %s, out: %s, answer: %s\n' % (in_list, out, answer))

    in_list = [1.1,2.2,3.3]
    answer = 6.6
    out = my_sum(*in_list)
    #*: unpacks the sequence into its individual components
    print('in: %s, out: %s, answer: %s\n' % (in_list, out, answer))
    
    answer = 'None'
    out = my_sum()
    #*: unpacks the sequence into its individual components
    print('in: %s, out: %s, answer: %s\n' % ('None', out, answer))
