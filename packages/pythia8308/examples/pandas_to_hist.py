import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file into a pandas dataframe
df = pd.read_csv('kinematics_vector_test_ctu8.csv')

# region columns
pt_l = df["pt_l"]
pt_lbar = df["pt_lbar"]
pt_l_lead = df["pt_l_lead"]
pt_l_trail = df["pt_l_trail"]
pt_ll = df["pt_ll"]
eta_l = df["eta_l"]
eta_lbar = df["eta_lbar"]
eta_l_lead = df["eta_l_lead"]
eta_l_trail = df["eta_l_trail"]
h_pt_l = df["h_pt_l"]
h_pt_lbar = df["h_pt_lbar"]
h_pt_l_lead = df["h_pt_l_lead"]
h_pt_l_trail = df["h_pt_l_trail"]
h_pt_ll = df["h_pt_ll"]
h_eta_l = df["h_eta_l"]
h_eta_lbar = df["h_eta_lbar"]
h_eta_l_lead = df["h_eta_l_lead"]
h_eta_l_trail = df["h_eta_l_trail"]


# endregion columns 

# region max
max_pt_l = max(pt_l.max(), h_pt_l.max())
max_pt_lbar = max(pt_lbar.max(), h_pt_lbar.max())
max_pt_l_lead = max(pt_l_lead.max(), h_pt_l_lead.max())
max_pt_l_trail = max(pt_l_trail.max(), h_pt_l_trail.max())
max_pt_ll = max(pt_ll.max(), h_pt_ll.max())
# endregion max

# region pt_l
plt.hist(pt_l, bins=50, histtype = 'step' ,edgecolor = 'blue' , fill = False, range = (50, max_pt_l), label = 'pt_l')
plt.hist(h_pt_l, bins=50, histtype = 'step' ,edgecolor = 'orange' , fill = False, range = (50, max_pt_l), label = 'h_pt_l')

plt.legend(loc='upper right')
# Add axis labels and a title
plt.xlabel('pt')
plt.ylabel('Count')
plt.title('Histogram of pt_l and h_pt_l')
plt.yscale('log')

# Display the plot
plt.savefig("pt_l_vs_h_pt_l.png")
plt.close()
# endregion pt_l

# region pt_lbar
plt.hist(pt_lbar, bins=50, histtype = 'step' ,edgecolor = 'blue' , fill = False, range = (50, max_pt_lbar), label = 'pt_lbar')
plt.hist(h_pt_lbar, bins=50, histtype = 'step' ,edgecolor = 'orange' , fill = False, range = (50, max_pt_lbar), label = 'h_pt_lbar')

plt.legend(loc='upper right')
# Add axis labels and a title
plt.xlabel('pt')
plt.ylabel('Count')
plt.title('Histogram of pt_lbar and h_pt_lbar')
plt.yscale('log')

# Display the plot
plt.savefig("pt_lbar_vs_h_pt_lbar.png")
plt.close()
# endregion pt_lbar

# region pt_l_trail
plt.hist(pt_l_trail, bins=50, histtype = 'step' ,edgecolor = 'blue' , fill = False, range = (50, max_pt_l_trail), label = 'pt_l_trail')
plt.hist(h_pt_l_trail, bins=50, histtype = 'step' ,edgecolor = 'orange' , fill = False, range = (50, max_pt_l_trail), label = 'h_pt_l_trail')

plt.legend(loc='upper right')
# Add axis labels and a title
plt.xlabel('pt')
plt.ylabel('Count')
plt.title('Histogram of pt_l_trail and h_pt_l_trail')
plt.yscale('log')

# Display the plot
plt.savefig("pt_l_trail_vs_h_pt_l_trail_test.png")
plt.close()
# endregion pt_l_trail

# region pt_l_lead
plt.hist(pt_l_lead, bins=50, histtype = 'step' ,edgecolor = 'blue' , fill = False, range = (50, max_pt_l_lead), label = 'pt_l_lead')
plt.hist(h_pt_l_lead, bins=50, histtype = 'step' ,edgecolor = 'orange' , fill = False, range = (50, max_pt_l_lead), label = 'h_pt_l_lead')

