import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
np.random.seed(0) #yani ek dfa jo random numbers generate huy, next time code run hony
# pr bhi vhi numbers generate hon

#  step 2 # generating random data 
heights=np.random.normal(160,10,100)
weights=0.6 * heights + np.random.normal(0,5,100)

#  step 3 # splitting the data for testing and training (hamesha 80% data ko train krty hn
# or baki 20% data ko test krty hn)
X = (heights.reshape(-1,1))
y = weights
X_train, X_test, y_train, y_test=train_test_split(X, y, train_size=0.2, random_state=42)

# step 4 # create and train linear regression model
model=LinearRegression()
model.fit(X_train, y_train)

# step 5 # make prediction using the trained model
y_pred=model.predict(X_test)  #yani ab 20% valy data ki baat ho rhi

# step 6 # visualize results
plt.scatter(X_test, y_test, color="blue", label="actual data")
plt.plot(X_test, y_pred, color="red", label="regression line")
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.title("Linear Regression: Weight vs Height")
plt.show()

