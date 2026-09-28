from sklearn import svm

input_data = [
    [5.1, 3.5, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2],
    [4.6, 3.4, 1.4, 0.3],

    [5.9, 3.0, 4.2, 1.5],
    [6.1, 2.9, 4.7, 1.4],
    [6.7, 3.1, 4.4, 1.4],
    [5.6, 2.7, 4.2, 1.3],
    [5.7, 3.0, 4.2, 1.2],

    [6.5, 3.0, 5.5, 1.8],
    [7.7, 2.6, 6.9, 2.3],
    [6.9, 3.2, 5.7, 2.3],
    [6.7, 3.1, 5.6, 2.4],
    [6.1, 2.6, 5.6, 1.4],
    [7.2, 3.0, 5.8, 1.6],
    [7.4, 2.8, 6.1, 1.9],
    [7.9, 3.8, 6.4, 2.0]
]

output_data = [
    "setosa",
    "setosa",
    "setosa",

    "versicolor",
    "versicolor",
    "versicolor",
    "versicolor",
    "versicolor",

    "virginica",
    "virginica",
    "virginica",
    "virginica",
    "virginica",
    "virginica",
    "virginica",
    "virginica",
]

model = svm.SVC()
model.fit(input_data, output_data)

res = model.predict([
    [4.4, 3.2, 1.3, 0.2],
    [6.7, 3.1, 4.7, 1.5],
    [6.5, 3.0, 5.2, 2.0],
    [5.9, 3.0, 5.1, 1.8]
])
print(res)
