import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import math

def cross_section_Phi(s, mass_Phi, c_1,a):

    return c_1*(s**2 -(s/a)**3)

def cross_section_Theta(s, angle_shift_theta, c_2,a):

    return c_2 * ((s+angle_shift_theta)**2 -((s+angle_shift_theta)/a)**3)

def data_Theta(s, angle_shift_theta, c_2,num_points,a):

    mu, sigma = 0, 0.25 # mean and standard deviation
    rand = np.random.normal(mu, sigma, num_points)
    return c_2 * ((s+angle_shift_theta)**2-((s+angle_shift_theta)/a)**3) +rand 

def significant_digit(number, significant_digits):
    if number == 0:
        return 0
    else:
        return round(number, significant_digits - int(math.floor(math.log10(abs(number))) + 1))

# Physical constants
a=2.3
g_phi = 1
mass_Phi = 1 # GeV
angle_shift_theta = np.pi/2 # GeV
c_1 = 1/20
c_2 = 1/20



# Mandelstam variable s (center-of-mass energy squared) range
sqrt_s_min = 0  # GeV
sqrt_s_max = np.pi  # GeV
num_points = 1000
num_points2 = 10

# error on the measurement
mu, sigma = 0.2, 0.2 # mean and standard deviation
err = np.maximum(np.random.normal(mu, sigma, num_points2),0.1*np.ones(num_points2))
 

sqrt_s = np.linspace(sqrt_s_min, sqrt_s_max, num_points)
sqrt_s2 = np.linspace(sqrt_s_min, sqrt_s_max, num_points2)
s = sqrt_s**2
s2 = sqrt_s2**2
s0 = 1

# Compute the cross-section
sigma_Phi = cross_section_Phi(s, mass_Phi, c_1,a)
sigma_Theta = cross_section_Theta(s, angle_shift_theta, c_2,a)

sigma_Phi_err = cross_section_Phi(s2, mass_Phi, c_1,a)
sigma_Theta2_err = cross_section_Theta(s2, angle_shift_theta, c_2,a)
hor_line = 0.5*np.ones(num_points2)
data = data_Theta(s2, angle_shift_theta, c_2,num_points2,a)

MSE_Phi = significant_digit(mean_squared_error(sigma_Phi_err, data),2)
MSE_Theta = significant_digit(mean_squared_error(sigma_Theta2_err, data),2)
MSE_hor_line = significant_digit(mean_squared_error(hor_line, data),2)
MSE_Phi_formatted = f"{MSE_Phi:.2f}"
MSE_Theta_formatted = f"{MSE_Theta:.2f}"
MSE_hor_line_formatted = f"{MSE_hor_line:.2f}"

# Create plot
fig, ax = plt.subplots()
ax.plot(sqrt_s, sigma_Phi, label='Cross-section Phi, MSE = '+str(MSE_Phi_formatted))
ax.plot(sqrt_s, sigma_Theta, label='Cross-section Theta, MSE = '+str(MSE_Theta_formatted))
# ax.errorbar(sqrt_s2, data,err, fmt='o', markersize=2, label='Data', color='black')
ax.scatter(sqrt_s2, data,s=3, label='Data', color='black')

ax.set_xlabel("Center-of-mass energy")
ax.set_ylabel("Cross-section")
ax.legend()
ax.set_title("Toy model cross-section for e+e- collision")

# Add horizontal line
ax.axhline(y=0.5, color='r', linestyle='--', label='Horizontal line, MSE = '+str(MSE_hor_line_formatted))
ax.legend()

# Save plot
plt.savefig('e+e-_angle.png')

# Show plot
plt.show()