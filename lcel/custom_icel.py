class Expression:
    def __init__(self, func):
        self.func = func

    def __call__(self,value):
        return self.func(value)

    def __or__(self,other):
        return Expression(lambda x: other(self(x)))

def upper(x):
    return x.upper()
def lower(x):
    return x.lower()

def reverse(x):
    return x[::-1]
upperFunction = Expression(upper)
lowerFunction = Expression(lower)
reverseFunction = Expression(reverse)

final = upperFunction|lowerFunction|reverseFunction
print(final("Hello world"))