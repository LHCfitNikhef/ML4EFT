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
p = lhapdf.mkPDF("cteq6l1", 0)

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
print '\n'
print '----====================================================----'
print 'Exercise 2 (Advanced Scientific Computing Workshop, July 2014)'
print 'pp --> Z --> mu+ mu-'
print '----====================================================----'
print '\n'

## define a fake parton density function:
## if you do not wish (or cannot) use lhapdf 6
## a function of q2 (the momentum transfer) and the momentum fraction x
def xfxQ_fake(id, x, q2):
    if abs(id) > 5 and id != 21:
        return 0
    else:
        return 0.15 * math.sin(20.0*x) * math.sin(20.0*q2)

## this function boosts along the z-direction
## and is used to go from the COM frame to the lab frame
def boostz(fourvector, beta):
  gamma = math.sqrt( 1  / (1 - beta**2) )
  boosted = [ gamma * fourvector[0] - gamma * beta * fourvector[3], fourvector[1], fourvector[2], - gamma * beta * fourvector[0] + gamma * fourvector[3] ]
  return boosted


## some parameters
pb_convert = 3.894E8 # conversion factor GeV^-2 -> pb
MZ = 91.188    # Z boson mass
GAMMAZ = 2.4414 # Z boson width
alpha = 1/132.507 # alpha QED
Gfermi = 1.16639E-5 # fermi constant
sw2 = 0.222246 # sin^2(weinberg angle)

# PP COM energy in GeV
ECM = 14000
s = ECM**2
print "hadron com energy:", ECM, "GeV"

# we also set minimum Q
Q_min = 60

## define a function that gives the differential cross section
## as a function of the parameters
## we include anything that depends on s hat
def dsigma(costh, hats, qtype):
    # constants and functions that appear in the differential cross section
    kappa = math.sqrt(2) * Gfermi * MZ**2 / (4 * math.pi * alpha)
    chi1 = kappa * hats * ( hats - MZ**2 ) / (  (hats-MZ**2)**2 + GAMMAZ**2*MZ**2 )
    chi2 = kappa**2 * hats**2 / (  (hats-MZ**2)**2 + GAMMAZ**2*MZ**2 )
    # CL and CR for leptons
    CVe = -0.5 + 2 * sw2
    CAe = -0.5
    # CL and CR
    # up-type quarks
    if qtype is 0:
        CVf = 0.5 - (4./3.) * sw2  
        CAf = 0.5
        Qf = 2./3. # charge of the quark
    # down-type quarks
    if qtype is 1:
        CVf = - 0.5 + (2./3.) * sw2
        CAf = -0.5
        Qf = -1./3.
    A0 = Qf**2 - 2 * Qf * CVe * CVf * chi1 + (CAe**2 + CVe**2) * (CAf**2 + CVf**2) * chi2  # see notes
    A1 = -4 * Qf * CAe * CAf * chi1 + 8 * CAe * CVe * CAf * CVf * chi2
    PREFAC = (2. * math.pi) * alpha**2 / (4.*hats) /3. # 2 * pi comes from d-phi integral, 1/3 from initial colour averaging
    return  PREFAC * ( A0 * ( 1 + costh**2 ) + A1 * costh )

## define a function that calculates the weight for the phase space point
## we will multiply by the range of integration later on
## this function will also take care of the parton density functions
def weight(hats, mu, x1, x2, costh_ii):
    qtype = 0 # up-type quarks
    w_ii = dsigma(costh_ii, hats, qtype) * ( p.xfxQ(2, x1, mu) *  p.xfxQ(-2, x2, mu) +  p.xfxQ(4, x1, mu) *  p.xfxQ(-4, x2, mu)  )     
    w_ii = w_ii + dsigma(-costh_ii, hats, qtype) *  ( p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +  p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) )  
    qtype = 1 # down-type quarks
    w_ii = w_ii + dsigma(costh_ii, hats, qtype) * ( p.xfxQ(1, x1, mu) *  p.xfxQ(-1, x2, mu) +  p.xfxQ(3, x1, mu) *  p.xfxQ(-3, x2, mu) )    
    w_ii = w_ii + dsigma(-costh_ii, hats, qtype) * ( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +  p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) )    
    # multiply by ranges and Jacobian, divide by the x1 and x2 since xfxQ gives x * f(x)
    return w_ii

## in the first step, we aim to calculate:
## - the cross section
## - and the maximum point of the phase space

# set the seed for random numbers 
# random.random() will give us random numbers using the Mersenne Twister algorithm
# see: https://docs.python.org/2/library/random.html
seed = 12342
random.seed(seed)

# choose the transform mass and width
MTR = Q_min
GTR = Q_min

# we also need the "ranges" (i.e. x2 - x1)
# for costh this is 1 - (-1) = 2
deltath = 2
# choose rho limits (see transformation)
rho1 = math.atan( Q_min**2 - MTR**2 ) / (GTR*MTR) 
rho2 = math.atan( (s - MTR**2) / (GTR*MTR) )
deltarho = rho2 - rho1

# number of integration points
N = 1000000

# loop over N phase space points,
# sum the weights up (sum_w) and the weights squared (sum_w_sq) (for the variance)
sum_w = 0
sum_w_sq = 0

