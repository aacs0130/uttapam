def myxml(name:str, value:str = None, *args, **kwargs) -> str:
    out_str = ''
    param_str = ''
    if value:
        out_str = value
    for item in kwargs.keys():
        param_str += str(item)+'=\"'+str(kwargs.get(item, None))+'\" '
    if param_str:
        param_str = param_str[:-1]
    if name:
        if param_str:
            out_str = '<'+name+' '+param_str+'>'+out_str+'</'+name+'>'
        else:
            out_str = '<'+name+'>'+out_str+'</'+name+'>'
    return out_str

if __name__ == '__main__':
    _name = 'foo'
    _output = myxml(_name)
    answer = '<foo></foo>'
    print('out:\t%s\nanswer:\t%s' % (_output, answer))
    print('diff: '+str(_output == answer))

    _name = 'foo'
    _value = 'bar'
    _output = myxml(_name, _value)
    answer = '<foo>bar</foo>'
    print('out:\t%s\nanswer:\t%s' % (_output, answer))
    print('diff: '+str(_output == answer))

    _name = 'foo'
    _value = 'bar'
    _output = myxml(_name, _value, a=1, b=2, c=3)
    answer = '<foo a=\"1\" b=\"2\" c=\"3\">bar</foo>'
    print('out:\t%s\nanswer:\t%s' % (_output, answer))
    print('diff: '+str(_output == answer))
