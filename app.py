import numpy as np
from sklearn.linear_model import LinearRegression
x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([3,5,7,9,11])
model=LinearRegression()
model.fit(x,y)
predicton =model.predict([[6]])
print("Perdicted salary for 6 years experience:",predicton[0])

