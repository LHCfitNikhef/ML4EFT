from __future__ import division
import numpy as np
import matrix2py

def invert_momenta(p):
        """ fortran/C-python do not order table in the same order"""
        new_p = []
        for i in range(len(p[0])):  new_p.append([0]*len(p))
        for i, onep in enumerate(p):
            for j, x in enumerate(onep):
                new_p[j][i] = x
        return new_p

matrix2py.initialisemodel('../../Cards/param_card.dat')

def scalarProduct(p,q):
    return p[0]*q[0]-p[1]*q[1]-p[2]*q[2]-p[3]*q[3]

p = np.array([[   0.5000000E+03,  0.0000000E+00,  0.0000000E+00,  0.5000000E+03],
     [   0.5000000E+03,  0.0000000E+00,  0.0000000E+00, -0.5000000E+03],
     [   0.5000000E+03,  0.1109243E+03,  0.4448308E+03, -0.1995529E+03],
     [   0.5000000E+03, -0.1109243E+03, -0.4448308E+03,  0.1995529E+03]])

P = invert_momenta(p)
alphas = 0.118
nhel = -1 # means sum over all helicity
me2_mg = matrix2py.get_value(P, alphas, nhel)
print me2_mg

p1 = p[0,:]
p2 = p[1,:]
p3 = p[2,:]
p4 = p[3,:]

s = scalarProduct(p1+p2, p1+p2)
t = scalarProduct(p3-p1, p3-p1)
u = scalarProduct(p4-p1, p4-p1)

gs = np.sqrt(4*np.pi*alphas)

me2 = (9/2)*gs**4*(3-(s*u)/(t**2)-(u*t)/(s**2)-(s*t)/(u**2))

print me2
print me2/me2_mg5
