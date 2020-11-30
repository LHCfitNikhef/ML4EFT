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
ECM = 13000
s = ECM**2

def weight(sqrts, mu, x1, x2, theta, cSMEFT, EFT, SM):
    if EFT == True:
        w_ii = (ExS.dsigmadThetaggSM(sqrts, theta) +ExS.dsigmadThetaggEFT(sqrts, theta, cSMEFT) )* ( p.xfxQ(21, x1, mu) *  p.xfxQ(21, x2, mu) )     
        w_ii += (ExS.dsigmadThetaqqSM(sqrts,theta) + ExS.dsigmadThetaqqEFT(sqrts,theta, cSMEFT))*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) +p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
        w_ii += (ExS.dsigmadThetaqqSM(sqrts,np.pi-theta) + ExS.dsigmadThetaqqEFT(sqrts,np.pi-theta, cSMEFT))*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) + p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
    else:
        w_ii = (ExS.dsigmadThetaggSM(sqrts, theta) )* ( p.xfxQ(21, x1, mu) *  p.xfxQ(21, x2, mu) )         
        w_ii += (ExS.dsigmadThetaqqSM(sqrts,theta) )*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) +p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
        w_ii += (ExS.dsigmadThetaqqSM(sqrts,np.pi-theta) )*( p.xfxQ(-1, x1, mu) *  p.xfxQ(1, x2, mu) +p.xfxQ(-2, x1, mu) *  p.xfxQ(2, x2, mu) +p.xfxQ(-3, x1, mu) *  p.xfxQ(3, x2, mu) +p.xfxQ(-4, x1, mu) *  p.xfxQ(4, x2, mu) + p.xfxQ(-5, x1, mu) *  p.xfxQ(5, x2, mu) )
    # multiply by ranges and Jacobian, divide by the x1 and x2 since xfxQ gives x * f(x)
    return w_ii

def renScale(theta, sqrts):
    return 91.188

def MC_xSec(Nsamples, cSMEFT, EFT = True, SM = True):

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
        w_ii = weight(np.sqrt(hats), mu, x1, x2, th, cSMEFT, EFT, SM) * deltath * deltarho * deltay * Jac  / (x1 * x2)
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
    return sigma*pb_convert



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