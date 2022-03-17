02 Optional parameter of function:
def func(*args):
*:unpacks the sequence into its individual components

func(c='1')
def func(*args, **kwargs):
c = kwargs.get('c', None)