# also define maximum point variable
w_max = 0
costh_max = -2 # so that it is obvious when something goes wrong!
Q_max = -1 # so that it is obvious when something goes wrong!

print 'integrating for cross section and maximum!'
print '...'
for ii in range(0,N):
    # print progress
    sys.stdout.write("progress: %d%%   \r" % (float(ii)*100./(N)) )
    sys.stdout.flush() 
    # random costheta and rho
    costh_ii = -1 + random.random() * deltath
    rho = rho1 + random.random() * deltarho
    # jacobian 
    Jac = (MTR * GTR) / ( math.cos(rho)**2 * s)
    # get s hat
    hats = MTR * GTR * math.tan(rho) + MTR**2
    # get maximum rapidity of dilepton, Y and find the range of integration for y (=2*Y)
    Y = - 0.5 * math.log(hats/s)
    deltay = 2 * Y
    # get a random value of y
    y = ( (2 * random.random()) - 1 ) * Y
    # calculate momentum fractions x1, x2
    x1 = math.sqrt(hats/s) * math.exp(y)
    x2 = math.sqrt(hats/s) * math.exp(-y)
    # get the scale Q
    Q = math.sqrt(hats)
    # set the scale for the pdfs
    mu = MZ
    # calc. phase space point weight
    w_ii = weight(hats, mu, x1, x2, costh_ii) * deltath * deltarho * deltay * Jac / (x1 * x2)
    # add to the sums
    sum_w = sum_w + w_ii
    sum_w_sq = sum_w_sq + w_ii**2
    # check if higher than maximum
    if w_ii > w_max:
        w_max = w_ii
        costh_max = costh_ii
        Q_max = math.sqrt(hats)

 # calculate cross section
sigma = sum_w / N

# and its error through the variance
variance = sum_w_sq/N - (sum_w/N)**2
error = math.sqrt(variance/N)

print 'done integrating!'
print '\n'
print 'maximum value of dsigma = ', w_max, 'found at costh = ', costh_max
print 'total cross section =', sigma * pb_convert, '+-', error * pb_convert, 'pb'

## now that we have the maximum, we can generate "events"

# we will store "generated" costh in an array:
PScosth = []
PSQ = []
PSx = []
PSy = []

# Number of events to generate
Neve = 10
# counter of events generate 
jj = 0
# start generating events (i.e. "hit or miss")
print 'generating events...'
while jj < Neve:
    sys.stdout.write("progress: %d%%   \r" % (float(jj)*100./(Neve)) )
    sys.stdout.flush()
    # random costheta and rho
    costh_ii = -1 + random.random() * deltath
    rho = rho1 + random.random() * deltarho
    # jacobian 
    Jac = (MTR * GTR) / ( math.cos(rho)**2 * s)
    # get s hat
    hats = MTR * GTR * math.tan(rho) + MTR**2
    # get maximum rapidity of dilepton, Y and find the range of integration for y (=2*Y)
    Y = - 0.5 * math.log(hats/s)
    deltay = 2 * Y
    # get a random value of y
    y = ( (2 * random.random()) - 1 ) * Y
    # calculate momentum fractions x1, x2
    x1 = math.sqrt(hats/s) * math.exp(y)
    x2 = math.sqrt(hats/s) * math.exp(-y)
    # get the scale Q
    Q = math.sqrt(hats)
    # set the scale for the pdfs
    mu = MZ
    # calc. phase space point weight
    w_ii = weight(hats, mu, x1, x2, costh_ii) * deltath * deltarho * deltay * Jac / (x1 * x2)
    # now divide by maximum and compare to probability
    prob = w_ii / w_max
    rand_num = random.random()
    # if the random number is less than the probability of the PS point
    # accept
    if rand_num < prob:
        jj = jj+1
        # here one can either analyze the event
        # or store them for later convenience
        PScosth.append(costh_ii)
        PSQ.append(Q)
        PSy.append(y)
        PSx.append(x1)
        # here we create the four-vectors of the hard process particles
        # and boost them to the laboratory frame
        beta = (x2 - x1) / (x2 + x1)
        # generate random phi
        phi = random.random() * 2 * math.pi
        sinphi = math.sin(phi)
        cosphi = math.cos(phi)
        sinth = math.sqrt( 1 - costh_ii**2 )
        pq1 = [ 0.5 * x1 * ECM, 0., 0., 0.5 * x1 * ECM ]
        pq2 = [ 0.5 * x2 * ECM, 0., 0., - 0.5 * x2 * ECM ]
        pem = [ 0.5 * Q, 0.5 * Q * sinth * cosphi, 0.5 * Q * sinth * sinphi, 0.5 * Q * costh_ii ]
        pep = [ 0.5 * Q, - 0.5 * Q * sinth * cosphi, - 0.5 * Q * sinth * sinphi, - 0.5 * Q * costh_ii ]
        # boost them to the lab frame
        pem_boosted = boostz(pem,beta)
        pep_boosted = boostz(pep,beta)
        print_events = True
        if print_events is True:
            print 'q1', pq1
            print 'q2', pq2
            print 'mu-', pem_boosted
            print 'mu+', pep_boosted
            print '\n'

generate_histo(PSQ, 'pp-Q')
generate_histo(PSy, 'pp-y')
generate_histo(PScosth, 'pp-costh')
generate_histo(PSx, 'pp-x')