import json
import matplotlib.pyplot as plt
get_data = open('/data/theorie/pherbsch/ML4EFT/results/nn_ctu8_subproj/posterior.json')

c_values = json.load(get_data)

print(c_values["ctu8"])

plt.hist(c_values["ctu8"])

get_data.close()