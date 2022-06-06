import re, string
def wordcount(filename) -> None:
    #Print characters, words, unique words, lines
    char_cnt = 0
    word_list = []
    lines = 0
    pattern = re.compile('[\W_]+')
    with open(filename, 'r') as fp:
        for line in fp:
            lines +=1
            char_cnt += len(line)
            #The answer doesn't consider the symbols
            '''remove symbols
            #Remove non alphanumaric char
            line = line.replace('-','')
            new_line = pattern.sub(' ', line)
            #remove '' from list
            line_word_list = filter(('').__ne__, new_line.split())
            '''
            line_word_list = line.split()
            word_list.extend(line_word_list)
    print('Characters: %d' % char_cnt)
    print('Words: %d' % len(word_list))
    #print(word_list)
    print('Unique Words: %d' % len(set(word_list)))
    #print(set(word_list))
    print('Lines: %d' % lines)

if __name__ == '__main__':
    _input = '20test.txt'
    print('Case 1: input file : %s' % _input)
    _output = wordcount(_input)

    print('\nAnswer: ')
    print('Characters: 164')
    print('Words: 28')
    print('Unique Words: 20')
    print('Lines: 11')
