'''

装饰器


'''

def print_func_name(func):
    def wrapper(*args,**kwargs):
        print(func.__name__)

        return func(*args,**kwargs)
    return wrapper
@ print_func_name
def say_hello(name):
    print(name,'hello')
    return 'haha'

@ print_func_name
def say_goodbye(name,age):
    print(age,name,'goodbye')



print(say_hello('tom'))