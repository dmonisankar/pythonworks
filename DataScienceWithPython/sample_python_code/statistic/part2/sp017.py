# A two-sample bootstrap hypothesis test for difference of means.

# You performed a one-sample bootstrap hypothesis test, which is impossible to do with permutation. Testing the hypothesis that two samples have the same distribution may be done with a bootstrap test, but a permutation test is preferred because it is more accurate (exact, in fact). But therein lies the limit of a permutation test; it is not very versatile. We now want to test the hypothesis that Frog A and Frog B have the same mean impact force, but not necessarily the same distribution. This, too, is impossible with a permutation test.

# To do the two-sample bootstrap test, we shift both arrays to have the same mean, since we are simulating the hypothesis that their means are, in fact, equal. We then draw bootstrap samples out of the shifted arrays and compute the difference in means. This constitutes a bootstrap replicate, and we generate many of them. The p-value is the fraction of replicates with a difference in means greater than or equal to what was observed.

# The objects forces_concat and empirical_diff_means are already in your namespace.


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def bootstrap_replicate_1d(data, func):
	""" Generate bootstrap replicate of 1d data."""
	return func(np.random.choice(data, size=len(data)))
	
def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data,func)

    return bs_replicates
	
	
df = pd.read_csv('data.csv', sep='\t', header=0)
force_a= df['impact_force'][(df['ID']=='A')].tolist()
force_b= df['impact_force'][(df['ID']=='B')].tolist()

# Concatenate forces: forces_concat
forces_concat = np.concatenate((force_a,force_b))

# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = np.mean(force_a)-np.mean(force_b)

# Compute mean of all forces: mean_force
mean_force = np.mean(forces_concat)

# Generate shifted arrays
force_a_shifted = force_a - np.mean(force_a) + mean_force
force_b_shifted = force_b - np.mean(force_b) + mean_force 

# Compute 10,000 bootstrap replicates from shifted arrays
bs_replicates_a = draw_bs_reps(force_a_shifted, np.mean, 10000)
bs_replicates_b = draw_bs_reps(force_b_shifted, np.mean, 10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_replicates_a - bs_replicates_b

# Compute and print p-value: p
p = np.sum(bs_replicates >= empirical_diff_means)/ 10000
print('p-value =', p)


# Nice work! Not surprisingly, the more forgiving hypothesis, only that the means are equal as opposed to having identical distributions, gives a higher p-value. Again, it is important to carefully think about what question you want to ask. Are you only interested in the mean impact force, or the distribution of impact forces?