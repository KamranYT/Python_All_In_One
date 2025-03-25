import seaborn as sns 
import matplotlib.pyplot as plt 
data = sns.load_dataset('titanic')
sns.countplot(x='class', data=data)
plt.show()