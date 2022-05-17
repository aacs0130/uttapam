def sorted_grades(grade_tuple:list) -> str:
    if len(grade_tuple) == 0:
        return ''
    elif len(grade_tuple[0]) != 3:
        raise Exception 

    sort_grade = sorted(grade_tuple, key = lambda x: x[2], reverse = True)
    out_str = ''
    for item in sort_grade:
        #last name first
        out_str += '{:12}\t{:12}\t{:.1f}\n'.format(item[1], item[0], item[2])
    return out_str

if __name__ == '__main__':

    _grades = [
        ('Alice', 'Wooding', 89),
        ('Bob', 'Johnson', 86),
        ('Cindy', 'Letterman', 93),
        ('David', 'Moor', 86),
        ('Eddie', 'Williams', 91)
        ]
    '''
    try :
    '''
    _output = sorted_grades(_grades)
    '''except Exception:
        _output = 'Wrong input element'
    '''
    print('in:\n%s\nout:\n%s\n' % (_grades, _output))
