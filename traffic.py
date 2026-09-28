# 1. define the problem (input and output)
# 2. collect and provide dataset
# 3. select an ML model
# 4. learn (train)
# 5. predict

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

input_data = [
    [6, 1],
    [7, 1],
    [8, 1],
    [9, 1],
    [10, 1],
    [11, 1],
    [12, 1],

    [6, 6],
    [7, 6],
    [8, 6],
    [9, 6],
    [10, 6],
    [11, 6],
    [12, 6],
]

output_data = [
    2,
    4,
    6,
    8,
    6,
    3,
    2.5,

    1,
    2,
    3,
    5,
    6,
    7,
    9
]

model = linear_model.LinearRegression()
model.fit(input_data, output_data)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(input_data)
model2 = linear_model.LinearRegression()
model2.fit(X_poly, output_data)


res = model.predict([ [8.5, 1], [10, 1], [10.5, 1], [11, 1] ])
print(res)

res2 = model2.predict(poly.transform([ [8.5, 1], [10, 1], [10.5, 1], [11, 1] ]))
print(res2)


res = model.predict([ [8.5, 6], [10, 6], [10.5, 6], [11, 6] ])
print(res)

res2 = model2.predict(poly.transform([ [8.5, 6], [10, 6], [10.5, 6], [11, 6] ]))
print(res2)
