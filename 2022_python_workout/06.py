def pl_word(word) -> str:
    vowel = 'aeiou'
    pl = ''
    if word[0] in vowel:
        pl = word+'way'
    else:
        if len(word) > 1:
            pl = word[1:]+word[0]+'ay'
        else:
            pl = word+'ay'
    return pl

def pl_sentence(sen) -> str:
    pig_sen = ''
    for word in sen.split(' '):
        pig_sen += pl_word(word)+' '        
    return pig_sen[:-1]

if __name__ == '__main__':
    sen = 'this is a test'
    pl_sen = pl_sentence(sen)
    answer = 'histay isway away esttay'
    print('in: %s\nout:\t%s\nanswer:\t%s\n' % (sen, pl_sen, answer))

    sen = 'y w you ok'
    pl_sen = pl_sentence(sen)
    answer = 'yay way ouyay okway'
    print('in: %s\nout:\t%s\nanswer:\t%s\n' % (sen, pl_sen, answer))

