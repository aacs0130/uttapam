def my_sum(*args):
    #*args for optional parameter
    if len(args) == 0:
        return
    elif len(args) > 0:
        if type(args[0]) == type(0):
            _sum = 0
            for num in args:
                _sum += num
        elif type(args[0]) == type(0.0):
            _sum  = 0.0
            for num in args:
                _sum += num
        elif type(args[0]) == type('a'):
            _sum=''
            for item in args:
                _sum += item
        elif type(args[0]) == type([1,2]):
            _sum=[]
            for item in args:
                _sum += item

        return _sum
        

if __name__ == '__main__':
    answer = 'None'
    out = my_sum()
    print('in: %s, out: %s, answer: %s\n' % ('None', out, answer))
    
    in_list = [10,20,30,40]
    answer = 100
    out = my_sum(*in_list)
    #*: unpacks the sequence into its individual components
    print('in: %s, out: %s, answer: %s\n' % (in_list, out, answer))

    in_list = ['abc', 'd', 'e']
    answer = 'abcde'
    out = my_sum(*in_list)
    print('in: %s, out: %s, answer: %s\n' % (in_list, out, answer))

    in_list = [[10,20,30], [40,50], [60]]
    answer = [10,20,30,40,50,60]
    out = my_sum(*in_list)
    print('in: %s, out: %s, answer: %s\n' % (in_list, out, answer))

