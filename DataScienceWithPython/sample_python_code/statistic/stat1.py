# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

versicolor_petal_length = [ 4.7,  4.5,  4.9,  4. ,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5, 4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9,5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3,4.2,  4.2,  4.2,  4.3,  3. ,  4.1]

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
plt.hist(versicolor_petal_length)
plt.xlabel('Petal Length')
plt.ylabel('count of samples')

# Show histogram
plt.show()
