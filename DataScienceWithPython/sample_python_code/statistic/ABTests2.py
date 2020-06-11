import random
import itertools
import matplotlib.pyplot as plt


n_visitors_a = 100  # number of visitors shown layout A
n_conv_a = 4        # number of vistors shown layout A who converted (4%)

n_visitors_b = 40  
n_conv_b = 2

def abayes(data, prior_sampler, simulate, compare):
    '''Yield samples from the posterior by Approximate Bayesian Computation.'''
    for p in prior_sampler:
        if compare(simulate(p), data):
            yield p

def compare_conversion(sim, obs):
    '''Return True if two observations are the same.'''
    return sim == obs

#compare_conversion(42, 42), compare_conversion(42, 99)



def simulate_conversion(p, n_visitors):
    '''Returns number of vistors who convert given conversion fraction p.'''
    # This used to be "outcomes = [random.random() < p for _ in range(nvisitors)] ...which was generating list ..but now this has been changed to generator"
    outcomes = (random.random() < p for _ in range(n_visitors))
    return sum(outcomes) //this is line where actually the previous line of code is getting executed
	
def uniform_prior_sampler():
    '''Yield random numbers in interval (0, 1).'''
    while True:
        yield random.random()
		


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))
	
	
posterior_a_sampler = abayes(
    data=n_conv_a,
    prior_sampler=uniform_prior_sampler(),
    simulate=lambda p: simulate_conversion(p, n_visitors_a),
    compare=compare_conversion)
	
nsamples = 5000
a_samples = take(nsamples, posterior_a_sampler)
b_samples = take(nsamples, posterior_b_sampler)



abbins = [i/200.0 for i in range(50)]  # 50 bins between 0 and 0.25
plt.hist(a_samples, bins=abbins, label='A', normed=True)
plt.hist(b_samples, bins=abbins, label='B', alpha=0.5, normed=True)
plt.title('Estimates of conversion fraction after the A/B test')
plt.legend();