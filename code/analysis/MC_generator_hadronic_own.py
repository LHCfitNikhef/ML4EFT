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
import EFTxSec_vers_02 as ExS 

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
ECM = 13000
s = ECM**2

def generate_histo(array, name):
  
    fig, ax = plt.subplots()
    n, bins = np.histogram(array, 50)

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

# def weight(sqrts, mu, x1, x2, theta, cSMEFT):
#     if cSMEFT != 0:
#         w_ii = (ExS.dsigmadThetaggSM(sqrts, theta) +ExS.dsigmadThetaggEFT(sqrts, theta, cSMEFT) )* ( p.xfxQ(21, x1, mu) *  p.xfxQ(21, x2, mu) )     
#         w_ii += (ExS.dsigmadThetaqqSM(sqrts,theta) + ExS.dsigmadThetaqqEFT(sqrts,theta, cSMEFT))*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) +p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
#         w_ii += (ExS.dsigmadThetaqqSM(sqrts,np.pi-theta) + ExS.dsigmadThetaqqEFT(sqrts,np.pi-theta, cSMEFT))*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) + p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
#     else:#SM case
#         w_ii = (ExS.dsigmadThetaggSM(sqrts, theta) )* ( p.xfxQ(21, x1, mu) *  p.xfxQ(21, x2, mu) )         
#         w_ii += (ExS.dsigmadThetaqqSM(sqrts,theta) )*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) +p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
#         w_ii += (ExS.dsigmadThetaqqSM(sqrts,np.pi-theta) )*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) + p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
#     # multiply by ranges and Jacobian, divide by the x1 and x2 since xfxQ gives x * f(x)
#     return w_ii

# def weight_02(sqrts, mu, x1, x2, cSMEFT):
#     w_ii = ExS.sigma_part_gg(sqrts, cSMEFT)*(p.xfxQ(21, x1, mu)*p.xfxQ(21, x2, mu))   
#     w_ii += 2*ExS.sigma_part_qq(sqrts, cSMEFT)*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])#Factor of two accounts of pi - theta contribution  
#     return w_ii

#     #w_ii += ExS.sigma_part_qq(sqrts, cSMEFT)*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) +p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
# v_weight_02 = np.vectorize(weight_02)

def renScale(theta, sqrts):
    return 91.188

def MC_xSec_diff(mtt, y, cSMEFT):
    deltath = np.pi
    sum_w = 0
    x1 = mtt/np.sqrt(s)*np.exp(y)
    x2 = mtt/np.sqrt(s)*np.exp(-y)

    Jac = 2*mtt/s

    N = 10**3    
    for ii in range(0,N):
        #sys.stdout.write("progress: %d%%   \r" % (float(ii)*100./(N)) )
        #sys.stdout.flush() 
        
        theta_ii = random.random()*deltath
        mu = renScale(theta_ii, mtt) 
        w_ii = ExS.weight(mtt, mu, x1, x2, theta_ii, cSMEFT)*deltath * Jac/ (x1 * x2)
        sum_w += w_ii

    sigma_diff = sum_w / N
    return sigma_diff

vMC_xSec_diff = np.vectorize(MC_xSec_diff)

def MC_xSec(Nsamples, cSMEFT):

    print("Hadron com energy:", ECM, "GeV")
    print('\n')
    print('----====================================================----')
    print('Computing top-pair production in the EFT with ctG = %.2f' %(cSMEFT))
    print('pp --> t t~')
    print('----====================================================----')
    print('\n')

    # define a function that calculates the weight for the phase space point
    # we will multiply by the range of integration later on
    #this function will also take care of the parton density functions

        

    ## in the first step, we aim to calculate:
    ## - the cross section
    ## - and the maximum point of the phase space

    # set the seed for random numbers 
    seed = 12342
    random.seed(seed)

    # we also need the "ranges" (i.e. x2 - x1)
    # for costh this is 1 - (-1) = 2
    deltath = np.pi


    rho1 = np.log(4*mt**2)
    rho2 = np.log(s)
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
    for ii in range(0,N):
        # print progress
        sys.stdout.write("progress: %d%%   \r" % (float(ii)*100./(N)) )
        sys.stdout.flush() 

        # random theta and rho
        th = random.random() * deltath    
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
        mu = renScale(th, np.sqrt(hats)) 
        # calc. phase space point weight
        w_ii = weight(np.sqrt(hats), mu, x1, x2, th, cSMEFT) * deltath * deltarho * deltay * Jac  / (x1 * x2)
        # add to the sums
        sum_w = sum_w + w_ii
        sum_w_sq = sum_w_sq + w_ii**2
        # check if higher than maximum
        if w_ii > w_max:
            w_max = w_ii
            th_max = th
            Y_max = y
            rho_max = rho

            #Q_max = math.sqrt(hats)
    print("sum of weights:",sum_w)
     # calculate cross section
    sigma = sum_w / N

    # and its error through the variance
    variance = sum_w_sq/N - (sum_w/N)**2
    error = math.sqrt(variance/N)

    print('done integrating!')
    print('\n')
    print('maximum value of dsigma = ', w_max, 'found at (th, y, rho) = ', th_max, Y_max, rho_max)
    print('total cross section =', sigma * pb_convert, '+-', error * pb_convert, 'pb')
    return sigma*pb_convert, w_max


def MC_genEvents(Nsamples, w_max, cSMEFT):
    PSmtt = []
    PSy = []
    # Number of events to generate
    Neve = Nsamples
    # counter of events generate 
    jj = 0
    # start generating events (i.e. "hit or miss")
    print('generating events...')
    while jj < Neve:
    # print progress
        sys.stdout.write("progress: %d%%   \r" % (float(jj)*100./(Neve)) )
        sys.stdout.flush() 
        deltath = np.pi

        rho1 = np.log(4*mt**2)
        rho2 = np.log(s)
        deltarho = rho2 - rho1
        # random theta and rho
        th = random.random() * deltath    
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
        mu = renScale(th, np.sqrt(hats)) 
        # calc. phase space point weight
        w_ii = weight(np.sqrt(hats), mu, x1, x2, th, cSMEFT) * deltath * deltarho * deltay * Jac  / (x1 * x2)
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
       