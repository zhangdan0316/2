def func():
    print("...1....")
    return "hello,world"


test1 = func
test2 = func()

print(type(test1))
print(type(test2))