import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y
	

# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(n = 100,p = 0.05, size=10000)

# Compute CDF: x, y
x,y = ecdf(n_defaults)

sns.set()

# Plot the CDF with axis labels
_=plt.xlabel("loan defaults per 100 loans")
_=plt.ylabel("Probability")
_=plt.plot(x, y, marker='.', linestyle='none')



# Show the plot
_=plt.show()


# Compute bin edges: bins
bins = np.arange(0, (max(n_defaults) + 1.5) - 0.5)

# Generate histogram
plt.hist(n_defaults, normed=True, bins=bins)

# Set margins
plt.margins(0.02)

# Label axes
_=plt.xlabel("Defaults per 100 loans")
_=plt.ylabel("probability")


# Show the plot

_ = plt.show()


