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
import mpmath as mp
import numpy as np
import pylab as pl
from scipy import interpolate, signal
import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

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
print('Exercise 1 (Advanced Scientific Computing Workshop, July 2014)')
print('e+e- --> Z/gamma -> mu+mu-')
print('----====================================================----')
print('\n')

## some parameters: equivalent to those in MadGraph
pb_convert = 3.894E8 # conversion factor GeV^-2 -> pb
MZ = 91.188    # Z boson mass
GAMMAZ = 2.4414 # Z boson width
alpha = 1/132.507 # alpha QED
Gfermi = 1.16639E-5 # fermi constant
sw2 = 0.222246 # sin^2(weinberg angle)

# e+e- COM energy in GeV
ECM = 90
hats = ECM**2
print ("e+e- com energy:", ECM, "GeV")


## define a function that gives the differential cross section
## as a function of the parameters
## we include anything that depends on s, even though in this case they are fixed for future use with variable s (hadron collisions)
def dsigma(costh):
    # CL and CR
    CV = -0.5 + 2 * sw2
    CA = -0.5
    # constants and functions that appear in the differential cross section
    kappa = math.sqrt(2) * Gfermi * MZ**2 / (4 * math.pi * alpha)
    chi1 = kappa * hats * ( hats - MZ**2 ) / (  (hats-MZ**2)**2 + GAMMAZ**2*MZ**2 )
    chi2 = kappa**2 * hats**2 / (  (hats-MZ**2)**2 + GAMMAZ**2*MZ**2 )
    A0 = 1 + 2 * CV**2 * chi1 + (CA**2 + CV**2)**2 * chi2  # see notes
    A1 = 4 * CA**2 * chi1 + 8 * CA**2 * CV**2 * chi2 
    
    PREFAC = (2 * math.pi) * alpha**2 / (4*hats) # 2 * pi comes from d-phi integral
    return  PREFAC * ( A0 * ( 1 + costh**2 ) + A1 * costh )

## in the first step, we aim to calculate:
## - the cross section
## - and the maximum point of the phase space

# set the seed for random numbers 
# random.random() will give us random numbers using the Mersenne Twister algorithm
# see: https://docs.python.org/2/library/random.html
seed = 12342
random.seed(seed)

# we also need the "range" (i.e. x2 - x1)
# for costh this is 1 - (-1) = 2
delta = 2

# number of integration points
N = 1000000

# loop over N phase space points,
# sum the weights up (sum_w) and the weights squared (sum_w_sq) (for the variance)
sum_w = 0
sum_w_sq = 0

# also define maximum point variable
w_max = 0
costh_max = -2 # so that it is obvious when something goes wrong!

print('integrating for cross section and maximum!')
print('...')
for ii in range(0,N):
    # print progress
    sys.stdout.write("progress: %d%%   \r" % (float(ii)*100./(N)) )
    sys.stdout.flush() 
    # random costheta
    costh_ii = -1 + random.random() * delta
    # calc. phase space point
    w_ii = dsigma(costh_ii) * delta
    # add to the sums
    sum_w = sum_w + w_ii
    sum_w_sq = sum_w_sq + w_ii**2
    # check if higher than maximum
    if w_ii > w_max:
        w_max = w_ii
        costh_max = costh_ii

# calculate cross section
sigma = sum_w / N

# and its error through the variance
variance = sum_w_sq/N - (sum_w/N)**2
error = math.sqrt(variance/N)

print('done integrating!')
print('\n')
print('maximum value of dsigma = ', w_max, 'found at costh = ', costh_max)
print('total cross section =', sigma * pb_convert, '+-', error * pb_convert, 'pb')

# print out value of analytical expression for sigma
# CL and CR
CV = -0.5 + 2 * sw2
CA = -0.5
# constants and functions that appear in the differential cross section
kappa = math.sqrt(2) * Gfermi * MZ**2 / (4 * math.pi * alpha)
chi1 = kappa * hats * ( hats - MZ**2 ) / (  (hats-MZ**2)**2 + GAMMAZ**2*MZ**2 )
chi2 = kappa**2 * hats**2 / (  (hats-MZ**2)**2 + GAMMAZ**2*MZ**2 )
A0 = 1 + 2 * CV**2 * chi1 + (CA**2 + CV**2)**2 * chi2  # see notes
A1 = 4 * CA**2 * chi1 + 8 * CA**2 * CV**2 * chi2 
print('analytical value:')
print('total cross section =', 4 * math.pi * alpha**2 * A0 * pb_convert/ 3. / hats, 'pb')

## now that we have the maximum, we can generate "events"
## in this simple case, we only have one parameter, costh
## we can translate this parameter into momenta for the outgoing particles

# we will store "generated" costh in an array:
PScosth = []

# Number of events to generate
Neve = 10E4
# counter of events generate 
jj = 0
# start generating events (i.e. "hit and miss")
print('generating events...')
while jj < Neve:
    sys.stdout.write("progress: %d%%   \r" % (float(jj)*100./(Neve)) )
    sys.stdout.flush()
    # random costheta
    costh_ii = -1 + random.random() * delta
    # calc. phase space point
    w_ii = dsigma(costh_ii) * delta
    # now divide by maximum and compare to probability
    prob = w_ii / w_max
    rand_num = random.random()
    # if the random number is less than the probability of the PS point
    # accept
    if rand_num < prob:
        jj = jj+1
        # here one can either analyze the
        # or store them for later convenience
        PScosth.append(costh_ii)
        # here we create the four-vectors of the hard process particles
        # generate random phi
        phi = random.random() * 2 * math.pi
        sinphi = math.sin(phi)
        cosphi = math.cos(phi)
        sinth = math.sqrt( 1 - costh_ii**2 )
        pem = [ 0.5 * ECM, 0., 0., 0.5 * ECM ]
        pep = [ 0.5 * ECM, 0., 0., - 0.5 * ECM ]
        pmm = [ 0.5 * ECM, 0.5 * ECM * sinth * cosphi, 0.5 * ECM * sinth * sinphi, 0.5 * ECM * costh_ii ]
        pmp = [ 0.5 * ECM, - 0.5 * ECM * sinth * cosphi, - 0.5 * ECM * sinth * sinphi, - 0.5 * ECM * costh_ii ]
        print_events = True
        if print_events is True:
            print('e-', pem)
            print('e+', pep)
            print('mu-', pmm)
            print('mu+', pmp)
            print('\n')

        
generate_histo(PScosth, 'ee-costh')