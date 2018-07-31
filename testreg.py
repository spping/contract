def register(func):
    print('running register(%s)' % func)
    return func

def func1():
    print('running func1')

@register
def func2():
    print('running func2')