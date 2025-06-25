import cProfile
def foo(num):
    num = num-1
    if num>=2:
        return foo(num)
    return num


cProfile.run("foo(10)")
