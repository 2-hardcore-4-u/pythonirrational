error = 0

def erroroccurance():
    global error
    error = error + 1
    print("ERROR OCCURED")
    return (None, None)

def clear_error():
    error = 0
    
def GCD(x):
    try:
        a = x[0]
        b = x[1]
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b
    except:
        print('g')
        erroroccurance()

def _reduce(a):
    try:
        localGCD = GCD(a)
        x = int(a[0] / localGCD)
        y = int(a[1] / localGCD)
        b = (0, 0)
        if (x > 0 and y > 0) or (x < 0 and y > 0):
            b = (x, y)
        else:
            b = (-x, -y)
        return b
    except:
        print('r')
        erroroccurance()

def add(a, b):
    try:
        x = int(a[0] * b[1] + b[0] * a[1])
        y = int(a[1] * b[1])
        z = (x, y)
        return _reduce(z)
    except:
        print('a')
        erroroccurance()

def sub(a, b):
    try:
        x = int(a[0] * b[1] - b[0] * a[1])
        y = int(a[1] * b[1])
        z = (x, y)
        return _reduce(z)
    except:
        print('s')
        erroroccurance()

def mul(a, b):
    try:
        x = int(a[0] * b[0])
        y = int(a[1] * b[1])
        z = (x, y)
        return _reduce(z)
    except:
        print('m')
        erroroccurance()

def div(a, b):
    try:
        x = int(a[0] * b[1])
        y = int(a[1] * b[0])
        z = (x, y)
        return _reduce(z)
    except:
        print('d')
        erroroccurance()

def eq(a, b):
    try:
        x = _reduce(a)
        y = _reduce(b)
        return x == y
    except:
        print('e')
        erroroccurance()

def lt(a, b):
    try:
        x = _reduce(a)
        y = _reduce(b)
        return sub(x, y)[0] < 0
    except:
        print('l')
        erroroccurance()


def create(a, b):
    try:
        return (a, b)
    except:
        print('c')
        erroroccurance()

def inp():
    try:
        a = int(input())
        b = int(input())
        print(_reduce(create(a, b)))
        return _reduce(create(a, b))
    except:
        print('i')
        erroroccurance()

def prt(a):
    x = str(a[0]) + " / " + str(a[1])
    print(x)