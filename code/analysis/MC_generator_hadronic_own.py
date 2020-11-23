#!//////////////////////////////////////////////////////////#
#!//e+e- -> Z/gamma -> mu+mu-
#!//Andreas Papaefstathiou
#!//July 2014
#!//////////////////////////////////////////////////////////#
#! /usr/bin/env python

#python stuff that may or may not be useful
from __future__ import with_statement
import math, cmath, string, os, sys, fileinput, pprint
from optparse import OptionParser
import random

#comment out the following if not using matplotlib and numpy
import matplotlib
import mpmath as mp
import numpy as np
import pylab as pl
from scipy import interpolate, signal
import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

## import LHAPDF and initialize PDFs
import lhapdf
## initializes PDF member object (for protons)
p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)

## what follows depends on matplotlib/numpy
## (taken from http://matplotlib.org/examples/api/histogram_path_demo.html)
def generate_histo(array, name):
  
    fig, ax = plt.subplots()
    n, bins = np.histogram(array, 20)

    # get the corners of the rectangles for the histogram
    left = np.array(bins[:-1])
    right = np.array(bins[1:])
    bottom = np.zeros(len(left))
    top = bottom + n

    # we need a (numrects x numsides x 2) numpy array for the path helper
    # function to build a compound path
    XY = np.array([[left,left,right,right], [bottom,top,top,bottom]]).T
    
    # get the Path object
    barpath = path.Path.make_compound_path_from_polys(XY)
    
    # make a patch out of it
    patch = patches.PathPatch(barpath, facecolor='blue', edgecolor='gray', alpha=0.8)
    ax.add_patch(patch)
    
    # update the view limits
    ax.set_xlim(left[0], right[-1])
    ax.set_ylim(bottom.min(), top.max())
    plt.savefig(name + '.pdf')
#    plt.show()

## Print some stuff
print('\n')
print('----====================================================----')
print('Exercise 2 (Advanced Scientific Computing Workshop, July 2014)')
print('pp --> Z --> mu+ mu-')
print('----====================================================----')
print('\n')



## some parameters
pb_convert = 3.894E8 # conversion factor GeV^-2 -> pb
alpha = 0.1184 # alpha QED
mt = 172 #Top quark mass in GeV
Gfermi = 0.0000116637
v = 1/np.sqrt(Gfermi*np.sqrt(2))
asQCD = 0.1184
cSMEFT = 1
LambdaSMEFT = 10**3
# PP COM energy in GeV
ECM = 13000
s = ECM**2
print("hadron com energy:", ECM, "GeV")

# we also set minimum Q
Q_min = 60



## define a function that gives the differential cross section
## as a function of the parameters
## we include anything that depends on s hat

def dsigmadThetaggSM(sqrts, theta):#Correct cross check with mathematica and MG
    sP = sqrts**2
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    g = np.sqrt(4*np.pi*asQCD)
    num = g**4*(-mt**4*(3*t**2+14*t*u+3*u**2)+mt**2*(7*t**2*u+t**3+7*t*u**2+u**3)+6*mt**8-t*u*(t**2+u**2))*(18*mt**2*(t+u)-18*mt**4+sP**2-9*(t**2+u**2))
    den = 48*sP**2*(t-mt**2)**2*(u-mt**2)**2
    Me2 = num/den
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta


def dsigmadThetaqqSM(sqrts, theta):
    sP = sqrts**2
    g = np.sqrt(4*np.pi*asQCD)
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    Me2 = 4*g**4*(-4*u*mt**2+6*mt**4-4*t*mt**2+t**2+u**2)/(9*sP**2)
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta

#EFT
def dsigmadThetaqqEFT(sqrts, theta, cSMEFT):
    sP = sqrts**2
    g = np.sqrt(4*np.pi*asQCD)
    Me2 = cSMEFT*(16*np.sqrt(2)*g**3*v*mt)/(9*LambdaSMEFT**2)
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta

def dsigmadThetaggEFT(sqrts, theta, cSMEFT):
    sP = sqrts**2
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    g = np.sqrt(4*np.pi*asQCD)
    Me2 = (cSMEFT*g**3*v*mt*(-18*mt**2*(t+u)+18*mt**4-sP**2+9*(t**2+u**2)))/(6*np.sqrt(2)*LambdaSMEFT**2*(mt**2-t)*(mt**2-u))
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta

## define a function that calculates the weight for the phase space point
## we will multiply by the range of integration later on
## this function will also take care of the parton density functions
def weight(sqrts, mu, x1, x2, theta):    
    w_ii = (dsigmadThetaggSM(sqrts, theta) +dsigmadThetaggEFT(sqrts, theta,1) )* ( p.xfxQ(21, x1, mu) *  p.xfxQ(21, x2, mu) )     
    w_ii += (dsigmadThetaqqSM(sqrts,theta) + dsigmadThetaqqEFT(sqrts,theta,1))*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) +p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
    w_ii += (dsigmadThetaqqSM(sqrts,np.pi-theta) + dsigmadThetaqqEFT(sqrts,np.pi-theta,1))*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) + p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )

    # multiply by ranges and Jacobian, divide by the x1 and x2 since xfxQ gives x * f(x)
    return w_ii

def renScale(theta, sqrts):
    return 91.188
    

## in the first step, we aim to calculate:
## - the cross section
## - and the maximum point of the phase space

# set the seed for random numbers 
# random.random() will give us random numbers using the Mersenne Twister algorithm
# see: https://docs.python.org/2/library/random.html
seed = 12342
random.seed(seed)



# we also need the "ranges" (i.e. x2 - x1)
# for costh this is 1 - (-1) = 2
deltath = np.pi

