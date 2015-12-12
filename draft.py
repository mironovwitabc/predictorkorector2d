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


def operator_Bx(u):
    new_matrix = matrix(amnty, amntx + 1)
    new_matrix.clear()
    for i in xrange(new_matrix.line):
        new_matrix.data[i][0] = u.data[i][0] * (-hy)
        new_matrix.data[i][new_matrix.col - 1] = u.data[i][u.col - 1]*(hy)
        for j in xrange(1, new_matrix.col - 1):
            new_matrix.data[i][j] = u.data[i][j]*(-hy) + u.data[i][j-1]*hy
    return new_matrix


def operator_Ax(u):
    new_matrix = matrix(amnty, amntx + 1)
    new_matrix.clear()
    new_solution = matrix(amnty, amntx + 1)
    new_solution.clear()
    alpha = vector(amntx + 1)
    beta = vector(amntx + 1)
    for i in xrange(new_matrix.line):
        alpha.data[0] = hy*hx/3
        beta.data[0] = hy*hx/6/alpha.data[0]
        new_matrix.data[i][0] = u.data[i][0]/alpha.data[0]
        for j in xrange(1, new_matrix.col - 1):
            alpha.data[j] = 2*hy*hx/3 - hy*hx/6*beta.data[j - 1]
            beta.data[j] = hy*hx/6/alpha.data[j]
            new_matrix.data[i][j] = (u.data[i][j] - hy*hx/6*new_matrix.data[i][j -1])/alpha.data[j]
        alpha.data[new_matrix.col - 1] = hy*hx/3 - hy*hx/6*beta.data[new_matrix.col - 2]
        new_matrix.data[i][new_matrix.col - 1] = (u.data[i][new_matrix.col - 1] - (hy*hx/6)*new_matrix.data[i][new_matrix.col - 2])/alpha.data[new_matrix.col - 1]
        new_solution.data[i][new_matrix.col - 1] = new_matrix.data[i][new_matrix.col - 1]
        for j in range(new_matrix.col - 2, -1, -1):
            new_solution.data[i][j] = new_matrix.data[i][j] - beta.data[j]*new_solution.data[i][j + 1]
    new_solution.printmatrix()
    return new_solution

solution_number =1 #input()
amntx =4 #input()
amnty = 4#input()
amntt =4 #input()
hx = 1/float(amntx)
hy = 1/float(amnty)
teta =0.3 #input()
tao = 1/float(amntt)
print hx, hy
w_x = matrix(amnty, amntx + 1)
w_y = matrix(amnty + 1, amntx)
u = matrix(amnty, amntx)

def_real_u(u, solution_number)
print "U"
u.printmatrix()
print "BxU"
operator_Bx(u).printmatrix()
w_x.copy(operator_Bx(u))

w_x.copy(operator_Ax(w_x))
w_x.printmatrix()