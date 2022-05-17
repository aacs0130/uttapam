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
1. 內建函式 sum(num[], init)
>init=initial value, return = sum([])+init
1. 內建函式int(str, num)
> num 幾進位
1. 內建函式 str.format()
> '{:2}{:2.2f}{:10}'.format(a_int, a_float, a_str)
1. 內建函式，f''
> f'Hello, {var_name}'

###常犯錯誤
1. dict use [] not ()
1. Cannot do - on two str
1. Try + Except, not catch
