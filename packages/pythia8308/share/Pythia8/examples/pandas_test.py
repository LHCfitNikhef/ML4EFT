import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file into a pandas dataframe
df = pd.read_csv('output_pt_ll.csv')

# Plot a histogram of the 'pt_ll' column
plt.hist(df['pt_ll'], bins=20)

# Add axis labels and a title
plt.xlabel('pt_ll')
plt.ylabel('Count')
plt.title('Histogram of pt_ll')
plt.yscale('log')

# Display the plot
plt.savefig("pt_ll_test.png")