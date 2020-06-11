#A/B testing with Approximate Bayesian Computation (ABC)
import random
import matplotlib.pyplot as plt

n_visitors_a = 100  # number of visitors shown layout A
n_conv_a = 4        # number of vistors shown layout A who converted (4%)

n_visitors_b = 40  
n_conv_b = 2

def estimate_conversion(n_visitors, n_conv, trial_conversion, n_estimates=5000):
    '''
    Return n_estimates estimates of the conversion fraction of a layout that 
    received n_visitors, n_conv of which converted.
    '''
    i = 0
    estimates = []
    while i < n_estimates:
        p = trial_conversion()
        n_sim = simulate_conversion(p, n_visitors)
        if n_conv == n_sim:
            estimates.append(p)
            i += 1
    return estimates
	
	


def trial_conversion_a():
    '''Return a random number in interval (0, 1).'''
    return random.random()

#trial_conversion_a()


def simulate_conversion(p, n_visitors):
    '''Returns number of vistors who convert given conversion fraction p.'''
    outcomes = [random.random() < p  for _ in range(n_visitors)]
    return sum(outcomes)

#simulate_conversion(0.5, 10)

a_estimates = estimate_conversion(n_visitors_a, n_conv_a, trial_conversion_a)
#len(a_estimates)


#%matplotlib inline



def trial_conversion_b():
    '''Return a random number around 0.06+/-0.02.'''
    while True:
        x = random.normalvariate(mu=0.06, sigma=0.02)
        if 0 <= x <= 1:
            return x

#trial_conversion_b()

b_estimates = estimate_conversion(n_visitors_b, n_conv_b, trial_conversion_b)
#len(b_estimates)


#%matplotlib inline

#abbins = [i/200.0 for i in range(50)]  # 50 bins between 0 and 0.25

abbins = [i/200.0 for i in range(50)]  # 50 bins between 0 and 0.25

plt.hist(a_estimates, bins=abbins, label='A', normed=True)
plt.hist(b_estimates, bins=abbins, label='B', alpha=0.5, normed=True)
plt.title('Estimates of conversion fraction for A and B after the A/B test');
plt.legend()
plt.show()


trial_as = [trial_conversion_a() for _ in range(100000)]
trial_bs = [trial_conversion_b() for _ in range(100000)]

plt.hist(trial_as, bins=abbins, label='A Before', normed=True)
plt.hist(trial_bs, bins=abbins, label='B Before', alpha=0.4, normed=True)
plt.title('Beliefs about conversion fraction prior to A/B test')
plt.legend()


b_estimates = estimate_conversion(n_visitors_b, n_conv_b, trial_conversion_b)
plt.hist(a_estimates, bins=abbins, label='A After', alpha=0.8, normed=True)
plt.hist(b_estimates, bins=abbins, label='B After', alpha=0.2, normed=True)
plt.title('Estimates of conversion fraction after the A/B test')
plt.legend()
plt.show()

# b_better = [b > a for a, b in zip(a_estimates, b_estimates)]

# print(b_better[:10])

# print(sum(b_better)/len(b_better))

