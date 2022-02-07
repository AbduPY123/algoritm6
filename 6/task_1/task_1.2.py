from memory_profiler import memory_usage

"""
Выполнить реверс числа
"""

# Меняем рекурсию на встроенную операцию


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper


@decor
def my_reverse(enter_num):
    if enter_num == 0:
        return ''
    return f"{str(enter_num % 10)}{my_reverse(enter_num // 10)}"


@decor
def my_reverse_2(enter_num):
    return str(enter_num)[::-1]


numb = 742234523452345234523453742234523452345234523453

print(my_reverse(numb))
print(my_reverse_2(numb))

"""
0.0703125
0.0
"""
