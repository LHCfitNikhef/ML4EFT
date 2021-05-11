import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from matplotlib import rc
from scipy.stats import norm
import csv

def normal(z):
    return 1/(np.sqrt(2*np.pi))*np.exp(-z**2/2)

with open("z_scores/truth/tc_sm.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')

    expected_eft = 0
    expected_sm = 0
    total = 0
    mean_tc_sm = []
    mean_tauc_sm = []
    sigma_tc_sm = []
    for line in reader:
        if total == 0:
            expected_eft = float(line[0])
            expected_sm = float(line[1])
        mean_tc_sm.append(float(line[2]))
        mean_tauc_sm.append(float(line[3]))
        sigma_tc_sm.append(float(line[4]))
        total += 1

    mean_tc_sm = np.array(mean_tc_sm)
    mean_tauc_sm = np.array(mean_tauc_sm)
    sigma_tc_sm = np.array(sigma_tc_sm)

    tc_mean_sm_1 = expected_eft - expected_sm - expected_eft*np.mean(mean_tauc_sm)
    tc_mean_sm_2 = np.mean(mean_tc_sm)

with open("z_scores/truth/tc_eft.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')

    expected_eft = 0
    expected_sm = 0
    total = 0
    mean_tc_eft = []
    mean_tauc_eft = []
    sigma_tc_eft = []
    for line in reader:
        if total == 0:
            expected_eft = float(line[0])
            expected_sm = float(line[1])
        mean_tc_eft.append(float(line[2]))
        mean_tauc_eft.append(float(line[3]))
        sigma_tc_eft.append(float(line[4]))
        total += 1

    mean_tc_eft = np.array(mean_tc_eft)
    mean_tauc_eft = np.array(mean_tauc_eft)
    sigma_tc_eft = np.array(sigma_tc_eft)

    tc_mean_eft_1 = expected_eft - expected_sm - expected_eft*np.mean(mean_tauc_eft)
    tc_mean_eft_2 = np.mean(mean_tc_eft)

z_score = (mean_tc_sm - mean_tc_eft)/sigma_tc_eft
p_value = 1 - norm.cdf(z_score)
p_value_best = np.mean(p_value)
p_value_unc = np.std(p_value)/np.sqrt(len(p_value))

print(p_value_best, p_value_unc)
#print(z_score)

#print("Average z score: ", np.mean(z_score), "std z score: ", np.std(z_score))
#print("Average p value: ", 1 - norm.cdf(np.mean(z_score)))

#print(np.mean(mean_tc_eft), np.std(mean_tc_eft)/np.sqrt(len(mean_tc_eft)), expected_eft*np.std(mean_tauc_eft), np.mean(sigma_tc_eft))
#print(np.mean(mean_tc_sm), expected_sm*np.std(mean_tauc_sm), np.mean(sigma_tc_sm))



sigma_mu_mean_sm = np.std(mean_tc_sm)/np.sqrt(len(mean_tc_sm))
sigma_mu_mean_eft = np.std(mean_tc_eft)/np.sqrt(len(mean_tc_eft))
sigma_sigma_mean_eft = np.std(sigma_tc_eft)/np.sqrt(len(sigma_tc_eft))

z_score_best = (np.mean(mean_tc_sm) - np.mean(mean_tc_eft))/np.mean(sigma_tc_eft)
z_score_best_var = (sigma_mu_mean_sm**2)/(np.mean(sigma_tc_eft)**2) + (sigma_mu_mean_eft**2)/(np.mean(sigma_tc_eft)**2) + (sigma_sigma_mean_eft*np.mean(sigma_tc_eft)/z_score_best)**2
z_score_best_std = np.sqrt(z_score_best_var)

p_value_best =  1 - norm.cdf(z_score_best)
p_value_best_sigma = normal(z_score_best)*z_score_best_std

#print(z_score_best, z_score_best_std)
#print(p_value_best, p_value_best_sigma)

###########

z_mean = (np.mean(mean_tc_sm) - np.mean(mean_tc_eft))*np.mean(1/sigma_tc_eft)

var_z = np.var(mean_tc_sm)/(np.mean(sigma_tc_eft)**2) + np.var(mean_tc_sm)/(np.mean(sigma_tc_eft)**2) + (z_mean/np.mean(sigma_tc_eft))**2*np.var(sigma_tc_eft)

#print(z_mean, np.sqrt(var_z))

# print("Average first: ", tc_mean_sm_1, "Average after: ", tc_mean_sm_2)
# print("Std method 1: ", expected_eft*np.std(mean_tauc_sm), "Std method 2 ", np.std(mean_tc_sm))