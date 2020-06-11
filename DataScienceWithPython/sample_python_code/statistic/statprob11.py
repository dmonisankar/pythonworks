import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# mean = np.mean(inter_times)
# samples = np.random.exponential(mean, size=10000)

# x, y = ecdf(inter_times)
# x_theor, y_theor = ecdf(samples)

# _ = plt.plot(x_theor,y_theor)
# _ = plt.plot(x,y,marker='.', linestyle='none')
# _ = plt.xlabel('time(days)')
# _ = plt.ylabel('CDF')
# plt.show()



def successive_poisson(tau1, tau2, size=1):
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size=size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size=size)

    return t1 + t2
	
	
# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764,715,size=100000)

# Make the histogram

_ =plt.hist(waiting_times,normed=True,bins=100,histtype='step')


# Label axes
_=plt.xlabel("Games Interval")
_=plt.ylabel("CDF")


# Show the plot
_= plt.show()


	