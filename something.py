def func(x):
    func2 = lambda x: x+5
    return func2(x) +85

func3 = lambda x,y=4:x+y
print(func3(5,6))

print(func(2))