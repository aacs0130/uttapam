def hex_to_dec(_hex) -> int:
    #Input is without 0x, and only use 0-9, and A-F 
    _dec = 0
    hex_map = { 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }
    for chat in _hex:
        _dec *=16
        if chat >= '0' and chat <= '9' :
            _dec+= int(chat)
        elif chat >= 'A' and chat <= 'F' :
            _dec+= hex_map[chat]
    return _dec

if __name__ == '__main__':
    _hex = '6'
    answer = 6
    _dec = hex_to_dec(_hex)
    print('in: %s, out: %s, answer: %s\n' % (_hex, _dec, answer))
   
    _hex = '0'
    answer = 0
    _dec = hex_to_dec(_hex)
    print('in: %s, out: %s, answer: %s\n' % (_hex, _dec, answer))

    _hex = 'F'
    answer = 15
    _dec = hex_to_dec(_hex)
    print('in: %s, out: %s, answer: %s\n' % (_hex, _dec, answer))

    _hex = '2A'
    answer = 42
    _dec = hex_to_dec(_hex)
    print('in: %s, out: %s, answer: %s\n' % (_hex, _dec, answer))
