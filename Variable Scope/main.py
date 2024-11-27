from math import pi # pi built-in variable

x = 2   # Global Variable

def func1():
    a = 1       # Enclosed Variable
    print(a)
    
    def func2():
        b = 1       # Local Variable
        print(a + b * pi)
    
    func2()
    
func1()