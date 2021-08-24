def afterEqual(str):
    x = str.split('=')
    return x[1]

def beforeEqual(str):
    x = str.split('=')
    return x[0]

def numComp(str):
    x = int(str)
    if type(x) == 'int':
        return True
    else:
        return False

def equation(str):
    s = 0
    b = 0
    indSum = 0
    indSubs = 0
    indTimes = 0
    indDiv = 0
    bE = beforeEqual(str)
    aE = afterEqual(str)

    for element in bE:
        if element == '+':
            indSum = bE.find('+') + 1            
            s = int(aE) - int(bE[indSum])
        elif element == '-':
            indSubs = bE.find('-') + 1
            s = int(aE) + int(bE[indSubs])

    for element in bE:
        if element == '/':
            indDiv = bE.find('/')
            if bE[indDiv + 1] == 'x':
                b = int(bE[indDiv - 1]) / s
            elif bE[indDiv - 1] == 'x':
                b = int(bE[indDiv + 1]) * s
        else:
            indTimes = bE.find('x') - 1
            b = s / int(bE[indTimes])
    print('x is:')
    return b

eq = input('Insert your equation: ')
print(equation(eq))

# Comprobar si el siguiente es un numero, y si devuelve true crear un string con ambos numeros