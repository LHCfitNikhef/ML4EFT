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