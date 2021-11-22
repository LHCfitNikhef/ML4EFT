#%%
import random
import numpy as np
import quad_clas.core.truth.vh_prod as vh_prod
import matplotlib.pyplot as plt


mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
luminosity = 60000
bins = np.array([mz + mh, 4]) # integration domain
a = vh_prod.findCoeff(bins) # a * eft_point = xsec

eft_point_sm = np.array([1, 0, 0, 0, 0, 0])

c1_min, c1_max = -100000, 100000
c2_min, c2_max = -100000, 100000
c1_list = np.linspace(c1_min, c1_max, 200)
c2_list = np.linspace(c2_min, c2_max, 200)

nu_efts = []
nu_sms = []
dsigmas_eft = []
dsigmas_sm = []
for c1 in c1_list:
    for c2 in c2_list:
        eft_point = np.array([1, c1, c1 ** 2, c2, c2 ** 2, c1 * c2])

        d2sigma_eft = vh_prod.dsigma_dmvh_dy(0, 0.4, c1, c2, lin=False, quad=True)
        d2sigma_sm = vh_prod.dsigma_dmvh_dy(0, 0.4, 0, 0, lin=False, quad=True)
        dsigmas_eft.append(d2sigma_eft)
        dsigmas_sm.append(d2sigma_sm)

        x_sec_eft = np.einsum('ij,i', a, eft_point)
        x_sec_sm = np.einsum('ij,i', a, eft_point_sm)

        nu_eft = x_sec_eft * luminosity
        nu_sm = x_sec_sm * luminosity

        nu_efts.append(nu_eft)
        nu_sms.append(nu_sm)

nu_efts = np.array(nu_efts)
nu_sms = np.array(nu_sms)
dsigmas_eft = np.array(dsigmas_eft)
dsigmas_sm = np.array(dsigmas_sm)

nu_efts = np.reshape(nu_efts, (len(c1_list), len(c2_list)))
nu_sms = np.reshape(nu_sms, (len(c1_list), len(c2_list)))
dsigmas = np.reshape(dsigmas_eft/dsigmas_sm, (len(c1_list), len(c2_list)))

c1_plane, c2_plane = np.meshgrid(c1_list, c2_list, indexing='ij')

fig, ax = plt.subplots(figsize=(10,6))
contour = ax.contour(c2_plane, c1_plane, nu_efts/nu_sms, levels=np.array([1]))
im = plt.imshow(nu_efts/nu_sms, origin='lower', extent=[np.min(c2_plane), np.max(c2_plane), np.min(c1_plane), np.max(c1_plane)], aspect='auto', cmap='RdBu',
               vmin = 0.8, vmax = 1.2)

#im = plt.imshow(dsigmas, origin='lower', extent=[np.min(c2_plane), np.max(c2_plane), np.min(c1_plane), np.max(c1_plane)], aspect='auto', cmap='RdBu')
x = np.linspace(np.min(c2_plane), np.max(c2_plane), 100)
plt.plot(x, -0.21742625577678323 * x, linestyle='dashed', color='k')
plt.scatter(0, 0, marker='o', color='k')
plt.xlim(np.min(c2_plane), np.max(c2_plane))
plt.ylim(np.min(c1_plane), np.max(c1_plane))
cbar = plt.colorbar(im)
plt.show()

#%%
cHq3 = 5
cHW = -0.21742625577678323 * cHq3
fig = plt.figure(figsize=(8, 5))
ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[])
x = np.linspace(1.1*(mz + mh), 2, 100)
y_sm = np.array([vh_prod.dsigma_dmvh(mvh, 0,0, lin=False, quad=True) for mvh in x])
y_eft = np.array([vh_prod.dsigma_dmvh(mvh, cHW,cHq3, lin=False, quad=True) for mvh in x])
ax1.plot(x,y_sm, label='sm')
ax1.plot(x, y_eft, label='eft')
ax1.set_yscale('log')
plt.legend()

ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18])
ax2.plot(x, y_eft / y_sm)

sigma = [vh_prod.sigma_bin(bins, -0.21742625577678323 * cHq3, cHq3, lin=True, quad=False) for cHq3 in [5]]
print(sigma)


plt.show()