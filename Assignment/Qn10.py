import numpy as np
from sklearn.model_selection import train_test_split

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])  
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])              

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


print("X_train:\n", X_train)
print("X_test:\n", X_test)
print("y_train:\n", y_train)
print("y_test:\n", y_test)