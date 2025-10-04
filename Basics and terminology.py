import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
# download dataset from here -> "https://www.kaggle.com/datasets/hnazari8665/tipscsv?select=tips.csv"
# load dataset
data = pd.read_csv(r"C:\Users\Admin\Downloads\tips.csv")
df = pd.DataFrame(data)
# define features and target
features = df[['total_bill', 'size']]
target = df['tip']

# print("features: \n", features.head())
# print("target: \n", target.head())

X_train, X_test, y_train, y_test = train_test_split(
	features, target, test_size=0.2, random_state=42
)

print("traning data set: ",X_train.shape)
print("testing data set: ",X_test.shape)

#visualize relationship
sns.pairplot(df, x_vars=['total_bill', 'size'],y_vars=['tip'],height=5,aspect=0.8,kind='scatter')
plt.title('features and target relationship')
plt.show()