plt.legend(loc='upper right')
# Add axis labels and a title
plt.xlabel('pt')
plt.ylabel('Count')
plt.title('Histogram of pt_l_lead and h_pt_l_lead')
plt.yscale('log')

# Display the plot
plt.savefig("pt_l_lead_vs_h_pt_l_lead_test.png")
plt.close()
# endregion pt_l_lead

# region pt_ll
plt.hist(pt_ll, bins=50, histtype = 'step' ,edgecolor = 'blue' , fill = False, range = (50, max_pt_ll), label = 'pt_ll')
plt.hist(h_pt_ll, bins=50, histtype = 'step' ,edgecolor = 'orange' , fill = False, range = (50, max_pt_ll), label = 'h_pt_ll')

plt.legend(loc='upper right')
# Add axis labels and a title
plt.xlabel('pt')
plt.ylabel('Count')
plt.title('Histogram of pt_ll and h_pt_ll')
plt.yscale('log')

# Display the plot
plt.savefig("pt_ll_vs_h_pt_ll_test.png")
plt.close()
# endregion pt_ll

# region eta_l
# Plot a histogram of the 'pt_ll' column
plt.hist(eta_l, bins=50, histtype = 'step' ,edgecolor = 'blue' , fill = False, range = (-2.5,2.5), label = "eta_l")
plt.hist(h_eta_l, bins=50, histtype = 'step' ,edgecolor = 'orange' , fill = False, range = (-2.5,2.5), label = "h_eta_l")


# Add axis labels and a title
plt.legend(loc='upper right')
plt.xlabel('eta')
plt.ylabel('Count')
plt.title('Histogram of eta_l and h_eta_l')
plt.yscale('log')

# Display the plot
plt.savefig("eta_l_vs_h_eta_l_test.png")
plt.close()
# endregion eta_l

# region eta_lbar
# Plot a histogram of the 'pt_ll' column
plt.hist(eta_lbar, bins=50, histtype = 'step' ,edgecolor = 'blue' , fill = False, range = (-2.5,2.5), label = "eta_lbar")
plt.hist(h_eta_lbar, bins=50, histtype = 'step' ,edgecolor = 'orange' , fill = False, range = (-2.5,2.5), label = "h_eta_lbar")


# Add axis labels and a title
plt.legend(loc='upper right')
plt.xlabel('eta')
plt.ylabel('Count')
plt.title('Histogram of eta_lbar and h_eta_lbar')
plt.yscale('log')

# Display the plot
plt.savefig("eta_lbar_vs_h_eta_lbar_test.png")
plt.close()
# endregion eta_lbar

# region eta_l_lead
# Plot a histogram of the 'pt_ll' column
plt.hist(eta_l_lead, bins=50, histtype = 'step' ,edgecolor = 'blue' , fill = False, range = (-2.5,2.5), label = "eta_l_lead")
plt.hist(h_eta_l_lead, bins=50, histtype = 'step' ,edgecolor = 'orange' , fill = False, range = (-2.5,2.5), label = "h_eta_l_lead")


# Add axis labels and a title
plt.legend(loc='upper right')
plt.xlabel('eta')
plt.ylabel('Count')
plt.title('Histogram of eta_l_lead and h_eta_l_lead')
plt.yscale('log')

# Display the plot
plt.savefig("eta_l_lead_vs_h_eta_l_lead_test.png")
plt.close()
# endregion eta_l_lead

# region eta_l_trail
# Plot a histogram of the 'pt_ll' column
plt.hist(eta_l_trail, bins=50, histtype = 'step' ,edgecolor = 'blue' , fill = False, range = (-2.5,2.5), label = "eta_l_trail")
plt.hist(h_eta_l_trail, bins=50, histtype = 'step' ,edgecolor = 'orange' , fill = False, range = (-2.5,2.5), label = "h_eta_l_trail")


# Add axis labels and a title
plt.legend(loc='upper right')
plt.xlabel('eta')
plt.ylabel('Count')
plt.title('Histogram of eta_l_trail and h_eta_l_trail')
plt.yscale('log')

# Display the plot
plt.savefig("eta_l_trail_vs_h_eta_l_trail_test.png")
plt.close()
# endregion eta_l_trail






