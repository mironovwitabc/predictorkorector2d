import math
from matrixandvectors import matrix
from matrixandvectors import vector


def solution(x, y, k):
    if k == 0:
        return math.sin(math.pi*x)*math.sin(math.pi*y)
    else:
        if k == 1:
            return (1 - x)*x*(1 - y)*y


def def_real_u(u, k):
    u.clear()
    for i in xrange(u.line):
        for j in xrange(u.col):
            u.data[i][j] = solution(hx*j+hx/2, hy*i+hy/2, k)


def corrector_x(u, b1, b2, a1, a2):
    Bu = matrix(u.line, u.col + 1)
    Bu.clear()
    for i in xrange(Bu.line):
        Bu.data[i][0] = u.data[i][0] * b1
        Bu.data[i][Bu.col - 1] = u.data[i][u.col - 1]*b2
        for j in xrange(1, Bu.col - 1):
            Bu.data[i][j] = u.data[i][j]*b1 + u.data[i][j-1]*b2
    #progonka A
    y = matrix(Bu.line, Bu.col)
    y.clear()
    gradu = matrix(Bu.line, Bu.col)
    gradu.clear()
    alpha = vector(Bu.col)
    beta = vector(Bu.col)
    for i in xrange(y.line):
        alpha.data[0] = a1
        beta.data[0] = a2/alpha.data[0]
        y.data[i][0] = Bu.data[i][0]/alpha.data[0]
        for j in xrange(1, y.col - 1):
            alpha.data[j] = 2*a1 - a2*beta.data[j - 1]
            beta.data[j] = a2/alpha.data[j]
            y.data[i][j] = (Bu.data[i][j] - a2*y.data[i][j -1])/alpha.data[j]
        alpha.data[y.col - 1] = a1 - a2*beta.data[y.col - 2]
        y.data[i][y.col - 1] = (Bu.data[i][y.col - 1] - a2*y.data[i][y.col - 2])/alpha.data[y.col - 1]
        gradu.data[i][y.col - 1] = y.data[i][y.col - 1]
        for j in range(y.col - 2, -1, -1):
            gradu.data[i][j] = y.data[i][j] - beta.data[j]*gradu.data[i][j + 1]
    gradu.printmatrix()
    return gradu


def corrector_y(u, b1, b2, a1, a2):
    Bu = matrix(u.line + 1, u.col + 1)
    Bu.clear()
    for i in xrange(Bu.line):
        Bu.data[i][0] = u.data[i][0] * b1
        Bu.data[i][Bu.col - 1] = u.data[i][u.col - 1]*b2
        for j in xrange(1, Bu.col - 1):
            Bu.data[i][j] = u.data[i][j]*b1 + u.data[i][j-1]*b2
    #progonka A
    y = matrix(Bu.line, Bu.col)
    y.clear()
    gradu = matrix(Bu.line, Bu.col)
    gradu.clear()
    alpha = vector(Bu.col)
    beta = vector(Bu.col)
    for i in xrange(y.line):
        alpha.data[0] = a1
        beta.data[0] = a2/alpha.data[0]
        y.data[i][0] = Bu.data[i][0]/alpha.data[0]
        for j in xrange(1, y.col - 1):
            alpha.data[j] = 2*a1 - a2*beta.data[j - 1]
            beta.data[j] = a2/alpha.data[j]
            y.data[i][j] = (Bu.data[i][j] - a2*y.data[i][j -1])/alpha.data[j]
        alpha.data[y.col - 1] = a1 - a2*beta.data[y.col - 2]
        y.data[i][y.col - 1] = (Bu.data[i][y.col - 1] - a2*y.data[i][y.col - 2])/alpha.data[y.col - 1]
        gradu.data[i][y.col - 1] = y.data[i][y.col - 1]
        for j in range(y.col - 2, -1, -1):
            gradu.data[i][j] = y.data[i][j] - beta.data[j]*gradu.data[i][j + 1]
    gradu.printmatrix()
    return gradu


solution_number =1 #input()
amntx =4 #input()
amnty = 4#input()
amntt =4 #input()
hx = 1/float(amntx)
hy = 1/float(amnty)
teta =0.3 #input()
tao = 1/float(amntt)
w_x = matrix(amnty, amntx + 1)
w_y = matrix(amnty + 1, amntx)
u = matrix(amnty, amntx)

def_real_u(u, solution_number)
print "U"
u.printmatrix()
w_x.copy(corrector_x(u,-hy,hy,hx*hy/3,hx*hy/6))