rho1 = np.log(4*mt**2)
rho2 = np.log(s)
deltarho = rho2 - rho1


# number of integration points
N = 10**6

# loop over N phase space points,
# sum the weights up (sum_w) and the weights squared (sum_w_sq) (for the variance)
sum_w = 0
sum_w_sq = 0

# also define maximum point variable
w_max = 0
costh_max = -2 # so that it is obvious when something goes wrong!
Q_max = -1 # so that it is obvious when something goes wrong!

print('integrating for cross section and maximum!')
print('...')
for ii in range(0,N):
    # print progress
    sys.stdout.write("progress: %d%%   \r" % (float(ii)*100./(N)) )
    sys.stdout.flush() 
    # random costheta and rho
    th_ii = random.random() * deltath
    
    rho = rho1 + random.random() * deltarho
    # get s hat
    hats = np.exp(rho)
    # get maximum rapidity of dilepton, Y and find the range of integration for y (=2*Y)
    Y = - 0.5 * math.log(hats/s)
    deltay = 2 * Y
    # get a random value of y
    y = ( (2 * random.random()) - 1 ) * Y
    # calculate momentum fractions x1, x2
    x1 = math.sqrt(hats/s) * math.exp(y)
    x2 = math.sqrt(hats/s) * math.exp(-y)

    Jac = np.exp(rho)/s
    # set the scale for the pdfs
    mu = renScale(th_ii, np.sqrt(hats))
    #print(mu)   
    # calc. phase space point weight
    w_ii = weight(np.sqrt(hats), mu, x1, x2, th_ii) * deltath * deltarho * deltay * Jac  / (x1 * x2)
    # add to the sums
    sum_w = sum_w + w_ii
    sum_w_sq = sum_w_sq + w_ii**2
    # check if higher than maximum
    if w_ii > w_max:
        w_max = w_ii
        th_max = th_ii
        #Q_max = math.sqrt(hats)
print("sum of weights:",sum_w)
 # calculate cross section
sigma = sum_w / N

# and its error through the variance
variance = sum_w_sq/N - (sum_w/N)**2
error = math.sqrt(variance/N)

print('done integrating!')
print('\n')
print('maximum value of dsigma = ', w_max, 'found at costh = ', th_max)
print('total cross section =', sigma * pb_convert, '+-', error * pb_convert, 'pb')

## now that we have the maximum, we can generate "events"

# # we will store "generated" costh in an array:
# PScosth = []
# PSQ = []
# PSx = []
# PSy = []

# # Number of events to generate
# Neve = 10
# # counter of events generate 
# jj = 0
# # start generating events (i.e. "hit or miss")
# print 'generating events...'
# while jj < Neve:
#     sys.stdout.write("progress: %d%%   \r" % (float(jj)*100./(Neve)) )
#     sys.stdout.flush()
#     # random costheta and rho
#     costh_ii = -1 + random.random() * deltath
#     rho = rho1 + random.random() * deltarho
#     # jacobian 
#     Jac = (MTR * GTR) / ( math.cos(rho)**2 * s)
#     # get s hat
#     hats = MTR * GTR * math.tan(rho) + MTR**2
#     # get maximum rapidity of dilepton, Y and find the range of integration for y (=2*Y)
#     Y = - 0.5 * math.log(hats/s)
#     deltay = 2 * Y
#     # get a random value of y
#     y = ( (2 * random.random()) - 1 ) * Y
#     # calculate momentum fractions x1, x2
#     x1 = math.sqrt(hats/s) * math.exp(y)
#     x2 = math.sqrt(hats/s) * math.exp(-y)
#     # get the scale Q
#     Q = math.sqrt(hats)
#     # set the scale for the pdfs
#     mu = MZ
#     # calc. phase space point weight
#     w_ii = weight(hats, mu, x1, x2, costh_ii) * deltath * deltarho * deltay * Jac / (x1 * x2)
#     # now divide by maximum and compare to probability
#     prob = w_ii / w_max
#     rand_num = random.random()
#     # if the random number is less than the probability of the PS point
#     # accept
#     if rand_num < prob:
#         jj = jj+1
#         # here one can either analyze the event
#         # or store them for later convenience
#         PScosth.append(costh_ii)
#         PSQ.append(Q)
#         PSy.append(y)
#         PSx.append(x1)
#         # here we create the four-vectors of the hard process particles
#         # and boost them to the laboratory frame
#         beta = (x2 - x1) / (x2 + x1)
#         # generate random phi
#         phi = random.random() * 2 * math.pi
#         sinphi = math.sin(phi)
#         cosphi = math.cos(phi)
#         sinth = math.sqrt( 1 - costh_ii**2 )
#         pq1 = [ 0.5 * x1 * ECM, 0., 0., 0.5 * x1 * ECM ]
#         pq2 = [ 0.5 * x2 * ECM, 0., 0., - 0.5 * x2 * ECM ]
#         pem = [ 0.5 * Q, 0.5 * Q * sinth * cosphi, 0.5 * Q * sinth * sinphi, 0.5 * Q * costh_ii ]
#         pep = [ 0.5 * Q, - 0.5 * Q * sinth * cosphi, - 0.5 * Q * sinth * sinphi, - 0.5 * Q * costh_ii ]
#         # boost them to the lab frame
#         pem_boosted = boostz(pem,beta)
#         pep_boosted = boostz(pep,beta)
#         print_events = True
#         if print_events is True:
#             print 'q1', pq1
#             print 'q2', pq2
#             print 'mu-', pem_boosted
#             print 'mu+', pep_boosted
#             print '\n'

# generate_histo(PSQ, 'pp-Q')
# generate_histo(PSy, 'pp-y')
# generate_histo(PScosth, 'pp-costh')
# generate_histo(PSx, 'pp-x')