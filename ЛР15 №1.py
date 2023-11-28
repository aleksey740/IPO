import time
from functools import wraps

def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.monotonic()
        result = method(*args, **kw)
        te = time.monotonic()
        ms = (te - ts) * 1000
        all_args = ', '.join(tuple(f'{a!r}' for a in args)
                             + tuple(f'{k}={v!r}' for k, v in kw.items()))
        print(f'{method.__name__}({all_args}): {ms:2.2f} ms')
        return result
    return timed

# использование:

@timeit
def slow_func(x, y, sleep): #Функция `slow_func` принимает три аргумента x, y, sleep. Внутри функции выполняется сложение x + y
    #потом происходит задержка выполнения на количество секунд
    #указанное в аргументе sleep, с использованием функции time.sleep. В примере вызов slow_func(10, 20, sleep=2)
    #означает, что x равно 10 , y равно 20,и функция засыпает на 2 секунды после выполнения операции сложения
    time.sleep(sleep)
    return x + y

slow_func(10, 20, sleep=2)
