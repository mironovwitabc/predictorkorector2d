import math

class vector:
    def __init__(self, n):
        self.data = [0 for i in xrange(n)]
        self.dim = n

    def copy(self,vctr):
        for i in range(self.dim):
            self.data[i] = vctr.data[i]

    def __add__(self, vctr):
        new_res = vector(vctr.dim)
        new_res.copy(vctr)
        if self.dim != vctr.dim:
            print "not matching dimensions"
            return 0
        for i in range(self.dim):
            new_res.data[i] = self.data + vctr.data[i]
        return new_res

    def __sub__(self, vctr):
        new_res = vector(vctr.dim)
        new_res.copy(vctr)
        if self.dim != vctr.dim:
            print "not matching dimensions"
            return 0
        for i in range(self.dim):
            new_res.data[i] = self.data[i] - vctr.data[i]
        return new_res

    def __mul__(self, a):
        new_res = vector(self.dim)
        new_res.copy(self)
        for i in range(self.dim):
            new_res.data[i] = new_res.data[i]*a
        return new_res

    def __div__(self, a):
        new_res = vector(self.dim)
        new_res.copy(self)
        for i in range(self.dim):
            new_res.data[i] = new_res.data[i]/float(a)
        return new_res
    def scmul(self, vctr1):
        return sum(self.data[i]*vctr1.data[i] for i in xrange(self.dim))

    def norm(self):
        return math.sqrt(self.scmul(self))

    def use_matrix(self, mtrx):
        if self.dim != mtrx.dim:
            print "not matching dimensions"
            return 0
        res_new = vector(self.dim)
        res_new.copy(self)
        for i in range(self.dim):
            res_new.data[i] = sum(mtrx.data[i][j]*self.data[j] for j in range(self.dim))
        return res_new

    def printvector(self):
        print " ".join("{:2.4f}".format(i) for i in self.data) + "\n"

    def set_vector(self,lst):
        self.data = lst
        self.dim = len(lst)


class matrix:
    def __init__(self, n, m):
        self.data = [[1 if j == i else 0 for j in xrange(m)] for i in xrange(n)]
        self.line = n
        self.col = m

    def copy(self, v):
        for i in xrange(v.line):
            for j in xrange(v.col):
                self.data[i][j] = v.data[i][j]

    def clear(self):
        for i in xrange(self.line):
            for j in xrange(self.col):
                self.data[i][j] = 0

    def __add__(self, Y):
        n = self.line
        m = self.col
        new_res = matrix(n, m)
        new_res.copy(self)
        for i in xrange(self.line):
            for j in xrange(self.col):
                new_res.data[i][j] += Y.data[i][j]
        return new_res

    def __sub__(self, Y):
        n = self.line
        m = self.col
        new_res = matrix(n, m)
        new_res.copy(self)
        for i in xrange(self.line):
            for j in xrange(self.col):
                new_res.data[i][j] -= Y.data[i][j]
        return new_res

    def __div__(self, a):
        n = self.line
        m = self.col
        new_res = matrix(n, m)
        new_res.copy(self)
        for i in xrange(self.line):
            for j in xrange(self.col):
                new_res.data[i][j] = new_res.data[i][j]/float(a)
        return new_res

    def __mul__(self, a):
        n = self.line
        m = self.col
        new_res = matrix(n, m)
        new_res.copy(self)
        for i in xrange(self.line):
            for j in xrange(self.col):
                new_res.data[i][j] *= float(a)
        return new_res

    def scmul(self, v):
        res = 0
        for i in xrange(self.line):
            for j in xrange(self.col):
               res += v.data[i][j]*self.data[i][j]
        return float(res)

    def norm(self):
        return math.sqrt(self.scmul(self))

    def printmatrix(self):
        print "\n".join([" ".join(["{:10.6f}".format(i) for i in x]) for x in self.data]) + "\n"

    def set_matrix(self, lst):
        for i in xrange(self.line):
            for j in xrange(self.col):
                self.data[i][j] = float(lst[i][j])
        self.dim = len(lst[1])

    def maxelement(self):
        res = 0
        for i in self.data:
            for j in i:
                if abs(res) < abs(j):
                    res = j
        return res