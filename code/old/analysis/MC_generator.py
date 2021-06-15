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
import EFTxSec as ExS 

# initializes PDF member object (for protons)
p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)

# some parameters
pb_convert = 3.894E8 # conversion factor GeV^-2 -> pb
alpha = 0.1184 # alpha QED
mt = 172 #Top quark mass in GeV
Gfermi = 0.0000116637
v = 1/np.sqrt(Gfermi*np.sqrt(2))
asQCD = 0.1184

LambdaSMEFT = 10**3
# PP COM energy in GeV
ECM = 14000
s = ECM**2


def renScale():
    return 91.188

def MC_genEvents(Nsamples, cSMEFT, order = None, NP = None, mtt_min = 1500, mtt_max = ECM, gen_events = True):

    print("Hadron com energy:", ECM, "GeV")
    print('\n')
    print('----====================================================----')
    print('Computing top-pair production in the EFT with ctG = %.2f' %(cSMEFT))
    print('pp --> t t~')
    print('----====================================================----')
    print('\n')     

    ## in the first step, we aim to calculate:
    ## - the cross section
    ## - and the maximum point of the phase space

    # set the seed for random numbers 
    seed = 12342
    random.seed(seed)

    # we also need the "ranges" (i.e. x2 - x1)
    # for costh this is 1 - (-1) = 2
    deltath = np.pi

    rho1 = np.log(mtt_min**2)#np.log(4*mt**2)
    rho2 = np.log(mtt_max**2)
    deltarho = rho2 - rho1

    # number of integration points

    N = Nsamples

    # loop over N phase space points,
    # sum the weights up (sum_w) and the weights squared (sum_w_sq) (for the variance)
    sum_w = 0
    sum_w_sq = 0

    # also define maximum point variable
    w_max = 0

    print('integrating for cross section and maximum!')
    print('...')
    #N_cut = 0
    for ii in range(0, N):
        # print progress
        sys.stdout.write("progress: %d%%   \r" % (float(ii)*100./(N)) )
        sys.stdout.flush() 

        # random theta and rho
        th = random.random() * deltath    
        rho = rho1 + random.random() * deltarho
        # get s hat
        hats = np.exp(rho)

        #selection cut
        # if np.sqrt(hats) < 1500:
        #     continue
        # get maximum rapidity of top pair, Y and find the range of integration for y (=2*Y)
        Y = - 0.5 * math.log(hats/s)
        deltay = 2 * Y
        # get a random value of y
        y = ( (2 * random.random()) - 1 ) * Y
        # calculate momentum fractions x1, x2
        x1 = math.sqrt(hats/s) * math.exp(y)
        x2 = math.sqrt(hats/s) * math.exp(-y)
        #Jacobian
        Jac = np.exp(rho)/s
        # set the scale for the pdfs
        mu = renScale() 
        # calc. phase space point weight
        w_ii = ExS.weight(np.sqrt(hats), mu, x1, x2, cSMEFT, order, NP) * deltarho * deltay * Jac  / (x1 * x2)
        # add to the sums
        sum_w = sum_w + w_ii
        sum_w_sq = sum_w_sq + w_ii**2
        # check if higher than maximum
        if w_ii > w_max:
            w_max = w_ii
            Y_max = y
            rho_max = rho
        #N_cut += 1


    sigma = sum_w / N
    print("cross section = ", sigma)

    # and its error through the variance
    variance = sum_w_sq/N - (sum_w/N)**2
    error = math.sqrt(variance/N)

    print('done integrating!')
    print('\n')
    print('maximum value of dsigma = ', w_max, 'found at (y, rho) = ', Y_max, rho_max)
    print('total cross section =', sigma * pb_convert, '+-', error * pb_convert, 'pb')

    if gen_events == False:
        return sigma * pb_convert, error * pb_convert

    print('generating events...')
    jj = 0
    PSmtt = []
    PSy = []
    while jj < N:
    # print progress
        sys.stdout.write("progress: %d%%   \r" % (float(jj)*100./(N)) )
        sys.stdout.flush() 
        deltath = np.pi

        rho1 = np.log(4*mt**2)
        rho2 = np.log(s)
        deltarho = rho2 - rho1
        # random rho  
        rho = rho1 + random.random() * deltarho
        # get s hat
        hats = np.exp(rho)
        # get maximum rapidity of top pair, Y and find the range of integration for y (=2*Y)
        Y = - 0.5 * math.log(hats/s)
        deltay = 2 * Y
        # get a random value of y
        y = ( (2 * random.random()) - 1 ) * Y
        # calculate momentum fractions x1, x2
        x1 = math.sqrt(hats/s) * math.exp(y)
        x2 = math.sqrt(hats/s) * math.exp(-y)
        #Jacobian
        Jac = np.exp(rho)/s
        # set the scale for the pdfs
        mu = renScale() 
        # calc. phase space point weight
        w_ii = ExS.weight(np.sqrt(hats), mu, x1, x2, cSMEFT, order, NP) * deltarho * deltay * Jac  / (x1 * x2)
        # now divide by maximum and compare to probability
        prob = w_ii / w_max
        rand_num = random.random()
        # if the random number is less than the probability of the PS point
        # accept
        if rand_num < prob:
            jj = jj+1
            # here one can either analyze the event
            # or store them for later convenience
            PSmtt.append(np.sqrt(hats))
            PSy.append(y)    
    PSmtt = np.array(PSmtt)
    Psy = np.array(PSy)        
    return PSmtt, PSy
