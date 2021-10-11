#Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        val = ''
        for x in l:
            if x[:1] == '0':
                if len(x) == 11:
                    val += '+91 '
                    x = x[1:]
                    val += x[:5] + ' '
                    val += x[5:]
                    return val
                elif len(x) == 10:
                    val += '+91 '
                    val += x[:5] + ' '
                    val += x[5:]
                    return val
            elif x[:2] == '90' or x[:2] == '91':
                if len(x) == 12:
                    val += '+91 '
                    x = x[2:]
                    val += x[:5] + ' '
                    val += x[5:]
                    return val
                elif len(x) == 10:
                    val += '+91 '
                    val += x[:5] + ' '
                    val += x[5:]
                    return val
    return fun

