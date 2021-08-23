def str2b(a):
    base = 1
    num = 0
    for i in range(len(a)-1, -1, -1):
        if a[i] == '1':
            num += base
        base *= 2
    return num

def b2str(a):
    out = ''
    if a == 0:
        return '0'
    while( a > 0):
        if (a % 2) == 1:
            out = '1'+out
        elif (a % 2) == 0:
            out = '0'+out
        #print('a = %d out = %s' % (a, out))
        #print('a mod 2 = %d a /2 = %d' % (a % 2, a/2))
        a = int(a/2)
    return out

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    return b2str(str2b(a)+str2b(b))

if __name__ == '__main__':
    '''
    a = '1010'
    b = '1011'
    print('a= %s, b=%s' %(a,b))
    print('a int = %d, b int = %d' %(str2b(a), str2b(b)))
    '''
    '''
    out = 21
    print('str %d binary %s' %(out, b2str(out)))
    print('correct = 10101')
    '''
    '''
    out = 11
    print('str %d binary %s' %(out, b2str(out)))
    print('correct = 1011')
    #'''
    '''
    out = 4
    print('str %d binary %s' %(out, b2str(out)))
    print('correct = 100')
    '''

    a = '1010'
    b = '1011'
    print('a= %s, b=%s' %(a,b))
    print('add =\t%s' % addBinary(a,b))
    print('correct =\t10101')

    a = '0'
    b = '0'
    print('a= %s, b=%s' %(a,b))
    print('add =\t%s' % addBinary(a,b))
    print('correct =\t0')

    a = '11'
    b = '1'
    print('a= %s, b=%s' %(a,b))
    print('add =\t%s' % addBinary(a,b))
    print('correct =\t100')
