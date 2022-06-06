###語法
1. def func(*args):
> *:unpacks the sequence into its individual components
>
> func(c='1')
> def func(*args, **kwargs):
> c = kwargs.get('c', None)
>
> def fun(var) -> int:
> Don't need to define var type

1. Function Annotations
>def foobar(a: int, b: "it's b", c: str = 5) -> tuple:
2. 內建函式 sum(num[], init)
>init=initial value, return = sum([])+init
3. 內建函式int(str, num)
> num 幾進位
4. 內建函式 str.format()
> '{:2}{:2.2f}{:10}'.format(a_int, a_float, a_str)
5. 內建函式，f''
> f'Hello, {var_name}'
6.filter()+__ne__
> list.remove(string) 只能拿掉一個
> filter配合__ne__可以拿掉全部
> new_list = filter((remove_str).__ne__, old_list)
7. Regex, pattern 留下alphanumeric
> import re
> pattern = re.compile('[\W_]+') 	#alphanumeric
> new_line = pattern.sub(' ', line) 	#substitute by ' '

###常犯錯誤
1. dict use [] not ()
2. Cannot do - on two str
3. Try + Except, not catch
4. with open(file_name, 'r') as fp:
